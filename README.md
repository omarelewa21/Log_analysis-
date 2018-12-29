# Log analysis project 

This is database project using sql impeded in python code. 
It works on some news database and extracts some information from it. These information are:
* Top three popular articles with counted views. 
* Listed authors with their counted articles' views. 
* Days in which number error HTTP requests exceeds 1 percent.

## Quick start
**Step1**: Setting up your environment. preferably, use FSND vagrant machine

##### vagrant installation
* Install virtualBox which is the software that actually runs the virtual machine from this link 
```
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 
```
* Donlowad vagrant from this link 
```
https://www.vagrantup.com/downloads.html
```
* Download VM configuration by forking repository ``` https://github.com/udacity/fullstack-nanodegree-vm```  and cloning it on your device.
* In your terminal, cd into **fullstack-nanodegree-vm** directory and you will find another directory called **vagrant**. 
* Change directory to the **vagrant** directory.
* In your terminal type command ```vagrant up``` to download the linux operating system and install it. 
* After finishing, run ```vagrant ssh``` to log into your newly installed linux vm. 


##### Install log analysis code
* In your command window type
```
$ git clone https://github.com/omarelewa21/Log_analysis-
```
* From your VM 
	Download newsdata.sql from this link 
``` 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
``` 
* Unzip the file and run command 
``` 
$ psql -d news -f newsdata.sql
```
* You can now explore the database using command
```psql -d news```

* In you terminal run the python code by using command
```
$ python3 log_analysis.py
``` 

### SQL code quick demo 
SQL elements used are: 
* select: Responsible for selecting distinct columns from tables. 
* where: Used to put some condition for the selection process. 
* count: Responsible for counting a partcular pattern in a column. 
* group by: used with count to aggregate based on special condition 
* inner join: method used to join two tables which have a column in common. 
* order by: Responsible for arranging rows in a column in an acending or descending order. 

###### Functions used are:
* ROUND(): Function used to get decimal values from an operation or number.
* concat(): Function used to adjust a text or string by adding parts to it. 
* cast(): function used to segregate the date from the timestamp (used in the group by for this code).







