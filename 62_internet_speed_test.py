# 10. Internet Speed Test
# Ask the user to enter download speed (Mbps).
# Display:
# •	Below 10 → Slow
# •	10–50 → Average
# •	Above 50 → Fast

speed = int(input("enter a speed(mbps) = "))

if speed < 10:
    print("slow speed")
elif speed >=10 and speed < 50:
    print("Average speed")
else:
    print("Fast speed")