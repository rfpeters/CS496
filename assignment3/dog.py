import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Dog(webapp2.RequestHandler):
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		new_dog = db_defs.Dog()
		name = self.request.get('name', default_value=None)
		breed = self.request.get('breed', default_value=None)
		age = self.request.get('age', default_value=None)
		if name:
			new_dog.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			message = {}
			message['Failed'] = "Invalid request, name is required"
			self.response.write(json.dumps(message))
			return
		if breed:
			new_dog.breed = breed
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, breed is required"
			message = {}
			message['Failed'] = "Invalid request, breed is required"
			self.response.write(json.dumps(message))
			return
		if age:
			new_dog.age = age
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, age is required"
			message = {}
			message['Failed'] = "Invalid request, age is required"
			self.response.write(json.dumps(message))
			return
		key = new_dog.put()
		d = key.get()
		out = d.to_dict()
		self.response.write(json.dumps(out))
		return
		
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Dog, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_defs.Dog.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
			
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			d = ndb.Key(db_defs.Dog, int(kwargs['id'])).get()
			d.key.delete()
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			message = {}
			message['Failed'] = "Invalid request, id is required"
			self.response.write(json.dumps(message))
			return
	
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			d = ndb.Key(db_defs.Dog, int(kwargs['id'])).get()
			if not d:
				self.response.status = 404
				self.response.status_message = "Dog not found"
				return
		if 'sid' in kwargs:
			s = ndb.Key(db_defs.Shelter, int(kwargs['sid']))
			if not s:
				self.response.status = 404
				self.response.status_message = "Shelter not found"
				return
		d.shelter = s
		d.put()
		self.response.write(json.dumps(d.to_dict()))
		return