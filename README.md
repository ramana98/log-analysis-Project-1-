# log-analysis-Project-1-
Project Description:
	Our task is to create a reporting tool that prints out reports (in plain text) based on
 	the data in the database. This reporting tool is a Python program using the psycopg2 module to 
	connect to the database.

Questions to be reported:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Project Requirements:
1. Python 2/Python 3
2. Psql
3. Vagrant
4. Virtual box

Set-up Procedure:
1. Install Vagrant.
2. Install Virtual Box.
3. Download the project log analysis from Udacity .
4. Unzip the downloaded file and place a copy of it in vagrant file.

Start the virtual machine:
1. Open the vagrant file  right click and select git bash here.
2. Run vagrant up command to build virtual machine for the first time.
3. Once it is built run vagrant ssh command.
4. Enter into the project path by running command cd.

Commands:
1.vagrant up
2.vagrant ssh
3.sudo apt-get install python3
4.sudo apt-get install postgres
5.sudo apt-get install python-psycopg2
6.sudo apt-get install python-pip
7.sudo -i -u postgres
8.psql(enters into psql)
9.\c news(Enters into news database)

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
10.alter role vagrant login

Loading the database:
1. Once you are ready with setting up the virtual machine start running the project.
2. Enter into project path .
3. Run python file as python filename.py.

Views:
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
