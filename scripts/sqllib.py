import MySQLdb
import urllib
import jinja2
import os
import urllib
import cgi
import csv
import StringIO
import string
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from google.appengine.api import users
import webapp2
import logging

class sqllib:

    ### Scaffolding ###
	
	def ConnectToDB(self):
	  try:
		if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
		  logging.info("I should be running on the cloud right now 1<br>")
		  db = MySQLdb.connect(host='127.0.0.1-+', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
		  logging.info("I should be running on the cloud right now 2<br>")
		else:
		  logging.info("I should be running on a normal computer right now 1")
		  db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
		  logging.info("I should be running on a normal computer right now 2")
	  except:
		logging.info("Can't connect to database")
	  return db

    ### Table Functions ###	  
	
	def CreateTable(self, name):
	  logging.info("We found it boss!"); 
	  sql = 'CREATE TABLE `gsdmarin`.`%s` ( `ID` INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`ID`));' % name
	  db = self.ConnectToDB()

	  logging.info('Creating.. Table Name: %s' % (name))
	  
	  cursor = db.cursor()
	  try:
		cursor.execute(sql)
	  except:
		logging.info("Something went wrong nigga")
		return 0;
		
	  logging.info('Creation complete...')
	  logging.info('SQL:\n' + sql)
	  
	  cursor.close()
	  db.close()
	  return 1

	def PrintTable(self, name):
	  sql = "SELECT * FROM `gsdmarin`.`%s`" % name
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  try:
		cursor.execute(sql)
	  except:
		logging.info('sictik:' + sql)
		return 0
	  
	  num_fields = len(cursor.description)
	  field_names = [i[0] for i in cursor.description]
	  
	  res = []
	  res.append(str(field_names))  
	  for row in cursor.fetchall():
		res.append(', '.join(str(e) for e in row) )
	  
	  stringRepresentation = '\n'.join(res) 
	  logging.info('String representation of the queried table:\n' + stringRepresentation)
	  
	  cursor.close()
	  db.close()
	  return stringRepresentation
		  
	def RemoveTable(self, name):
	  sql = "DROP TABLE `gsdmarin`.`%s`;" % name
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  try:
		cursor.execute(sql)
	  except:
		logging.info('sictik:' + sql)
		return 0
	  cursor.close()
	  db.close()
	  return 1

    ### Entity Functions ###
	
	def ListEntities(self, name):
	  sql = "SELECT * FROM `gsdmarin`.`%s`" % name
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  try:
		cursor.execute(sql)
	  except:
		logging.info('sictik:' + sql)
		return 0
	  
	  num_fields = len(cursor.description)
	  field_names = [i[0] for i in cursor.description]
	  entities = []
	  for f in field_names:
		entities.append([f])
	  
	  for row in cursor.fetchall():
		i=0
		for ele in row:
		  entities[i].append(ele)
		  i += 1
	  
	  print entities
	  return entities
	  
	def RemoveEntity(self, name, id):
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  sql = "DELETE FROM `gsdmarin`.`%s` WHERE ID = %s;" % (name, id)
	  
	  try:
		cursor.execute(sql)
		db.commit()
	  except:
		print "sictik ki ne sictikkk"
		print sql
		return 0
		
	  return 1  	  
	  
	def AddEntity(self, name):
	  sql = "SELECT * FROM `gsdmarin`.`%s` LIMIT 1" % name
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  try:
		cursor.execute(sql)
	  except:
		logging.info('sictik:' + sql)
		return 0
	  
	  nulls = "null"
	  num_fields = len(cursor.description)-1
	  while num_fields > 0:
		num_fields-=1
		nulls += ',null'
	  sql = "INSERT INTO `gsdmarin`.`%s` VALUES(%s);" % (name, nulls)
	  
	  try:
		cursor.execute(sql)
		db.commit()
	  except:
		logging.info('sictik:' + sql)
		return 0
	  
	  cursor.close()
	  db.close()
	  return cursor.lastrowid

	def AddEntityWithValues(self, name, dict):
	  db = self.ConnectToDB()
	  db.autocommit(False) # start transaction
	  cursor = db.cursor()
	  try:
		for row in range(1,len(dict[0])):  
		  sql = []
		  sql.append("INSERT INTO `gsdmarin`.`%s` (" % name)
		  for col in range(0,len(dict)-1):
			sql.append("`%s`," % dict[col][0])
		  sql.append("`%s`)" % dict[len(dict)-1][0])
		  sql.append("VALUES (")    
		  for col in range(0,len(dict) - 1):
			sql.append("'%s'," % dict[col][row])
		  sql.append("'%s' );" % dict[len(dict) - 1][row])
		  print "----\n%s\n----" % ' '.join(sql)
		  cursor.execute(' '.join(sql))
		db.commit()
	  except:
		db.rollback()
		print "make sure that the column names are exactly the same as the column names in the real table"
		return 0

	  cursor.close()
	  db.close()
	  return cursor.lastrowid

	### Attribute Functions ###
	
	def AddAttribute(self, name, attribute, type):
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  sql = "ALTER TABLE `gsdmarin`.`%s` ADD COLUMN `%s` %s NULL ;" % (name,attribute, type)
	  print sql
	  
	  try:
		cursor.execute(sql)
		db.commit()
	  except:
		print "sictik ki ne sictikkk"
		return 0
		
	  return 1

	def RemoveAttribute(self, name, attribute):
	  db = self.ConnectToDB()
	  cursor = db.cursor()
	  
	  sql = "ALTER TABLE `gsdmarin`.`%s` DROP COLUMN `%s`;" % (name, attribute)

	  try:
		cursor.execute(sql)
		db.commit()
	  except:
		print "sictik ki ne sictikkk"
		print sql
		return 0
		
	  return 1

    ### Value Functions ###
	def GetValue(table, id, attribute):
	  sql = "SELECT `%s` FROM `gsdmarin`.`%s` WHERE ID = '%s';" % (attribute, table, id)
	  db = ConnectToDB()
	  cursor = db.cursor()
	  
	  try:
	    cursor.execute(sql)
	  except:
	    logging.info('sictik:' + sql)
	    return 0  
	  
	  for row in cursor.fetchall():
	    res = row[0]
	  
	  cursor.close()
	  db.close()
	  return res
	  
	def SetValue(table, id, attribute, value):
	  db = ConnectToDB()
	  cursor = db.cursor()
	  sql = "UPDATE `gsdmarin`.`%s` SET `%s`='%s' WHERE `ID`='%s';" % (table,attribute,value,id)

	  try:
	    cursor.execute(sql)
	    db.commit()
	  except:
	    print "sictik ki ne sictikkk"
	    print sql
	    return 0
	  
	  cursor.close()
	  db.close()  
	  return 1 

	def SetAllEntities(table, attribute, value):
	  db = ConnectToDB()
	  cursor = db.cursor()
	  sql = "UPDATE `gsdmarin`.`%s` SET `%s`='%s' WHERE `ID` > '0';" % (table, attribute, value)
	  try:
	    cursor.execute(sql)
	    db.commit()
	  except:
	    print "sictik ki ne sictikkk"
	    print sql
	    return 0
	  
	  cursor.close()
	  db.close()  
	  return 1 

	def SetAllAttributes(table, id, dict):
	  sql = "UPDATE `gsdmarin`.`%s`" % table
	  sql = [sql]
	  sql.append("SET")
	  middle = []
	  for i in range(0,len(dict)):
	    middle.append("`%s` = '%s'" % (dict[i][0],dict[i][1]))
	  sql.append(', '.join(middle))
	  sql.append("WHERE ID = %s;" % id)
	  
	  sql = ' '.join(sql)
	  print sql
	  db = ConnectToDB()
	  cursor = db.cursor()
	  try:
	    cursor.execute(sql)
	    db.commit()
	  except:
	    print "sictik ki ne sictikkk"
	    print sql
	    return 0
	  
	  cursor.close()
	  db.close()  
	  return 1