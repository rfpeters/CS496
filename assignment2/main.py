import webapp2

config = {'default-group':'base-data'}

application = webapp2.WSGIApplication([
	('/', 'index.Index')
], debug=True, config=config)