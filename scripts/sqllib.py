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
from tuplelib import pair 

class sqllib:

		### Scaffolding ###
	
	def ConnectToDB(self):
		try:
			if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
				#Eger code deployedsa buradayim
				logging.info("I should be running on the cloud right now 1<br>")
				#Documentation @ https://cloud.google.com/appengine/docs/python/cloud-sql/
				db = MySQLdb.connect(unix_socket='/cloudsql/gsdmarin-info:database', db='gsdmarin', user='root')
				logging.info("I should be running on the cloud right now 2<br>")
			else:
				#LOCAL - Ancak gercek sql'e connected
				logging.info("I should be running on a normal computer right now 31")
				#db = MySQLdb.connect(unix_socket='/cloudsql/gsdmarin-info:database', db='gsdmarin', user='root')

				db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='batu', passwd='1234')

				logging.info("I should be running on a normal computer right now 2")
		except:
			logging.info("Can't connect to database")
		return db

		### Table Functions ###	  
	
	def CreateTable(self, name, page):
		sql1 = "CREATE TABLE `gsdmarin`.`%s` ( `ID` INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`ID`));" % name
		sql2 = "INSERT INTO `gsdmarin`.`MASTER` (`TABLE`,`PAGE`) VALUES ('%s','%s')" % (name, page)
		
		db = self.ConnectToDB()
		db.autocommit(False) # start transaction

		logging.info('Creating.. Table Name: %s' % (name))
		
		cursor = db.cursor()
		try:
			cursor.execute(sql1)
			cursor.execute(sql2)
			db.commit()
		except:
			logging.info("Something went wrong nigga")
			db.rollback()
			self.RemoveTable(name, page)
			return 0;
		
		logging.info('Creation complete...')
		logging.info('SQL1:\n' + sql1)
		logging.info('SQL2:\n' + sql2)
		
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
			
	def RemoveTable(self, name, page):
		sql1 = "DELETE FROM `gsdmarin`.`MASTER` WHERE `TABLE` = '%s' AND `PAGE` = '%s';" % (name, page) #deletes from META automatically because they're connected via foreign key relationship
		sql2 = "DROP TABLE `gsdmarin`.`%s`;" % name
		db = self.ConnectToDB()
		cursor = db.cursor()
		
		try:
			cursor.execute(sql1)
			db.commit()
			cursor.execute(sql2)
		except:
			logging.info('sictik:\n' + sql1 + "\n" + sql2)
			return 0

		cursor.close()
		db.close()
		return 1

		### Page Functions ###
	def AddPage(self, name, type):
		db = self.ConnectToDB()
		db.autocommit(False) # start transaction
		cursor = db.cursor()
		try:
			sql = "INSERT INTO `gsdmarin`.`PAGES` (`Name`,`Type`) VALUES ('" + name + "','" + type + "');"
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			print "make sure that the column names are exactly the same as the column names in the real table"
			return 0

		cursor.close()
		db.close()
		return cursor.lastrowid
		
	def RemovePage(self, name):
		db = self.ConnectToDB()
		cursor = db.cursor()
		sql1 = "DELETE FROM `gsdmarin`.`PAGES` WHERE 'Name' = '%s';" % name
		sql2 = "DELETE FROM `gsdmarin`.`MASTER` WHERE 'PAGE' = '%s';" % name
		try:
			cursor.execute(sql1)
			db.commit()
			cursor.execute(sql2)
			db.commit()
		except:
			print "sictik ki ne sictikkk"
			print sql1
			print sql2
			return 0
		
		return 1  		 	  
		
		
		### Entity Functions ###
	def ListAllEntities(self, name):
		db = self.ConnectToDB()
		cursor = db.cursor()
		
		sql = "SELECT `ID` FROM `gsdmarin`.`MASTER` WHERE `TABLE` = '%s';" % name
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0
		
		for row in cursor.fetchall():
			for r in row:
				id_ = r

		sql = "SELECT * FROM `gsdmarin`.`%s`" % name
		
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0
		
		num_fields = len(cursor.description)
		field_names = [i[0] for i in cursor.description]
		entities = []
		i=0
		for f in field_names:
			entities.append([f])			
			entities[i].append(self.GetMetaValue(id_,f,db))
			i = i + 1

		
		for row in cursor.fetchall():
			i=0
			for ele in row:
				entities[i].append(ele)
				i += 1
		
		cursor.close()
		db.close()
		return entities
	
	def GetEntityByID(self, name, id):
		db = self.ConnectToDB()
		cursor = db.cursor()
		
		sql = "SELECT * FROM `gsdmarin`.`%s` WHERE ID = %s;" % (name, id)
		
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print "sictik ki ne sictikkk"
			print sql
			return 0
		
		return 1  	
	
	def GetEntitiesByAttr(self, name, attribute, value):
		db = self.ConnectToDB()
		cursor = db.cursor()

		sql = "SELECT * FROM `gsdmarin`.`%s` WHERE `%s` = '%s';" % (name, attribute, value)
		
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0
		first = 1;
		res = []
		for row in cursor.fetchall():
			if first == 1:				
				for c in row:
					print "c:" + str(c)
					res.append([c])
				first = 0
			else:
				i=0
				for c in row:
					res[i].append(c)
					i = i + 1
		cursor.close()
		db.close()
		return res
		
		
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

	def RemoveAllEntities(self, name):
		db = self.ConnectToDB()
		cursor = db.cursor()
		sql = "TRUNCATE TABLE `gsdmarin`.`%s`;" % (name)
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
	
	def AddAttribute(self, name, page, attribute, type_, class_):
		db = self.ConnectToDB()
		cursor = db.cursor()

		# obtain the id.
		sql = "SELECT `ID` FROM `gsdmarin`.`MASTER` WHERE `TABLE` = '%s' AND `PAGE` = '%s';" % (name, page)
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0  
		id_ = -1	
		for row in cursor.fetchall():
			id_ = row[0]
		if id_ == -1:
			print "clouln't get the id of the page-table pair. Probably table don't exist in MASTER"
			return 0
		
		sql1 = "ALTER TABLE `gsdmarin`.`%s` ADD COLUMN `%s` %s NULL ;" % (name,attribute, type_)
		sql2 = "INSERT INTO `gsdmarin`.`META` (`ID`, `COLUMN_NAME`, `CLASS`) VALUES (%s, '%s', '%s');" % (id_, attribute, class_)
		print sql1
		print sql2

		try:
			cursor.execute(sql1)
			db.commit()
			cursor.execute(sql2)
			db.commit()
		except:
			print "sictik ki ne sictikkk"
			return 0
		
		return 1

	def RemoveAttribute(self, name, page, attribute):
		db = self.ConnectToDB()
		cursor = db.cursor()
		
		# obtain the id.
		sql = "SELECT `ID` FROM `gsdmarin`.`MASTER` WHERE `TABLE` = '%s' AND `PAGE` = '%s';" % (name, page)
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0  
		id_ = -1	
		for row in cursor.fetchall():
			id_ = row[0]
		if id_ == -1:
			print "clouln't get the id of the page-table pair. Probably table don't exist in MASTER"
			return 0

		sql1 = "ALTER TABLE `gsdmarin`.`%s` DROP COLUMN `%s`;" % (name, attribute)
		sql2 = "DELETE FROM `gsdmarin`.`META` WHERE `ID` = '%s' AND `COLUMN_NAME` = '%s';" % (id_, attribute)

		try:
			cursor.execute(sql1)
			db.commit()
			cursor.execute(sql2)
			db.commit()
		except:
			print "sictik ki ne sictikkk"
			print sql1
			print sql2
			return 0
		
		return 1

	### Value Functions ###
	def GetMetaValue(self, id_, col_name,db):
		cursor = db.cursor()
		sql = "SELECT `CLASS` FROM `gsdmarin`.`META` WHERE `ID` = '%s' AND `COLUMN_NAME` = '%s';" % (id_, col_name)
		try:
			cursor.execute(sql)
		except:
			logging.info('sictik:' + sql)
			return 0
		for row in cursor.fetchall():
			return row[0]
		return -1

	def GetValue(self, table, id, attribute):
		sql = "SELECT `%s` FROM `gsdmarin`.`%s` WHERE ID = '%s';" % (attribute, table, id)
		db = self.ConnectToDB()
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
		
	def SetValue(self, table, id, attribute, value):
		db = self.ConnectToDB()
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

	def SetAllEntities(self, table, attribute, value):
		db = self.ConnectToDB()
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

	def SetAttributes(self, table, id, dict):
		sql = "UPDATE `gsdmarin`.`%s`" % table
		sql = [sql]
		sql.append("SET")
		middle = []
		for i in range(0,len(dict)):
			middle.append("`%s` = '%s'" % (dict[i].first,dict[i].second))
		sql.append(', '.join(middle))
		sql.append("WHERE ID = %s;" % id)
		
		sql = ' '.join(sql)
		print sql
		db = self.ConnectToDB()
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