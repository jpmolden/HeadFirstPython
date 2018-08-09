Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> debconfig = { 'host': '127.0.0.1',
		  'user': 'jpmolden',
		  'password': 'lukeskywalker',
		  'database': 'cuddlelogDB', }
>>> dbconfig = { 'host': '127.0.0.1',
		  'user': 'jpmolden',
		  'password': 'lukeskywalker',
		  'database': 'cuddlelogDB', }
>>> debconfig = None
>>> debconfig
>>> gd
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    gd
NameError: name 'gd' is not defined
>>> del debconfig
>>> debconfig
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    debconfig
NameError: name 'debconfig' is not defined
>>> dbconfig
{'host': '127.0.0.1', 'user': 'jpmolden', 'password': 'lukeskywalker', 'database': 'cuddlelogDB'}
>>> import mysql.connector
>>> conn = mysql.connector.connect(**dbconfig)
>>> cursor = conn.cursor()
>>> con
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    con
NameError: name 'con' is not defined
>>> conn
<mysql.connector.connection.MySQLConnection object at 0x03B0A090>
>>> conn.database()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    conn.database()
TypeError: 'str' object is not callable
>>> conn.user()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    conn.user()
TypeError: 'str' object is not callable
>>> cursor.description()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    cursor.description()
TypeError: 'NoneType' object is not callable
>>> _SQL = """show tables"""
>>> cursor.execute(_SQL)
>>> res = cursor.fetchall()
>>> res
[('log',)]
>>> _SQL = """describe log"""
>>> cursor.execute(_SQL)
>>> res = cursor.fetchall()
>>> res
[('id', b'int(11)', 'NO', 'PRI', None, 'auto_increment'), ('ts', b'timestamp', 'NO', '', None, ''), ('name', b'varchar(128)', 'NO', '', None, ''), ('email', b'varchar(128)', 'NO', '', None, ''), ('ip', b'varchar(16)', 'NO', '', None, ''), ('browser_string', b'varchar(256)', 'NO', '', None, ''), ('cuddle_num', b'varchar(64)', 'NO', '', None, '')]
>>> from pprint import pprint
>>> pprint(res)
[('id', b'int(11)', 'NO', 'PRI', None, 'auto_increment'),
 ('ts', b'timestamp', 'NO', '', None, ''),
 ('name', b'varchar(128)', 'NO', '', None, ''),
 ('email', b'varchar(128)', 'NO', '', None, ''),
 ('ip', b'varchar(16)', 'NO', '', None, ''),
 ('browser_string', b'varchar(256)', 'NO', '', None, ''),
 ('cuddle_num', b'varchar(64)', 'NO', '', None, '')]
>>> for row in res:
	print(row)

	
('id', b'int(11)', 'NO', 'PRI', None, 'auto_increment')
('ts', b'timestamp', 'NO', '', None, '')
('name', b'varchar(128)', 'NO', '', None, '')
('email', b'varchar(128)', 'NO', '', None, '')
('ip', b'varchar(16)', 'NO', '', None, '')
('browser_string', b'varchar(256)', 'NO', '', None, '')
('cuddle_num', b'varchar(64)', 'NO', '', None, '')
>>> _SQL = """insert into log
name, email, ip, browser_string, cuddle_num)
values
(%s, %s, %s, %s, %s)"""
>>> _SQL
'insert into log\nname, email, ip, browser_string, cuddle_num)\nvalues\n(%s, %s, %s, %s, %s)'
>>> print(_SQL,'','','','','')
insert into log
name, email, ip, browser_string, cuddle_num)
values
(%s, %s, %s, %s, %s)     
>>> print(_SQL,'','','','d','w')
insert into log
name, email, ip, browser_string, cuddle_num)
values
(%s, %s, %s, %s, %s)    d w
>>> cursor.execute(_SQL)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    cursor.execute(_SQL)
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\cursor.py", line 566, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 549, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 438, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name, email, ip, browser_string, cuddle_num)
values
(%s, %s, %s, %s, %s)' at line 2
>>> cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\cursor.py", line 566, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 549, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 438, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name, email, ip, browser_string, cuddle_num)
values
('Queen Bri', 'jp@gmail.com'' at line 2
>>> cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
 
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\cursor.py", line 566, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 549, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 438, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name, email, ip, browser_string, cuddle_num)
values
('Queen Bri', 'jp@gmail.com'' at line 2
>>> _SQL = """insert into log (name, email, ip, browser_string, cuddle_num) values (%s, %s, %s, %s, %s)"""
 
>>> cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
 
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    cursor.execute(_SQL, ('Queen Bri','jp@gmail.com','127.126.3','Chrome','42'))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\cursor.py", line 566, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 549, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Users\johnp_000\AppData\Local\Programs\Python\Python37-32\lib\site-packages\mysql\connector\connection.py", line 438, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.DatabaseError: 1364 (HY000): Field 'ts' doesn't have a default value
>>> hello
 
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> print('dsd')
 
dsd
>>> 
