# News Data Database Program

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the 3 most popular articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Required Programs

The following programs are required to properly run the database project. Any programs that need to be downloaded and installed are hyperlinked below.

Required Version:
- Python version 2.7.12
- [Vagrant](https://www.vagrantup.com/)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

# Instructions

Getting started is easy and these following steps will help to ensure that you can successfully access the project.

Note: Unzip the newsdata file first and make sure that it is in your vagrant folder.

1. From the command line, navigate to the folder containing the vagrantfile.
2. Power up the virtual machine by typing: __vagrant up__ (_This may take a few minutes to complete_).
3. Once powered up, typ __vagrant ssh__.
4. Cd into the vagrant folder by typing __cd /vagrant__ (_Your command line will also direct you there as well_).
5. load the data by typing in __psql -d news -f newsdata.sql__.
+ _psql_ is the PostgreSQL command line program.
+ _-d news_ will connect you to the database named news.
+ _-f newsdata.sql_ will run the SQL statements in the newsdata.sql file.
6. Type in the command _python logsAnalysis.py_ to run file.
7. The results will not display in the command line.