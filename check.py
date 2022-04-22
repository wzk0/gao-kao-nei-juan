import time
import random
import os

积分=".data/money.txt"
今天=".data/today.txt"
with open(积分, 'r') as f:
	原积分=f.read()
with open(今天, 'r') as f:
	日期=str(f.read())
money=random.randint(0,50)
today=time.strftime("%Y-%m-%d", time.localtime())

def jifen():
	现积分=int(原积分)+money
	os.system("rm -rf .data/money.txt && touch .data/money.txt")
	with open(积分, 'w') as f:
		f.write(str(现积分))
def check():
	if 日期==str(today):
		print("今天已经签到啦，积分不会增加！")
		with open(".data/money.txt", 'r') as f:
			现积分=int(f.read())
		print("现有积分:"+str(现积分))
	else:
		jifen()
		print("今日签到成功！积分增加:"+str(money))
		with open(".data/money.txt", 'r') as f:
			现积分=int(f.read())
		print("现有积分:"+str(现积分)+"\n")
		os.system("rm -rf .data/today.txt && touch .data/today.txt")
		with open(".data/today.txt", 'w') as f:
			f.write(today)

def pure():
	奖励积分=random.randint(0,25)
	print("奖励！积分增加:"+str(奖励积分))
	with open(".data/money.txt", 'r') as f:
		原积分=int(f.read())
	现积分=原积分+奖励积分
	os.system("rm -rf .data/money.txt && touch .data/money.txt")
	with open(积分, 'w') as f:
		f.write(str(现积分))
	print("现有积分:"+str(现积分))

def all():
	with open(".data/all.txt",'r') as f:
		all=int(f.read())
	nowall=all+1
	os.system("rm -rf .data/all.txt && touch .data/all.txt")
	with open(".data/all.txt",'w') as f:
		f.write(str(nowall))

def right():
	with open(".data/right.txt",'r') as f:
		right=int(f.read())
	nowright=right+1
	os.system("rm -rf .data/right.txt && touch .data/right.txt")
	with open(".data/right.txt",'w') as f:
		f.write(str(nowright))

def wrong():
	with open(".data/wrong.txt",'r') as f:
		wrong=int(f.read())
	nowwrong=wrong+1
	os.system("rm -rf .data/wrong.txt && touch .data/wrong.txt")
	with open(".data/wrong.txt",'w') as f:
		f.write(str(nowwrong))
