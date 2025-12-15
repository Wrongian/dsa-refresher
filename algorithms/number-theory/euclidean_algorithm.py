# Find the greatest common divisor of n and m
def gcd(n, m): 
  # invariant : n > m 
  if m > n:
    n, m = m, n

  if m == 0: 
    return n

  return gcd(m, n % m)