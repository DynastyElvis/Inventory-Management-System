Excel inventory management can help companies keep track of their existing inventory items. Using Excel worksheets, users can manually enter their product details into rows and columns to organize stock counts, check availability, and adjust these numbers as goods are sold

## Author  
  
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)


GITHUB - [ELVIS](https://github.com/DynastyElvis)

  
 
##  Live Link  
 Click [View Site](https://elvis-inventory-system.herokuapp.com/)  to visit the site


[Go Back to the top](#Inventory-Management-System)

## Screenshots 
###### User DASHBOARD
 
<img src="https://raw.githubusercontent.com/DynastyElvis/Inventory-Management-System/main/Files/Screenshot%20from%202022-10-23%2023-13-39.png">
 

 ###### User Inventory Page
 <img src="https://raw.githubusercontent.com/DynastyElvis/Inventory-Management-System/main/Files/Screenshot%20from%202022-10-23%2023-13-55.png">


  ###### Admin superuser Section authentication
 <img src="https://raw.githubusercontent.com/DynastyElvis/Inventory-Management-System/main/Files/Screenshot%20from%202022-10-23%2023-14-20.png">


 ###### Admin superuser Section authentication
 <img src="https://raw.githubusercontent.com/DynastyElvis/Inventory-Management-System/main/Files/Screenshot%20from%202022-10-23%2023-15-00.png">

 ###### Admin Excel file importation for file inventory management
 <img src="https://raw.githubusercontent.com/DynastyElvis/Inventory-Management-System/main/Files/Screenshot%20from%202022-10-23%2023-15-22.png">


<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
	

	
	Alias /static /home/Desktop/My Dev Apps/inventory_management-master/inventory_management_system/static
<Directory /home/Desktop/My Dev Apps/inventory_management-master/inventory_management_system/static>
    Require all granted
</Directory>

<Directory /home/Desktop/My Dev Apps/inventory_management-master/inventory_management_system>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess inventory_management_system python-home=/home/Desktop/My Dev Apps/inventory_management-master/virtual python-path=/home/Desktop/My Dev Apps/inventory_management-master/inventory_management_system
WSGIProcessGroup inventory_management_system
WSGIScriptAlias / /home/Desktop/My Dev Apps/inventory_management-master/inventory_management_system/wsgi.py



</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

