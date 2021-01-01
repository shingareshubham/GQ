# GQ
GQ Backend Developer Assessment

# Deploued on AWS

Created seperate private repo and deployed this project on AWS added AWS Postgres RDS.
# Functionality
> User registration
> User login
> Created own mems API. url: http://www.scloud24.com/api/photogallary/v1/getall/



# Home page url
www.scloud24.com
# Assignment url
> http://www.scloud24.com/userAccount/login/

## AWS Ubuntu instance

### 1. Connect EC2 instance using ssh

### 2. Go to the roor
> sudo su

### 3. Update and upgrade system
> apt-get update</br>
> apt-get upgrade

### 4. install java
> apt-get install openjdk-8-jre

### 6. Python Installation and virtual environment creation
> apt-get install python3-venv    # Install virtual env package</br>
> python3 -m venv env             # Create virtual environment</br>
> source env/bin/activate         # Activate environment</br>


### 8.  requirements.txt
> pip freeze > requirements.txt     --- Create requirements
> pip3 install -r requirements.txt  --- Install all apckage

### 9. Clone project
> git clone https://github.com/shingareshubham/gq.git


# Check which port is running for which service
> lsof -i -P -n | grep LISTEN


# Install Apache2 for djnago
> sudo apt-get install apache2</br>
> sudo apt-get install libapache2-mod-wsgi
> sudo apt-get install libapache2-mod-wsgi-py3

> systemctl restart apache2</br>
> systemctl stop apache2</br>

# check wsgi is install or not
> sudo a2enmod wsgi

# create django_conf file in apache
sudo nano /etc/apache2/sites-available/scloud24.conf

<VirtualHost *:80>
	ServerAdmin shingareshubham@gmail.com
	ServerName scloud24.com
	ServerAlias www.scloud24.com
	DocumentRoot /home/ubuntu/scloud24/papi
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	Alias /static /home/ubuntu/scloud24/papi/static
	<Directory /home/ubuntu/scloud24/papi/static>
		Require all granted
	</Directory>

	Alias /static /home/ubuntu/scloud24/papi/media
	<Directory /home/ubuntu/scloud24/papi/media>
		Require all granted
	</Directory>

	<Directory /home/ubuntu/scloud24/papi/papi>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	WSGIDaemonProcess scloud24 python-path=/home/ubuntu/scloud24/papi python-home=/home/ubuntu/scloud24/env
	WSGIProcessGroup scloud24
	WSGIScriptAlias / /home/ubuntu/scloud24/papi/papi/wsgi.py
</VirtualHost>

