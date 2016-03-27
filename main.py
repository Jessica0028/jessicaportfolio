import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
    	   template = JINJA_ENVIRONMENT.get_template('templates%s' % self.request.path)
    	   self.response.write(template.render())
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())
                                                 
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/interests.html', MainHandler),
    ('/photo.html', MainHandler),
    ('/contact.html', MainHandler),

], debug=True)

