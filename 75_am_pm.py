import time

t = time.localtime()

h = t.tm_hour
m = t.tm_min
s = t.tm_sec

if h > 12:
    am_pm = "PM"
else:
    am_pm = "AM"

if h > 12:
    h = h - 12
elif h == 0:
    h = 12


print(h,":",m,":",s,am_pm)