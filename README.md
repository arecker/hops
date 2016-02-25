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
        ... (output)
    (hops) $ python manage.py createsuperuser

Start the site locally

    (hops) $ python manage.py runserver

You should now be able to access the site from http://127.0.0.1:8000
