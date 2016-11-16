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
	if num and num.isdigit():
		if int(num) in days:
			return int(num)
	return None
	

def valid_month(num):
	num = num[0].upper()+num[1:].lower()
	if num and num in months: 
		return num
	return None

	
def valid_year(num):
	if num and num.isdigit():
		num = int(num)
		if num > 1900 and num < 2020:
			return num
	return None

def b_escape_html(s):
	for (i,o) in (("&", "&amp;"), ("<","&lt;"),(">","&gt;"),('"',"&quot;")):
		s = s.replace(i,o)
	return s

import cgi
def escape_html(s):
	return cgi.escape(s, quote=True)
	
