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
from sqllib import sqllib

# This Python file uses Spaces for Alignment

class call_method(webapp2.RequestHandler):
  def post(self):
    #try:
      func = self.request.get('func')
      page = self.request.get('page')
      name = self.request.get('name')
      attribute = self.request.get('attribute')
      id = self.request.get('id')
      value = self.request.get('value')

      self.response.out.write('Method to Call: %s <br>' % (func))
      self.response.out.write('Name of Table:  %s <br>' % (name))
      self.response.out.write('Page Name:      %s <br>' % (page))
      self.response.out.write('Attribute:      %s <br>' % (attribute))
      self.response.out.write('ID:             %s <br>' % (id))
      self.response.out.write('Value:          %s <br>' % (value))
      
      sqlimpl = sqllib();
      out = "-- Output: "
      
	  ### Table Functions ###
      if func == "CreateTable":
        out += str(sqlimpl.CreateTable(name, page))
      elif func == "RemoveTable":
        out += str(sqlimpl.RemoveTable(name, page))
      elif func == "PrintTable":
        out += str(sqlimpl.PrintTable(name))
      ### Entity Functions ###
      elif func == "RemoveEntity":
        out += str(sqlimpl.RemoveEntity(name, id))
      elif func == "AddEntity":
        out += str(sqlimpl.AddEntity(name))
      elif func == "ListAllEntities":
        out += str(sqlimpl.ListAllEntities(name))
      elif func == 'AddEntityWithValues':
        self.response.out.write('Dictionary for AddEntityWithValues is given by hand')
        dict = []
        dict.append(['SHIP'])
        dict[0].append('ship1')
        dict[0].append('ship2')
        dict.append(['DATE'])
        dict[1].append('1991-12-21')
        dict[1].append('1010-10-10')
        dict.append(['REPORT'])
        dict[2].append('report1')
        dict[2].append('report2')
        out += str(sqlimpl.AddEntityWithValues(name, dict))
      ### Attribute Functions ###
      elif func == "AddAttribute":
        out += str(sqlimpl.AddAttribute(name, page, attribute, 'VARCHAR(100)', 'red_hooded_motherfucker'))
      elif func == "RemoveAttribute":
        out += str(sqlimpl.RemoveAttribute(name, page, attribute))
      ### Value Functions ###
      elif func == "SetValue":
        out += str(sqlimpl.SetValue(name, id, attribute, value))
      elif func == "GetValue":
        out += str(sqlimpl.GetValue(name, id, attribute))
      elif func == "SetAllEntities":
        out += str(sqlimpl.SetAllEntities(name, attribute, value))
      elif func == "SetAttributes":
        dict = []
        dict.append(['pay'])
        dict[0].append('11')
        dict.append(['day'])
        dict[1].append('21')
        out += str(sqlimpl.SetAllAttributes(name, id, dict))
      elif func == "GetEntityByID":
        sqlimpl.GetEntityByID(name, attribute, id)
      elif func == "GetEntitiesByAttr":
        sqlimpl.GetEntitiesByAttr(name, attribute, value)
      else:
        out = "-- Error: Method " + func + " not found." + "\n"        
      self.response.out.write(out)
    #except:
      #logging.error('-- Error: Exception thrown during execution.')
      #self.response.out.write('-- Error: Exception thrown during execution.')
 