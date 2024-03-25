result = 0
a = input()

while a != '':
  if int(a) % 2 == 0:
    result += int(a)
  a = input()

print(result)
