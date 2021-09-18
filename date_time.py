import time #Unix time

# time in seconds since Jan 1, 1970
start_time = time.time()
print(start_time)

for i in range(100):
    i += 1

end_time = time.time()-start_time
print(end_time)

local_time = time.localtime()
print(local_time)

month = local_time.tm_mon
day = local_time.tm_mday
year = local_time.tm_year
zone = local_time.tm_zone


hr = local_time.tm_hour
min = local_time.tm_min
sec = local_time.tm_sec

current_time = f"{hr}:{min}:{sec}"
print(current_time)

print(f"{month}/{day}/{year}")


