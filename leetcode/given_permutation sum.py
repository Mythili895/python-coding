##Given three integers x,y and z you need to find the
##sum of all the numbers formed by having 4 atmost x
##times , having 5 atmost y times and having 6 atmost
##z times as a digit.

def sumcalc(x,y,z):
  if x < 0 or y < 0 or z < 0: return -1
  import itertools
  sum = 0
  for i, j, k in itertools.product(range(x + 1), range(y + 1), range(z + 1)):
    e = (('4' * i) + ('5' * j) + ('6' * k))
    if e:
      perms = [''.join(p) for p in itertools.permutations(e)]  
      for i in set(perms): sum += int(i)
  return sum
