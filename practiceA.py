# コマンドライン引数
import sys
args = sys.argv

# if (len(sys.argv) <= 1):
if len(args) <= 1:
    print("引数として名前を指定してください")
else:
    name = args[1]
    if name == "Yoko":
        print(f"こんにちは{name}さん")
    else:
        print(f"はじめまして{name}さん")