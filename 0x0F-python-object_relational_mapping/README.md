# Python - Object-relational mapping

**Please make sure your MySQL server is in 5.7. If not, please install MySQL 5.7 => Refer to this repo, 0x0D-SQL_introduction directory/README.md**

Linking Databases and Python.
In the first part, I use the module `MySQLdb` to connect to a MySQL database and execute my SQL queries.
In the second part, I use the module `SQLAlchemy`, and Object Relational Mapper (ORM).
The purpose of an ORM is to abstract the storage to the usage.
To illustrate the difference, inspect the alternatives below.
###### Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
###### With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
You might notice that all of them have the same syntanx, but not always!
### Installations
For installing `MySQLdb`, you need to have `MySQL` installed.
##### Install `MySQLdb` module version `1.3.x`
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.10'
```
##### Install `SQLAlchemy` module version `1.2.x`
```
$ sudo pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
```
You may have this warning message: You can ignore it.
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```
# Tasks
##### 0-select_states.py
A script that lists all `states` from the database `hbtn_0e_0_usa`:
- The script takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Module `MySQLdb` (`import MySQLdb`)
- The script connects to a MySQL server running on `localhost` at port `3306`
- Results are stored in ascending order by states.id
- It does not execute when imported.
##### 1-filter_states.py
A script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`
##### 2-my_filter_states.py
A cript that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched`.
- Uses `format` to create the SQL query with the user input.
##### 3-my_safe_filter_states.py
Tests `SQL injection`
A script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!