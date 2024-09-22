import datetime 

print(dir(datetime.datetime.now()))
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.now().time().second)
# print(datetime.datetime.now().strptime)

print((datetime.datetime.now() - datetime.datetime(1998 , 12 , 4)).days)
  