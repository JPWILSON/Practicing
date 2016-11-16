months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_day(num):
	days = [i for i in range(1,32)]
	if num.isdigit():
		num = int(num)
		if num in days:
			return num	
	else: 
		return None

def valid_month(num):
	if num:
		num = num[0].upper()+num[1:].lower()
		if num in months:
			return num
		else:
			return None

def valid_year(num):
	if num and num.isdigit():
		if int(num) > 1900 and int(num) < 2020:
			return int(num)
		else:
			return None
	return None

def b_escape_html(s):
	for (i,o) in (("&","&amp;"), (">","&gt;"),("<","&lt;"),('"',"&quot;")):
		s = s.replace(i,o)
	return s

import cgi
def escape_html(s):
	return cgi.escape(s, quote = True)
	
