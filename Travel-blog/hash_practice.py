import hashlib

def using_md5(word2hash):
	x = hashlib.md5(word2hash).hexdigest()
	return x

