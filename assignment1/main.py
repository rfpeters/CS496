import webapp2
import datetime

now = datetime.datetime.now()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(str(now))
		
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)