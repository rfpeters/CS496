#Ryan Peters

import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Pokemon(webapp2.RequestHandler):
	#POST request are used for creating new entities
	#Required Parameter: name, breed, age
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		new_pokemon = db_defs.Pokemon()
		name = self.request.get('name', default_value=None)
		lat = self.request.get('lat', default_value=None)
		long = self.request.get('long', default_value=None)
		user = self.request.get('user', default_value=None)
		if name:
			new_pokemon.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			message = {}
			message['Failed'] = "Invalid request, name is required"
			self.response.write(json.dumps(message))
			return
		if lat:
			new_pokemon.lat = lat
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, lat is required"
			message = {}
			message['Failed'] = "Invalid request, lat is required"
			self.response.write(json.dumps(message))
			return
		if long:
			new_pokemon.long = long
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, long is required"
			message = {}
			message['Failed'] = "Invalid request, long is required"
			self.response.write(json.dumps(message))
			return
		if user:
			new_pokemon.user = ndb.Key(db_defs.User, int(user))
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, long is required"
			message = {}
			message['Failed'] = "Invalid request, long is required"
			self.response.write(json.dumps(message))
			return
		key = new_pokemon.put()
		d = key.get()
		out = d.to_dict()
		self.response.write(json.dumps(out))
		return
	
	#GET request are used for retrieving data from database	
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		#Retrieve info on one dog
		if 'id' in kwargs:
			user = ndb.Key(db_defs.User, int(kwargs['id']))
			query = db_defs.Pokemon.query(db_defs.Pokemon.user == user)
			if query:
				message = {}
				pokemon = []
				for p in query:
					pokemon.append(p.to_dict())
				message['pokemon'] = pokemon
				self.response.write(json.dumps(message))
			else:
				message = {}
				message['Failed'] = "Invalid request, unknown user"
				self.response.write(json.dumps(message))
		#Retrieve id of all cat entities
		else:
			q = db_defs.Pokemon.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
		
	#DELETE request removes a dog entity from the database
	#Required Parameters: id
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			d = ndb.Key(db_defs.Pokemon, int(kwargs['id'])).get()
			if d:
				d.key.delete()
			else:
				self.response.status = 400
				self.response.status_message = "Invalid request, pokemon unknown"
				message = {}
				message['Failed'] = "Invalid request, pokemon unknown"
				self.response.write(json.dumps(message))
				return
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			message = {}
			message['Failed'] = "Invalid request, id is required"
			self.response.write(json.dumps(message))
			return
	
	#PUT request creates an association between a dog and shelter
	#Required Parameter: Dog id in URL, Shelter id in Body
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			p = ndb.Key(db_defs.Pokemon, int(kwargs['id'])).get()
			if not p:
				self.response.status = 404
				self.response.status_message = "Dog not found"
				message = {}
				message['Failed'] = "Invalid request, unknown dog"
				self.response.write(json.dumps(message))
				return		
			p.name = self.request.get('name')
			p.put()
			self.response.write(json.dumps(p.to_dict()))
			return
		#else:
		#	self.response.status = 404
		#	self.response.status_message = "Shelter not found"
		#	message = {}
		#	message['Failed'] = "Invalid request, unknown shelter"
		#	self.response.write(json.dumps(message))
		#	return