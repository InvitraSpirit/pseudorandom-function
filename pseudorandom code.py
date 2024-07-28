x = int(input("Enter the seed: "))
z = int(input("Enter the amount of numbers: "))


def random(x, z):
  y = str(x * x)
  c = list(y)
  random_var = ""

  while z != 0:
    if z < 0:
      break
    random_var += str(c[1])
    sum = (int(c[0]) * 1000) + (int(c[1]) * 100) + (int(c[2]) * 10) + int(c[3])
    y = str(sum * sum)
    c = list(y)
    z = z - 1
  return random_var
