import time

def return_date():
    time_now = time.localtime()
    print(f"today is {time_now.tm_mon}/{time_now.tm_mday}/{time_now.tm_year}")

def return_time():
    time_now = time.localtime()
    print(f"the time is {time_now.tm_hour}:{time_now.tm_min}:{time_now.tm_sec}")

return_date()
return_time()