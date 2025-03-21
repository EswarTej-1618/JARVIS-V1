import requests

def find_myip():
    # ip_add=requests.get("http://ip-api.com/json/{query}?fields=status,continent,country,regionName,city,district,lat,lon").json()
    ip_add=requests.get("http://ip-api.com/json/?fields=status,continent,country,regionName,city,district,lat,lon,query").json()
    # .json() give us the date in somewhat dictionary format
    # query-ipaddress manully filled
    return ip_add

# ip=o.find_myip()["ip"]
details=find_myip()
ip=details['query']
print(f"your ip is {ip}") 
location=details['country']+" "+details['regionName']
print(f"your location is {location}")

