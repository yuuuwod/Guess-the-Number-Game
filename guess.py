import random

def select_difficulty():
    print("--- 難易度を選んでください ---")
    print("1: 易しい:1~10")
    print("2: 普通:1~100")
    print("3: 難しい:1~1000")
    while True:
        choice = input("番号を入力してください (1 or 2 or 3): ")

        if choice == "1":
            print("易しいモードを選択しました。")
            return "easy"
        elif choice == "2":
            print("普通モードを選択しました。")
            return "normal"
        elif choice == "3":
            print("難しいモードを選択しました。")
            return "hard"
        else:
            print("1 or 2 or 3 を入力してください。")

difficulty = select_difficulty()
if difficulty == "easy":
    randomint = random.randint(1, 10)
elif difficulty == "normal":
    randomint = random.randint(1, 100)
elif difficulty == "hard":
    randomint = random.randint(1, 1000)
count = 0

while count < 10:
    try:
        absint = int(input("入力してください: "))
    except ValueError:
        print("数字を入力してください")
        continue

    count += 1

    if absint == randomint:
        print(f"正解！{count}回で当てました")
        break

    if absint < randomint:
        print("もっと大きい数字です")
    else:
        print("もっと小さい数字です")

    if count == 10:
        print(f"{count}回失敗したのでゲームオーバー")

with open("result.txt", "a", encoding="utf-8") as f:
    f.write(str(count))
