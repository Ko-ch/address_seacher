from address_seacher import AddressSearcher


def main():
    # ユーザーからの郵便番号を受け取る
    zipcode = int(input("郵便番号を数字7桁を入力してね："))
    # 郵便番号を使って地名をとってくる
    address = AddressSearcher().search(zipcode)
    # 地名をprintする
    print(f"指定の住所は：{address}")


if __name__ == "__main__":
    main()
