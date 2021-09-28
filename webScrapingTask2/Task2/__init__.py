import mysql.connector as connector

#connect to phpMyAdmin as root user
con = connector.connect(host="localhost",user="root")

if con.is_connected():
    dbInfo = con.get_server_info()
     
#create a cursor object to execute queries
cursor = con.cursor()
 
#create database named WebScrapingT2
cursor.execute("Create Database WebScrapingT2")

#use the database WebScrapingT2 created for further operations
cursor.execute("Use WebScrapingT2")

#create the tables as specified with columns as specified
cursor.execute("create table JobTypes1(Categories varchar(30) primary key)")
cursor.execute("create table JobTypes2(Subcategories varchar(30) primary key)")
cursor.execute("create table States(State varchar(30) primary key)")
cursor.execute("create table CompanyDetails(Name varchar(30),Description varchar(80),State varchar(30) references States(State),Subcategories varchar(30) references JobTypes2(Subcategories))")
cursor.execute("create table Jobs(Company varchar(30), JobPosition varchar(30), Location varchar(40))")



