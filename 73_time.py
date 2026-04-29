import time

current_time = time.localtime()

h = current_time.tm_hour
m = current_time.tm_min
s = current_time.tm_sec

print(h,":",m,":",s)