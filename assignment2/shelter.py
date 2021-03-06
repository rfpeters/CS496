import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs
import json

class Shelter(webapp2.RequestHandler):
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not Acceptable, API only supports application/json."
			return
		new_selter = db_models.Shelter()
		name = self.request.get('name', default_value=None)
		phone = self.request.get('phone', default_value=None)
		address = self.request.get('address', default_value=None)
		city = self.request.get('city', default_value=None)
		state = self.request.get('state', default_value=None)
		zip = self.request.get('zip', default_value=None)
		if name:
			new_selter.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
		if phone:
			new_selter.phone = phone
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, phone is required"
		if address:
			new_shelter.address = address
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, adress is required"
		if city:
			new_shelter.city = city
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, city is required"
		if state:
			new_shelter.state = state
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
		if zip:
			new_shelter.zip = zip
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, name is required"
		key = new_shelter.put()
		out = new_shelter.to_dict()
		self.response.write(json.dumps(out))
		return
	