def repeatedString(string,n):
  count =0
  for i in string:
    if i =="a":
      count += 1
  if (n%len(string))==0 :
    count = count * (n//len(string))
  else:
    count= count *(n//len(string))
    x= n%len(string)
    for i in string[:x]:
      if i=="a":
        count +=1
  return  count

string = input()
n= int(input())
print(repeatedString(string,n))