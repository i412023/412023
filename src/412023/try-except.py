while True:
    user_input = input("請輸入正整數: ")
    try:
        number = int(user_input)
    except ValueError:
        print("輸入的數值不是正整數")
        continue
    else:
        print("程式沒有錯誤")
    finally:
        print("程式執行完畢")
