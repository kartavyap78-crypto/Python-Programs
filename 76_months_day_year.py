import time 

dmy = time.localtime()

d = dmy.tm_mday
m = dmy.tm_mon
y = dmy.tm_year

print(d,":",m,":",y)