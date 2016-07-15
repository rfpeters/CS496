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
			return
		if breed:
			new_dog.breed = breed
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			return
		if age:
			new_dog.age = age
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			return
		key = new_dog.put()
		#out = new_dog.to_dict()
		#self.response.write(json.dumps(out))
		return