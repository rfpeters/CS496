import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Cat(webapp2.RequestHandler):
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
			return
		if breed:
			new_cat.breed = breed
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			return
		if age:
			new_cat.age = age
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			return
		key = new_cat.put()
		c = key.get()
		out = c.to_dict()
		self.response.write(json.dumps(out))
		return
		
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Cat, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_defs.Cat.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
			
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Cat, int(kwargs['id'])).get()
			out.key.delete()
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			return