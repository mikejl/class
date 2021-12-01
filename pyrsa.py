# Function to find gcd
# of two numbers
def euclid(m, n):
	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)	
	
# Program to find
# Multiplicative inverse
def exteuclid(a, b):	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a		
	return (r1, t1)

# Enter two large prime
# numbers p and q
print("RSA Key Calcualtor")
print("by Dr. Mike")
print(" *******************")
print("Steps:")
print("1. Choose two large prime numbers p and q")
print("2. Calculate n=p*q") 
print("3. Select public key e") 
print("   such that it e not a factor of (p-1)*(q-1)")
print("4. Select private key d such that the following equation:")
print("   is true (d*e)mod(p-1)(q-1)=1")
print("   or d is inverse of E in modulo (p-1)*(q-1)")
print(" *******************")
print("Enter two prime numbers for q and p")
print("Examples p = 17 and q = 11 (keep small)")
p = int(input("p: "))
q = int(input("q: "))
n = p * q
print("n= p * q is: ", n)
Pn = (p-1)*(q-1)
print("p - 1: ", p-1)
print("q - 1: ", q-1)
print("Pn is(p-1)*(q-1): ", Pn)

# Generate encryption key in range 1<e<Pn
key = []
for i in range(2, Pn):	
	gcd = euclid(Pn, i)	
	if gcd == 1:
		key.append(i)

print("Possible Public Keys")
print(key)
print("")
print("Select an encryption key 'e' from the above list")
e = int(input("e: "))

print("Obtaing inverse of encryption key in Z_Pn")
r, d = exteuclid(Pn, e)
if r == 1:
	d = int(d)	
else:
	print("Multiplicative inverse for\
	the given encryption key does not \
	exist. Choose a different encryption key ")

print("******DONE**********")
print("The encryption key is: ", e)
print("The decryption key is: ", d)
