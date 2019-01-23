# log-analysis-Project-1-
Project Description:
	Our task is to create a reporting tool that prints out reports (in plain text) based on
 	the data in the database. This reporting tool is a Python program using the psycopg2 module to 
	connect to the database.

Questions to be reported:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Technologies:
-->Python 2/Python 3
-->Psql
-->Vagrant
-->Virtual box

Procedure:
-->vagrant box add ubuntu/trusty64
-->vagrant init
-->vagrant up
-->vagrant ssh
-->sudo apt-get install python3
-->sudo apt-get install python-pip
-->sudo apt-get install postgres
-->sudo apt-get install python-psycopg2

Designing of roles:
1.create role vagrant
2.alter user vagrant with superuser
3.alter user vagrant with createrole
4.alter user vagrant with createdb
5.alter user vagrant with replication
6.create database vagrant
7.create database news
8.alter database vagrant owner to vagrant
9.alter database news owner to vagrant

Loading the database:
-->psql -d news -f newsdata.sql(loads data into news)
-->python filename.py(to run python file)
We need to create views as:
query 1:
	create view firstquery as select title,count(title) as amount 
	from articles,log where articles.slug=substr(log.path,10) group
	 by title;
query 2:
	 create view secondquery as select authors.name,count(authors.name) 
		as total from articles,log,authors where 
	articles.slug=substr(log.path,10) and articles.author=authors.id group by name;
query 3:
	create view thirdquery as  select date(time),
            round(100.0*sum(case log.status when '200 OK' then 0 else 1
            end)/count(log.status) , 2) as per from log group by
            date(time) order by per desc;
