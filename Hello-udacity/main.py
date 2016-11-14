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
import webapp2

form = """
<form action="/testform">
			<input name="q">
			<input type = "submit">
		</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-type'] = 'text/html' #the default is text/html i think? change from text/plain
		self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.out.write(q)
		
		#The following is how to view the http request:
		#self.response.headers['Content-type'] = 'text/plain'
		#self.response.out.write(self.request)

#This is the url mapping section, and it maps to Mainpage
app = webapp2.WSGIApplication([('/', MainPage),
								('/testform', TestHandler)], debug = True)
