#  Write a Python program to convert seconds to day, hour, minutes and seconds.
import datetime, time

sec = int(input("Insert seconds: "))

result = datetime.timedelta(seconds= sec)
print(result)