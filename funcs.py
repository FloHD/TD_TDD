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



def geo(data):
	if len(data) <= 1:
		return False
	
	else:
		flag = True
		reason = data[1] / data[0]

		for i in range(len(data)-1):
			if(data[i] != data[i+1]/reason):
				flag = False	
				break

		return flag

def ari(data):
	if len(data) <= 1:
		return False
	
	else:
		flag = True
		reason = data[1] - data[0]

		for i in range(len(data)-1):
			if(data[i] != data[i+1]-reason):
				flag = False	
				break

		return flag



def geo2(data, n):
	data_add = []

	if len(data) <= 1:
		return False
	
	else:
		flag = True
		reason = data[1] / data[0]

		for i in range(len(data)-1):
			if(data[i] != data[i+1]/reason):
				flag = False	
				break

		if flag == True:
			last = data[len(data)-1]
			for j in range(n):
				data_add.append(last*reason)
				last = data_add[len(data_add)-1]

		#print(data_add)

		return flag, data_add

def ari2(data, n):
	data_add = []

	if len(data) <= 1:
		return False
	
	else:
		flag = True
		reason = data[1] - data[0]

		for i in range(len(data)-1):
			if(data[i] != data[i+1]-reason):
				flag = False	
				break

		if flag == True:
			last = data[len(data)-1]
			for j in range(n):
				data_add.append(last+reason)
				last = data_add[len(data_add)-1]

		#print(data_add)

		return flag, data_add

	
