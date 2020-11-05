Provisioning a new site
=======================

## Required packages:

* Python 3.8
* Pipenv
* Git
* Nginx

eg, on Arch Linux:

    sudo pacman -S git python python-pipenv nginx

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── .venv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc