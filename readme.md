# About
This is a simple blog platform that serves blog data from markdown files in `./assets/posts/`.

This project used vue.js for the client and django for the api server.

# Usage

## Use the scripts

## Manual setup

### versions

- python 3.8.13
- nodejs v16.17.0

### python venv

Crete a python venv environment.

    $ python3 -m venv ./venv

Activate the venv.

    $ source ./venv/bin/activate
    (venv) $

Install the required dependencies, and run the django migrations.

    (venv) $ cd blog
    (venv) blog/$ pip3 install -r requirements.txt
    (venv) blog/$ python3 manage.py migrate

### npm/nodejs

npm/nodejs is used for the client application. 

Install the required dependencies:

    (venv) blog/$ cd ../blog-client  # make sure you change to the blog-client directory
    (venv) blog-client/$ npm install

## Running the blog

To run the blog you will need to run both vue and django.

### django

Make sure the virtual environment is active and you're in the blog directory.

    (venv) blog/$ python3 manage.py runserver localhost:8000

### vue js

In a separate terminal start the vue server, make sure you're in the blog-client folder.
*If you aren't running django on localhost:8000 you will need to specify this in `./blog-client/src/config.js`*

    blog-client/$ npm run dev
