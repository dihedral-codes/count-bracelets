import math

def phi(n):
  amount = 0
  for k in range(1, n + 1):
    if math.gcd(n, k) == 1:
      amount += 1
  return amount

def nek(n, k):
  no = 0
  for d in range(1, n + 1):
    if n % d == 0:
      no += (phi(d) * k**(n / d))
  return (no / n)

def brc(n, k):
  nonek = nek(n, k)
  if (n % 2 == 0):
    return ((nonek / 2) + ((k**(n/2)) * (k + 1) / 4))
  else:
    return ((nonek / 2) + ((k**((n + 1) / 2)) / 2))

