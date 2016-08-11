#Ryan Peters

import webapp2
from google.appengine.ext import ndb
import db_defs
import json

class Login(webapp2.RequestHandler):
	def post(self):
		query = db_defs.User.query(db_defs.User.email == self.request.get('email', default_value=None))
		password = self.request.get('password', default_value=None)
		if password:
			for q in query:
				if q.password == password:
					out = q.to_dict()
					self.response.write(json.dumps(out))
					return
			message = {}
				message['Failed'] = "Email and password did not match"
				self.response.write(json.dumps(message))