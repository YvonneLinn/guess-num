import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end) #產生一個隨機整數1~100(不要印出)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜一個數字:') #讓使用者重複輸入數字去猜
	num = int(num)
	if num == r:
		print('恭喜猜對了!') #猜對的話就說猜對了
		print('這是你猜的第', count, '次')
		break
	else: #猜錯的話 要告訴他比答案大或小
		if num > r:
			print('答錯囉!數字要再小一些!')
		else:
			print('答錯囉!數字要再大一些!')
	print('這是你猜的第', count, '次')
