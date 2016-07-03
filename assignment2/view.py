import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class View(base_page.BaseHandler):
	def get(self):
		customer_key = ndb.Key(urlsafe=self.request.get('key'))
		customer = customer_key.get()
		self.template_value['name'] = customer.name
		self.template_value['email'] = customer.email
		self.template_value['password'] = customer.password
		self.template_value['phone'] = customer.phone
		self.template_value['phone_type'] = customer.phone_type
		self.render('view.html', self.template_value)