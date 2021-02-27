driving = input("運転したことがありますか？（はい、いいえ）：")
if driving != "はい" and driving != "いいえ":
	print("はい/いいえ　のみ入力してください")
	raise SystemExit

age = input("年齢を入力してください：")
age = int(age)
if driving == "はい":
	if age >= 18:
		print("認証OK")
	else:
		print("なぜ運転したことあるの？")
elif driving == "いいえ":
	if age >= 18:
		print("免許取ることが可能です")
	else :
		print("あと少し免許取れますね")
else:
	print("正しい答え入力してください")