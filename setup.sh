#!/usr/bin/env bash
python3 -m venv ./venv
source ./venv/bin/activate

cd blog
pip3 install -r requirements.txt
python3 manage.py migrate

cd ../blog-client
npm install

echo "Setup complete!"