# コマンドライン引数
import sys
args = sys.argv

# 引数が指定されているか確認
# if (len(sys.argv) <= 1):
if len(args) <= 1:
    print("引数として名前を指定してください")
else:
    # 一つ目の引数を名前として取得
    name = args[1]

    # 名前によって挨拶を変える
    if name == "Yoko":
        print(f"こんにちは{name}さん")
    else:
        print(f"はじめまして{name}さん")

# 二つ目の引数があればその値をなければ3を count とする
count = int(args[2]) if len(args) > 2 else 3


# 回数(count)だけ繰り返す
for i in range(count):
    # 偶数のときだけ表示する
    if i % 2 == 0:
        print("回数:", i)