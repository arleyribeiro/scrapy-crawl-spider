# How to install virtualenv:

### Install **pip** first

**pip** is a package management system used to install and manage software packages written in the Python programming language.

`$ sudo apt-get install python-pip`

**virtualenv** is a tool for creating virtual environments.

### Then install **virtualenv** using:

`$ sudo pip install virtualenv`

### Now create a virtual environment 

`$ virtualenv -p python3 myenv`

>you can use any name insted of **venv** and **-p** set version of Python

### Active your virtual environment:

`$ source bin/activate`

### To deactivate:

`$ deactivate`

# Install requirements

### In folder of file springer.py

Active the virtual enviroment and using

`pip install -r requirements.txt`

then run de crawler

`scrapy runspider springer.py`
