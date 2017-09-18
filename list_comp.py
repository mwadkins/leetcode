
ret=[]
# generate non primes
for i in range (2,8):
	for j in range (i*2,50,i):
		ret.append(j)

# anything not in non primes is a prime
for i in range (2,50):
	if i not in ret:
		print i, 

print
print "now using list comp"
# repeated using list comprehension
nonprimes=[j for i in range (2,8) for j in range(i*2,50,i)]
primes=[i for i in range (2,50) if i not in nonprimes]
print primes
