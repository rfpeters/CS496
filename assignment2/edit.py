import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Edit(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}
		self.phone_types = []
		self.phone_types.append({'name':'home', 'checked':True})
		self.phone_types.append({'name':'work', 'checked':False})
		self.phone_types.append({'name':'cell', 'checked':False})
	
	def get(self):
		cust_key = ndb.Key(urlsafe=self.request.get('key'))
		cust = cust_key.get()
		self.template_values['key'] = self.request.get('key')
		self.template_values['cust_name'] = cust.name
		self.template_values['cust_email'] = cust.email
		self.template_values['cust_phone'] = cust.phone
		self.template_values['cust_pwd'] = cust.password		
		sports = db_defs.Sports.query(ancestor=ndb.Key(db_defs.Sports, self.app.config.get('default-group'))).fetch()
		sport_box = []
		for p in self.phone_types:
			if p['name'] == cust.phone_type:
				p['checked'] = True
		for s in sports:
			if s.key in cust.sports:
				sport_box.append({'name':s.name, 'key':s.key.urlsafe(), 'checked':True})
			else:
				sport_box.append({'name':s.name, 'key':s.key.urlsafe(), 'checked':False})
		self.template_values['sports'] = sport_box
		self.template_values['phone_type'] = self.phone_types
		self.render('edit.html', self.template_values)
		
	def post(self):
		cust_key = ndb.Key(urlsafe=self.request.get('key'))
		cust = cust_key.get()
		cust.name = self.request.get('name_input')
		cust.email = self.request.get('email_input')
		cust.password = self.request.get('password_input')
		cust.phone = self.request.get('phone_input')
		cust.phone_type = self.request.get('phone_type')
		cust.sports = [ndb.Key(urlsafe=x) for x in self.request.get_all('sports[]')]
		cust.put()
		self.render('edit.html')