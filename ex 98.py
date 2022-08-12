# Write a Python program to get the system time.
from datetime import datetime
time = datetime.now().strftime("%H:%M:%S")
print(time)