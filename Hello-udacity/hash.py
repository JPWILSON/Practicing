import hashlib

def md5(x):
	ans = hashlib.md5(x)
	print ans
	print ans.hexdigest()

def shaaar(y):
	ans = hashlib.sha256(y)
	print ans
	print ans.hexdigest()

shaaar("udacity")