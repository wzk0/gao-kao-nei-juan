import time
import random
import os

积分=".temp/money.txt"
今天=".temp/today.txt"
with open(积分, 'r') as f:
	原积分=f.read()
with open(今天, 'r') as f:
	日期=str(f.read())
money=random.randint(0,50)
today=time.strftime("%Y-%m-%d", time.localtime())

def jifen():
	现积分=int(原积分)+money
	os.system("rm -rf .temp/money.txt && touch .temp/money.txt")
	with open(积分, 'w') as f:
		f.write(str(现积分))
def check():
	if 日期==str(today):
		print("今天已经签到啦，积分不会增加！")
		with open(".temp/money.txt", 'r') as f:
			现积分=int(f.read())
		print("现有积分:"+str(现积分))
	else:
		jifen()
		print("今日签到成功！积分增加:"+str(money))
		with open(".temp/money.txt", 'r') as f:
			现积分=int(f.read())
		print("现有积分:"+str(现积分)+"\n")
		os.system("rm -rf .temp/today.txt && touch .temp/today.txt")
		with open(".temp/today.txt", 'w') as f:
			f.write(today)

def pure():
	奖励积分=random.randint(0,25)
	print("奖励！积分增加:"+str(奖励积分))
	with open(".temp/money.txt", 'r') as f:
		原积分=int(f.read())
	现积分=原积分+奖励积分
	os.system("rm -rf .temp/money.txt && touch .temp/money.txt")
	with open(积分, 'w') as f:
		f.write(str(现积分))
	print("现有积分:"+str(现积分))
