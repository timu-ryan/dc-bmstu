some_str = input()

if some_str[0] == ' ':
  some_str = some_str[1:]

if some_str[-1] == ' ':
  some_str = some_str[:-1]

while('  ' in some_str):
  some_str = some_str.replace('  ', ' ')

print(some_str.replace(' ', '*'))
