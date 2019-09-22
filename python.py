import time
time = time.localtime()
print(time)
print(f"today is {time.tm_mon}/{time.tm_mday}/{time.tm_year}")
print(f"the time is {time.tm_hour}:{time.tm_min}:{time.tm_sec}")