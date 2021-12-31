def min_int(a, b):
	if a < b :
		return a
	else :
		return b

def mean(data):
	if len(data) == 0:
		return None

	else:
		mean = sum(data)/len(data)
		return mean


def median(data):
	data = sorted(data)
	l = len(data)
	
	if l == 0:
		return None

	if l % 2 == 0:
		return (data[(l-1)/2] + data[(l+1)/2])/2.0

	else:
		return data[(l-1)/2]

def st_dev(data):
	if len(data) == 0:
		return None

	else:
		mean = sum(data)/len(data)
		var = sum((l-mean)**2 for l in data) / len(data)
		st_dev = var**0.5
		return st_dev
