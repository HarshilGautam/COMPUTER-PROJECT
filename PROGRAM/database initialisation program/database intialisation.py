import mysql.connector as pyt
mycon=pyt.connect(host="localhost",user='root',password="prashu@1910")
csr=mycon.cursor()
a="create database if not exists cricbook"
f="use cricbook"
b="create table if not exists name(name varchar(100),ticket_number varchar(100) primary key,phone_number varchar(10) unique key,date varchar(10) unique key,no_seats integer(100))"
c="create table if not exists matches(matches varchar(100),ticket_number varchar(100) ,phone_number varchar(10),date varchar(10) unique key)"
d="alter table matches add foreign key (ticket_number) references name(ticket_number) on delete cascade"
e="alter table matches add foreign key (phone_number) references name(phone_number) on delete cascade"
g="alter table matches add foreign key (date) references name(date) on delete cascade"
csr.execute(a)
mycon.commit
csr.execute(f)
mycon.commit
csr.execute(b)
mycon.commit
csr.execute(c)
mycon.commit
csr.execute(d)
mycon.commit
csr.execute(e)
mycon.commit
print("database succesfully imported")
