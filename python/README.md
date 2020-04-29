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

## Reference

reference: [Digital Ocean Tutorials](https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt)

reference: [Like Geeks](https://likegeeks.com/downloading-files-using-python/)

