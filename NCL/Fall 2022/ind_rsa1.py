from Crypto.PublicKey import RSA

n = 591
e = 157
candidates = []
for c in range(2, n):
  if n % c == 0:
    candidates.append(c)

print(candidates)

p = candidates[0]
q = candidates[1]

phi = (p-1)*(q-1)
print(f'phi is: {phi}')
d = pow(e,-1,phi)
print(f'd is: {d}')

key = RSA.construct((n,e,d,p,q))
pem = key.exportKey('PEM')
print(pem.decode())