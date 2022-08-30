# Instructions

How to setup and run this application.

## Python and Django

### Setup virtual environment

First create the virtual environment using venv, in the root of this project run:

    $ python3 -m venv ./venv

Activate the virtual environment and install the dependencies:

    $ ./venv/bin/activate
    $ pip3 install -r ./blog/requirements.txt

### Start the backend

Now the Django server can be run with:

    $ cd blog
    $ python3 manage.py runserver

