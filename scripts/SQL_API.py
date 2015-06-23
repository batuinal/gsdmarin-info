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

class call_method(webapp2.RequestHandler):
  def post(self):
    #try:
      func = self.request.get('func')
      name = self.request.get('name')
      attribute = self.request.get('attribute')
      id = self.request.get('id')
      entity = self.request.get('entity')

      # AYHUN: Senin inputlarindan bir tek burada dict yok, onun icin farkli bir debugging dusuneblirsn.
      #       Input variable adlari yukarida tanimli, kulanman icin..

      self.response.out.write('Method to Call: %s <br>' % (func))
      self.response.out.write('Name of Table:  %s <br>' % (name))
      self.response.out.write('Attribute:      %s <br>' % (attribute))
      self.response.out.write('ID:             %s <br>' % (id))
      self.response.out.write('Entity:         %s <br>' % (entity))
	  
      sqlimpl = sqllib();
	  
      logging.info("Calling appropriate function..."); 
	  
	  ### Table Functions ###
      if func == "CreateTable":
        sqlimpl.CreateTable(name)
      elif func == "RemoveTable":
        sqlimpl.RemoveTable(name)
      elif func == "PrintTable":
        sqlimpl.PrintTable(name)
      ### Entity Functions ###
      elif func == "RemoveEntity":
        sqlimpl.RemoveEntity(name, id)
      elif func == "AddEntity":
        sqlimpl.AddEntity(name)
      elif func == "ListEntities":
        sqlimpl.ListEntities(name)
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
        sqlimpl.AddEntityWithValues(name, dict)
      ### Attribute Functions ###
      elif func == "AddAttribute":
        sqlimpl.AddAttribute(name, attribute, 'VARCHAR(100)')
      elif func == "RemoveAttribute":
        sqlimpl.RemoveAttribute(name, attribute)
      elif func == "ListAttributes":
        sqlimpl.ListAttributes(name)
      ### Value Functions ###
      
      ### Else Statement ###
      else:
        self.response.out.write('-- Could not find ' + func + '\n')         
    #except:
      #logging.error('Error in getting/running correct func')
      #self.response.out.write('-- Error: Exception thrown while executing function.')