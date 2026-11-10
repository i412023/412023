import random

def generate_password() -> int:
    return random.randint(1, 100)

def check_password(user_input: int, password: int) -> bool:
    return user_input == password

def main() -> None:
    password = generate_password()
    min_value = 1
    max_value = 100
    while True:
        try:
            user_input = int(input(f"輸入你猜的數字（介於 {min_value} 到 {max_value} 之間）: "))
            if user_input < min_value or user_input > max_value:
                raise ValueError("輸入的數字不在指定範圍內。")
            if check_password(user_input, password):
                print("密碼正確")
                break
            else:
                print("密碼錯誤")
                if user_input < password:
                    print("提示: 大一點。")
                    min_value = user_input + 1
                else:
                    print("提示: 小一點。")
                    max_value = user_input - 1
        except ValueError:
            print(f"請輸入一個 {min_value}~{max_value} 之間的整數。")
        except KeyboardInterrupt:
            print("\n遊戲手動中止。")
            break
        except Exception as e:
            print(f"嚴重錯誤發生: {e}")


if __name__ == "__main__":
    main()