# GQ
GQ Backend Developer Assessment


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


### 8. Install main required packages from requirements.txt
> pip3 install -r requirements.txt 

### 9. Clone project
> git clone https://github.com/shingareshubham/papi_engine.git


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
sudo nano /etc/apache2/sites-available/djangoprojectgq.conf
<VirtualHost *:80>
	ServerAdmin shingareshubham@gmail.com
	ServerName scloud24.com
	ServerAlias www.scloud24.com
	DocumentRoot /home/ubuntu/GQ
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	Alias /static /home/ubuntu/GQ/static
	<Directory /home/ubuntu/GQ/static>
		Require all granted
	</Directory>

	Alias /static /home/ubuntu/GQ/media
	<Directory /home/ubuntu/GQ/media>
		Require all granted
	</Directory>

	<Directory /home/ubuntu/GQ/grayquest>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	WSGIDaemonProcess papi_engine python-path=/home/ubuntu/GQ python-home=/home/ubuntu/GQ/env
	WSGIProcessGroup GQ
	WSGIScriptAlias / /home/ubuntu/GQ/grayquest/wsgi.py
</VirtualHost>

# Active conf file
> sudo a2ensite djangoprojectgq.conf
