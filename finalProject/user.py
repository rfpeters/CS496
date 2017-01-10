#Ryan Peters

import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class User(webapp2.RequestHandler):
	#POST request are used for creating new entities
	#Required Parameter: name, email, password
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		
		new_user = db_defs.User()
		name = self.request.get('name', default_value=None)
		email = self.request.get('email', default_value=None)
		password = self.request.get('password', default_value=None)
		if name:
			new_user.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
			message = {}
			message['Failed'] = "Invalid request, name is required"
			self.response.write(json.dumps(message))
			return
		if email:
			new_user.email = email
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, email is required"
			message = {}
			message['Failed'] = "Invalid request, email is required"
			self.response.write(json.dumps(message))
			return
		if password:
			new_user.password = password
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, password is required"
			message = {}
			message['Failed'] = "Invalid request, password is required"
			self.response.write(json.dumps(message))
			return
		key = new_user.put()
		out = new_user.to_dict()
		self.response.write(json.dumps(out))
		return
	
	#GET request are used for retrieving data from database
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		#Retrieve info on one user
		if 'id' in kwargs:
			out = ndb.Key(db_defs.User, int(kwargs['id'])).get()
			if out:
				message=out.to_dict()				
				self.response.write(json.dumps(message))
			else:
				message = {}
				message['Failed'] = "Invalid request, unknown key"
				self.response.write(json.dumps(message))
		#Retrieve id of all user entities
		else:
			q = db_defs.User.query()
			keys = q.fetch(keys_only=True)
			results = {'keys':[x.id() for x in keys]}
			self.response.write(json.dumps(results))
	
	#DELETE request removes a user entity from the database
	#Required Parameters: id
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		if 'id' in kwargs:
			s = ndb.Key(db_defs.User, int(kwargs['id'])).get()
			if s:
				s.key.delete()
				d = db_defs.Pokemon.query(db_defs.Pokemon.shelter == s.key).fetch(keys_only=True)
				if d:
					ndb.delete_multi(d)
				return
			else:
				self.response.status = 400
				self.response.status_message = "Invalid request, user unknown"
				message = {}
				message['Failed'] = "Invalid request, user unknown"
				self.response.write(json.dumps(message))
				return
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, id is required"
			message = {}
			message['Failed'] = "Invalid request, id is required"
			self.response.write(json.dumps(message))
			return			