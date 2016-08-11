import webapp2

app = webapp2.WSGIApplication([], debug=True)
app.router.add(webapp2.Route(r'/user', 'user.User'))
app.router.add(webapp2.Route(r'/user/<id:[0-9]+>', 'user.User'))
app.router.add(webapp2.Route(r'/pokemon', 'dog.Dog'))
app.router.add(webapp2.Route(r'/pokemon/<id:[0-9]+>', 'dog.Dog'))
app.router.add(webapp2.Route(r'/login', 'login.User'))
