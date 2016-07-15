import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Shelter(webapp2.RequestHandler):
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		new_shelter = db_defs.Shelter()
		name = self.request.get('name', default_value=None)
		phone = self.request.get('phone', default_value=None)
		address = self.request.get('address', default_value=None)
		city = self.request.get('city', default_value=None)
		state = self.request.get('state', default_value=None)
		zip = self.request.get('zip', default_value=None)
		if name:
			new_shelter.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			message = {}
			message['Failed'] = "Invalid request, name is required"
			self.response.write(json.dumps(message))
			return
		if phone:
			new_shelter.phone = phone
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, phone is required"
			message = {}
			message['Failed'] = "Invalid request, phone is required"
			self.response.write(json.dumps(message))
			return
		if address:
			new_shelter.address = address
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, address is required"
			message = {}
			message['Failed'] = "Invalid request, address is required"
			self.response.write(json.dumps(message))
			return
		if city:
			new_shelter.city = city
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, city is required"
			message = {}
			message['Failed'] = "Invalid request, city is required"
			self.response.write(json.dumps(message))
			return
		if state:
			new_shelter.state = state
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, state is required"
			message = {}
			message['Failed'] = "Invalid request, state is required"
			self.response.write(json.dumps(message))
			return
		if zip:
			new_shelter.zip = zip
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, zip is required"
			message = {}
			message['Failed'] = "Invalid request, zip is required"
			self.response.write(json.dumps(message))
			return
		key = new_shelter.put()
		out = new_shelter.to_dict()
		self.response.write(json.dumps(out))
		return
	
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Shelter, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_defs.Shelter.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
			
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Shelter, int(kwargs['id'])).get()
			out.key.delete()
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			return