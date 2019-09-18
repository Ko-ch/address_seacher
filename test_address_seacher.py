import unittest


class AddressSearcher:
    def search(self, postal_code):
        return "岩手県八幡平市大更"


class TestAddressSearcher(unittest.TestCase):
    def test_郵便番号を入力し岩手県八幡平市大更を取得する(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)


if __name__ == "__main__":
    unittest.main()
