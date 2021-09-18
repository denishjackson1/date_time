import time

# can run the time without getting stuck?
while True:
    local_time = time.localtime()
    time.sleep(1)
    hr = local_time.tm_hour
    min = local_time.tm_min
    sec = local_time.tm_sec

    current_time = f"{hr}:{min}:{sec}"
    print(current_time)