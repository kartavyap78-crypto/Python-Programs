import time

# colors (ANSI codes)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

day_time = time.localtime()

h = day_time.tm_hour
m = day_time.tm_min
s = day_time.tm_sec

print(BLUE + f"⏰ Time = {h}:{m}:{s}" + RESET)

if h >= 6 and h < 12:
    print(YELLOW + "🌅 Good Morning ☀️" + RESET)
elif h >= 12 and h < 16:
    print(GREEN + "🌞 Good Afternoon 😎" + RESET)
elif h >= 16 and h < 20:
    print(BLUE + "🌇 Good Evening 🌆" + RESET)
elif h >= 20 and h < 24:
    print(RED + "🌙 Good Night 😴" + RESET)
else:
    print("❌ Invalid time")