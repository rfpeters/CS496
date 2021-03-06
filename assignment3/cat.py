#Ryan Peters
#07/16/16
#Cat class for handling request for cat entities

import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Cat(webapp2.RequestHandler):
	#POST request are used for creating new entities
	#Required Parameter: name, breed, age
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		new_cat = db_defs.Cat()
		name = self.request.get('name', default_value=None)
		breed = self.request.get('breed', default_value=None)
		age = self.request.get('age', default_value=None)
		if name:
			new_cat.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			message = {}
			message['Failed'] = "Invalid request, name is required"
			self.response.write(json.dumps(message))
			return
		if breed:
			new_cat.breed = breed
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, breed is required"
			message = {}
			message['Failed'] = "Invalid request, breed is required"
			self.response.write(json.dumps(message))
			return
		if age:
			new_cat.age = age
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, age is required"
			message = {}
			message['Failed'] = "Invalid request, age is required"
			self.response.write(json.dumps(message))
			return
		key = new_cat.put()
		c = key.get()
		out = c.to_dict()
		self.response.write(json.dumps(out))
		return
		
	#GET request are used for retrieving data from database
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		#Retrieve info on one cat
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Cat, int(kwargs['id'])).get()
			if out: 
				message=out.to_dict()
				self.response.write(json.dumps(message))
			else:
				message = {}
				message['Failed'] = "Invalid request, unknown key"
				self.response.write(json.dumps(message))
		#Retrieve id of all cat entities
		else:
			q = db_defs.Cat.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
	
	#DELETE request removes a cat entity from the database
	#Required Parameters: id
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			d = ndb.Key(db_defs.Cat, int(kwargs['id'])).get()
			if d:
				d.key.delete()
			else:
				self.response.status = 400
				self.response.status_message = "Invalid request, cat unknown"
				message = {}
				message['Failed'] = "Invalid request, cat unknown"
				self.response.write(json.dumps(message))
				return
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			message = {}
			message['Failed'] = "Invalid request, id is required"
			self.response.write(json.dumps(message))
			return
	
	#PUT request creates an association between a cat and shelter
	#Required Parameter: Cat id in URL, Shelter id in Body
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			c = ndb.Key(db_defs.Cat, int(kwargs['id'])).get()
			if not c:
				self.response.status = 404
				self.response.status_message = "Cat not found"
				message = {}
				message['Failed'] = "Invalid request, unknown cat"
				self.response.write(json.dumps(message))
				return		
		s = ndb.Key(db_defs.Shelter, int(self.request.get('sid')))
		shelter = s.get()
		if shelter:
			c.shelter = s
			c.put()
			self.response.write(json.dumps(c.to_dict()))
			return
		else:
			self.response.status = 404
			self.response.status_message = "Shelter not found"
			message = {}
			message['Failed'] = "Invalid request, unknown shelter"
			self.response.write(json.dumps(message))
			return