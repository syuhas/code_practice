k_const = 6174

def to_int(n):
	stringls = [str(x) for x in n]
	string = "".join(stringls)
	num = int(string)
	return num
	
def asc(n):
	ls = [int(x) for x in str(n)]
	sls = [str(y) for y in ls]
	sls.sort()
	sorted = to_int(sls)
	return sorted
	
def dsc(n):
	ls = [int(x) for x in str(n)]
	sls = [str(y) for y in ls]
	sls.sort(reverse=True)
	sorted = to_int(sls)
	return sorted
	
def find_match(a):
	flag = False
	if a == k_const:
		flag = True
		return flag
	else:
		flag = False
		return flag

result = False
counter = 0

num = int(input("Enter a 4 digit number: "))

a = asc(num)
d = dsc(num)

num = d - a

print(f"{d} - {a} = {num}")

""" result = find_match(num)

while result != True:
	a = asc(num)
	d = dsc(num)
	num = d - a
	print(f"{d} - {a} = {num}")
	result = find_match(num)
	counter += 1

print (f"\nKaprekar's constant was found over {counter + 1} iterations.") """
	
