# hops

Official Website of the Hops Museum - [thehopsmuseum.org](http://thehopsmuseum.org)

## Building

To build the project locally, first fork and clone the repository.

    $ cd ~/git
    $ git clone https://github.com/YOUR_USER/hops.git

Next, create a new python virtual environment and install the
`dev.txt` dependencies.

    $ virtualenv --no-site-packages ~/.virtualenvs/hops
    $ source ~/.virtualenvs/hops/bin/activate
    (hops) $ pip install -r ~/git/hops/requirements/dev.txt

Run the migrations and create a superuser for the website that will
have access to the admin panel

    (hops) $ cd ~/git/hops/
    (hops) $ python manage.py migrate
    (hops) $ python manage.py createsuperuser

Start the site locally

    (hops) $ python manage.py runserver

You should now be able to access the site from http://127.0.0.1:8000

## Contributing

For a list of outstanding bugs or features not yet implemented, be
sure to check the
[issue tracker](https://github.com/arecker/hops/issues).

### Commits

- Avoid junk merge commits in your pull request by rebasing off of
  recent `master`
- Write your commit messages in _present_ tense, noting which feature
  it pertains to
- Include the key phrase "fixes #NN" so the issue tracker can
  associate your work with a logged issue
