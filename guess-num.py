import random
r = random.randint(1, 100) #產生一個隨機整數1~100(不要印出)
while True:
	num = input('請猜一個1~100之間的數字:') #讓使用者重複輸入數字去猜
	num = int(num)
	if num == r:
		print('恭喜猜對了!') #猜對的話就說猜對了
		break
	else: #猜錯的話 要告訴他比答案大或小
		if num > r:
			print('答錯囉!數字要再小一些!')
		else:
			print('答錯囉!數字要再大一些!')
