import requests


class AddressSearcher:
    def search(self, postal_code):
        url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=" + postal_code
        response_dict = requests.get(url).json()
        都道府県 = response_dict["results"][0]["address1"]
        市区町村 = response_dict["results"][0]["address2"]
        町域 = response_dict["results"][0]["address3"]
        return f"{都道府県}{市区町村}{町域}"
