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
from date_calcs import *
import webapp2

form = """
<form method = "post">
			<h2>What is your birthday</h2>
			<label>
				Day: 
				<input name="day" value = "%(day)s">
			</label>
			<label>
				Month: 
				<input name ="month" value = "%(month)s">
			</label>
			<label>
				Year: 
				<input name ="year" value = "%(year)s">
			</label><br>
			<div style= "color: red">%(error)s</div><br>
			<input type = "submit">
		</form>
"""

class MainPage(webapp2.RequestHandler):
	#Since w're going to be printing the form in a couple of places, generalize into a fn:
	def write_form(self, error="", day = "", month="", year= ""):
		self.response.out.write(form % {"error": error,
										"day": escape_html(day),
										"month": escape_html(month),
										"year": escape_html(year)})

	def get(self):
		#Now, because of above fn, can just use it here:
		#self.response.out.write(form)
		self.write_form()

	def post(self):
		user_day = self.request.get('day')
		user_month = self.request.get('month')
		user_year = self.request.get('year')

		day = valid_day(user_day)
		month = valid_month(user_month)
		year = valid_year(user_year)

		if not (day and month and year):
			self.write_form("Sorry bud, something you entered wasn't valid...", 
				user_day, user_month, user_year)
		else:
			self.redirect("/thanks")
			

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks for submitting a valid date my boet!")


#This is the url mapping section, and it maps to Mainpage
app = webapp2.WSGIApplication([('/', MainPage),
								('/thanks', ThanksHandler)], debug = True)

