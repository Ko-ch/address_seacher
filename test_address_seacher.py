import unittest

import requests


class AddressSearcher:
    def search(self, postal_code):
        url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=" + postal_code
        response_dict = requests.get(url)
        都道府県 = response_dict.json()["results"][0]["address1"]
        市区町村 = response_dict.json()["results"][0]["address2"]
        町域 = response_dict.json()["results"][0]["address3"]
        return f"{都道府県}{市区町村}{町域}"


class TestAddressSearcher(unittest.TestCase):
    def test_郵便番号を入力し岩手県八幡平市大更を取得する(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)

    def test_郵便番号を入力し東京都練馬区豊玉南を取得する(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="1760014")

        self.assertEqual("東京都練馬区豊玉南", actual)

    def test_郵便番号を入力し大阪府茨木市東福井を取得する(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="5670062")

        self.assertEqual("大阪府茨木市東福井", actual)


if __name__ == "__main__":
    unittest.main()
