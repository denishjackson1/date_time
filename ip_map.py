import socket
import time
from requests import get
import folium

local_ip = socket.gethostbyname(socket.gethostname())
print('local ip:', local_ip)

start_time = time.time()
#print(start_time)

public_ip = get('https://api.ipify.org').text
print('public ip:', public_ip)

ip_data = get('http://ip-api.com/json/'+public_ip).text
print(type(ip_data), ip_data)

import json

ip_data = json.loads(ip_data)
print(type(ip_data), ip_data)

lat = ip_data['lat']
long = ip_data['lon']

base_map = folium.Map(location=[lat,long])
base_map.save('ip_map.html')

end_time = time.time()
#print(end_time)

final_time = end_time-start_time
print('time:', str(final_time)+'s')