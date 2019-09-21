import unittest

from address_seacher import AddressSearcher


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

    def test_存在しない郵便番号が入力されたらエラーメッセージを表示する(self):
        address_searcher = AddressSearcher()
        actual = address_searcher.search(postal_code="0000000")

        expected = "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
