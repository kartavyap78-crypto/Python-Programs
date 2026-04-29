import time

day_time = time.localtime()
h = day_time.tm_hour
m = day_time.tm_min
s = day_time.tm_sec
print(h,":",m,":",s)

if h >= 6 and h < 12:
    print("Good morning")
elif h >= 12 and h < 16:
    print("Good afternoon")
elif h >= 16 and h < 20:
    print("Good evening")
elif h >= 20 and h < 24:
    print("Good night")
else:
    print("invalid")
 