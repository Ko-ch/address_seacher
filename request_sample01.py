import requests

response_01 = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

data_01 = response_01.json()

print(data_01["results"][0]["address1"])

response_02 = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=5670062")

data_02 = response_02.json()

print(data_02["results"][0]["address1"])
