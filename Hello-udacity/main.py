#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os 
import webapp2
import jinja2

from google.appengine.ext import db 

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape= True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(**params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def render_front(self, title="", content="", error=""):
		self.render("misc.html",title = title, content = content, error = error)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		content = self.request.get("content")
		
		if title != "" and content != "":
			self.redirect("/success")
		else:
			error = "There is an error in your submission"
			self.render_front(title, content, error)


class SuccessHandler(Handler):
	def get(self):
		self.response.out.write("Thanks for submitting, 12:43 midday :)")

app = webapp2.WSGIApplication([('/', MainPage), ("/success", SuccessHandler)], debug = True)

'''
import os
import webapp2
import jinja2

from google.appengine.ext import db 

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(**params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def render_front(self, title="", art="", error=""):
		self.render("misc.html", title = title, art = art, error = error)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")

		if title and art:
			self.write("Thanks")
		else:
			error = "Submission incomplete"
			self.render_front(title, art, error)


app = webapp2.WSGIApplication([('/', MainPage)], debug = True)

'''