# Log analysis project 

This is database project using sql impeded in python code. 
It works on some news database and extracts some information from it. These information are:
* Top three popular articles with counted views. 
* Listed authors with their counted articles' views. 
* Days in which number error HTTP requests exceeds 1 percent.

## Quick start

In your command window type
```
$ git clone https://github.com/omarelewa21/Movie_website
```
either from a virtual machine or directly on your terminal type 
Download newsdata.sql from this link 
``` 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
``` 
``` 
$ psql -d news -f newsdata.sql
```
You can now explore the database using command
```psql -d news```

In you terminal run the python code by using command
```
$ python3 log_analysis.py
``` 
### SQL code demo 
SQL elements used are: 
* Create view as: a method for creating temporary table in order to be used afterwards. 
* select: Responsible for selecting distinct columns from tables. 
* where: Used to put some condition for the selection process. 
* count: Responsible for counting a partcular pattern in a column. 
* group by: used with count to aggregate based on special condition 
* having: used to specify some conditions after group by. 
* ROW_NUMBER(): SQL function which gives each row a number in a tabe. 
* inner join: method used to join two tables which have a column in common. 
* sum: Gives the sum of all numbers in a cloumn.
* order by: Responsible for arranging rows in a column in an acending or descending order. 







