# Find the greatest common divisor of n and m
def gcd(n, m): 
  # invariant : n > m 
  if m > n:
    n, m = m, n

  while m != 0: 
    n, m = m, n % m

  return n