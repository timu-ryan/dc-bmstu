# s = str(input())
# a = s.split()
# k = str(input())
# for item in a:
#     if k in item or k in item.lower():
#         print(item)

some_str = input()
sub_str = input()

arr = some_str.split()

for string in arr:
  print(f'string: {string}')
  print(sub_str.lower())
  if string.lower().find(sub_str.lower()) != -1:
    print(string)