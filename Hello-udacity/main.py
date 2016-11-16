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
from date_calcs import * 

form = """
	<form method="post">
		<h2>Enter Dates</h2>
		<label>
			Day: 
			<input type="text" name = "day" value = "%(day)s">
		</label>
		<label>
			Month: 
			<input type="text" name = "month" value = "%(month)s">
		</label>
		<label>
			Year: 
			<input type="text" name = "year" value = "%(year)s">
		</label><br>
		<div style="color:red">%(error)s</div>
		<input type = "submit" value="Go!">
	</form>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, error="", day = "", month= "", year=""):
		self.response.out.write(form % {"error": error, "day": day, "month": month, "year": year})

	def get(self):
		self.write_form()

	def post(self):
		user_day = self.request.get('day')
		user_month = self.request.get('month')
		user_year = self.request.get('year')

		day = valid_day(user_day)
		month = valid_month(user_month)
		year = valid_year(user_year)

		if not (day and month and year):
			self.write_form("Try again, entries aren't valid", user_day, user_month, user_year)
		else:
			self.redirect('/thanks')

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Well done, it has been submitted")

app = webapp2.WSGIApplication([('/', MainHandler),
								('/thanks', ThanksHandler)], debug = True)

