# Tech Demo

This project uses a Python virtual environment:
 `source venv/bin/activate`

Project located at `/var/www/tech-demo` on the test server.

---
## Our Server Configuration

- Ubuntu 18.04
- Apache 2.4.29-1ubuntu4.14
- Python 3.6.9
- Django 3.1.3
- SQLite3 3.22.0-1ubuntu0.4
---
## Requirements

- Python 3.6
- Django 3.1
- SQLite3

If using Apache2, mod_wsgi is also needed

---
### Apache2 Config

Installation
```
sudo apt install apache2
sudo apt install apache2-dev
```
Web directory
```
sudo mkdir /var/www/tech-demo
sudo chmod 777 /var/www/tech-demo
```
Virtual host conf file
```
sudo nano /etc/apache2/sites-available/tech-demo.conf
```
```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    <Directory /var/www/tech-demo/www>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory

    WSGIDaemonProcess www python-home=/var/www/tech-demo/venv python-path=/var/www/tech-demo/www
    WSGIProcessGroup www
    WSGIScriptAlias / /var/www/tech-demo/www/www/wsgi.py
</VirtualHost>
```
Enable the new site and disable the default site
```
sudo a2ensite /etc/apache2/sites-available/tech-demo.conf
sudo a2dissite /etc/apache2/sites-available/000-default.conf
```
Restart Apache2
```
sudo service apache2 reload
```

---
### Django Config
Install pip
```
sudo apt install python3-pip
```
Install venv for the virtual environment
```
sudo apt install python3-venv
```
Install Django
```
python3 -m pip install Django
```
mod_wsgi for Apache2 and Django
```
sudo apt install python-dev
sudo apt install libapache2-mod-wsgi-py3
sudo a2enmod /etc/apache2/mods-available/wsgi
sudo service apache2 reload
```

---
### Project Config
Assuming source code is copied to `/var/www`

Project tree
```
/var/www/tech-demo/
/var/www/tech-demo/www
/var/www/tech-demo/www/db.sqlite3
/var/www/tech-demo/www/www/wsgi.py
/var/www/tech-demo/venv
/var/www/tech-demo/README.md
```
Setup
```
cd /var/www/tech-demo
source venv/bin/activate
chmod 664 www/db.sqlite3
sudo chown www-data www/db.sqlite3
sudo chown www-data www
sudo service apache2 restart
```