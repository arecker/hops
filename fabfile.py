import os

from fabric.api import run, sudo, env, cd
from fabric.contrib import files
from fabric.contrib.project import rsync_project
import yaml


env['use_ssh_config'] = True


class Config(object):
    def __init__(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        secret_path = os.path.join(cur_dir, 'secrets.yml')
        with open(secret_path, 'r') as stream:
            self.data = yaml.load(stream)

        self.data['cur_dir'] = cur_dir

    def get(self, key, default=None):
        return self.data.get(key, default)


class PackageInstaller(object):
    def __init__(self):
        self.config = Config()

    def run(self):
        deps_string = ' '.join(self.config.get('dependencies'))
        if deps_string:
            sudo('apt-get update')
            sudo('apt-get install -y {}'.format(deps_string))


class SourcePusha(object):
    def __init__(self):
        self.config = Config()
        self.payload = os.path.dirname(self.config.get('cur_dir'))
        self.payload = os.path.join(self.payload, '')
        self.target = self.config.get('src_path')
        self.target = os.path.join(self.target, '')

    def run(self):
        run('mkdir -p {}'.format(os.path.dirname(self.target)))
        excludes = ('.git', 'temp', 'deployment',
                    'uploads', '*.pyc')
        rsync_project(local_dir=self.payload,
                      remote_dir=self.target,
                      exclude=excludes,
                      delete=True)


class VirtualEnvInstaller(object):
    def __init__(self):
        config = Config()
        self.env_path = config.get('env_path')
        self.src_path = config.get('src_path')
        self.reqs = os.path.join(self.src_path, 'requirements/prod.txt')

    def run(self):
        if not files.exists(self.env_path):
            run('mkdir -p {}'.format(self.env_path))
            run('virtualenv --no-site-packages {}'
                .format(self.env_path))
        with cd(self.env_path):
            run('./bin/pip install -r {}'
                .format(self.reqs))


class DatabaseThingy(object):
    def __init__(self):
        config = Config()
        self.db_name = config.get('db_name')
        self.db_pass = config.get('db_pass')
        self.db_user = config.get('db_user')

    def _db_exists(self):
        mess = 'psql -lqt | cut -d \| -f 1 | grep -w {0} | wc -l'  # never touching this again
        return sudo(mess.format(self.db_name), user='postgres') == '1'

    def _create_db(self):
        sudo('psql -c "CREATE DATABASE {0};"'.format(self.db_name), user='postgres')
        sudo('psql -c "CREATE USER {0} WITH PASSWORD {1};"'
             .format(self.db_user, '\'' + self.db_pass + '\''), user='postgres')
        sudo('psql -c "GRANT ALL PRIVILEGES ON DATABASE {0} TO {1};"'
             .format(self.db_name, self.db_user), user='postgres')  # check yo privelege

    def run(self):
        if self._db_exists():
            return
        self._create_db()


class SettingsChanger(object):
    def __init__(self):
        config = self.config = Config()
        src = config.get('src_path')
        self.manage_target = os.path.join(src, 'manage.py')
        self.wsgi_target = os.path.join(src, 'hops/wsgi.py')
        self.settings_target = os.path.join(src, 'hops/settings/prod.py')

    def run(self):
        files.sed(self.manage_target,
                  'hops.settings.dev',
                  'hops.settings.prod')

        files.sed(self.wsgi_target,
                  'hops.settings.dev',
                  'hops.settings.prod')

        change_list = ['secret_key',
                       'host',
                       'db_name',
                       'db_user',
                       'db_pass',
                       'db_port',
                       'static_root',
                       'media_root',
                       'log_path']

        for term in change_list:
            before = '%{}%'.format(term.upper())
            after = self.config.get(term)
            files.sed(self.settings_target, before, after)


class DjangoProjectPrepper(object):
    def __init__(self):
        config = Config()
        self.user = config.get('user')
        self.static_root = config.get('static_root')
        self.media_root = config.get('media_root')
        self.python = os.path.join(config.get('env_path'),
                                   'bin/python')
        self.manage = os.path.join(config.get('src_path'), 'manage.py')
        self.log = config.get('log_path')

    def run(self):
        run('mkdir -p {}'.format(os.path.dirname(self.log)))
        run('touch {}'.format(self.log))

        run('{} {} migrate'.format(self.python, self.manage))

        for thing in [self.static_root, self.media_root]:
            sudo('mkdir -p {}'.format(thing))
            sudo('chown -R {}:www-data {}'.format(self.user, thing))

        sudo('chmod 777 {}'.format(self.media_root))

        run('{} {} collectstatic --noinput'
            .format(self.python, self.manage))


class BaseTemplatePusher(object):
    template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configs')

    def _put_template(self, filename=None, destination=None, context=None, use_sudo=False):
        files.upload_template(
            filename=filename,
            destination=destination,
            context=context,
            use_jinja=True,
            template_dir=self.template_dir,
            use_sudo=use_sudo
        )


class SystemdThingy(BaseTemplatePusher):
    def __init__(self):
        config = Config()
        self.user = config.get('user')
        self.port = config.get('systemd_port')
        self.desc = config.get('systemd_desc')
        self.file = config.get('systemd_file')
        self.log = config.get('log_path')
        self.working = config.get('src_path')
        self.env = config.get('env_path')

    def run(self):
        destination = os.path.join('/etc/systemd/system/', self.file)
        wsgi = 'hops.wsgi'
        gunicorn = os.path.join(self.env, 'bin/gunicorn')

        context = {'description': self.desc,
                   'user': self.user,
                   'working_dir': self.working,
                   'port': self.port,
                   'log': self.log,
                   'wsgi': wsgi,
                   'gunicorn': gunicorn}

        self._put_template(filename='systemd.txt',
                           destination=destination,
                           context=context,
                           use_sudo=True)

        sudo('systemctl daemon-reload')
        sudo('systemctl enable {service} && systemctl restart {service}'
             .format(service=self.file))
        sudo('systemctl status {}'.format(self.file))


class NginxThingy(BaseTemplatePusher):
    def __init__(self):
        config = Config()

        static_root = os.path.join(config.get('static_root'), '')
        media_root = os.path.join(config.get('media_root'), '')

        self.context = {'domain': config.get('host'),
                        'site_root': config.get('site_root'),
                        'static_root': static_root,
                        'media_root': media_root,
                        'port': config.get('systemd_port'),
                        'log': config.get('log_path')}
        self.destination = os.path.join('/etc/nginx/sites-available/',
                                        config.get('nginx_file'))
        self.link = self.destination.replace('sites-available',
                                             'sites-enabled')

    def run(self):
        self._put_template(filename='nginx.txt',
                           destination=self.destination,
                           context=self.context,
                           use_sudo=True)

        if files.exists(self.link):
            sudo('rm {}'.format(self.link))

        sudo('ln -s {} {}'.format(self.destination, self.link))
        sudo('nginx -s reload')


class HostFileThingy():
    def __init__(self):
        self.domain = Config().get('host')

    def run(self):
        entry = '127.0.0.1 {}'.format(self.domain)
        files.append('/etc/hosts', entry, use_sudo=True)


def handshake():
    run('echo "Hello from $(hostname)"')


def deploy():
    PackageInstaller().run()
    SourcePusha().run()
    VirtualEnvInstaller().run()
    DatabaseThingy().run()
    SettingsChanger().run()
    DjangoProjectPrepper().run()
    SystemdThingy().run()
    NginxThingy().run()
    HostFileThingy().run()
