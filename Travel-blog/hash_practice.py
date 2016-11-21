import hashlib

def using_md5(word2hash):
	x = hashlib.md5(word2hash).hexdigest()
	return x

def using_sha2(word):
	y = hashlib.sha256(word).hexdigest()
	return y


print using_sha2("udacity")
