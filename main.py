##导入模块
import sys	##退出程序
import os	##系统指令
import time	##显示时间
import do	##题目处理
import platform	##系统检测
import rf	##读取配置
import random	##随机抽取
import requests	##获取数据

def 做题():
	act="wget "+rf.repo+str(number)+".yaml"
	os.system(act)
	do.练习(number)
	again=input("是/否(y/n)继续:")
	if again=="y":
		做题()
	else:
		pass

os.system('clear')	##清屏
print('--- Terminals Exercises (高中) ---\n')

print("正在检查配置...")
##检查config是否配置好
if rf.ok!=1:
	print('请打开config.yaml进行配置后再运行脚本！')
	sys.exit(0)
else:
	print("\033[32m√\033[0m\n")

##检查系统
print("正在检查系统...")
if platform.system() == 'Windows':
	print("系统为:" + platform.system() + "，不太适合学习！")
else:
	print("系统为:" + platform.system() + "，适合学习！")
print("\033[32m√\033[0m\n")

print("正在获取信息...")
url=rf.repo+"most.txt"
r=requests.get(url)
b=int(r.text)
数量=str(b+1)
print("\033[32m√\033[0m\n")

os.system('clear')      ##清屏
print('--- Terminals Exercises (高中) ---\n')

print("\033[32m检查通过！\033[0m")

print("目前题库数量:"+数量+"\n")

rf.gui()

##输入序号
模式=input('\n请输入序号：')
print("\n")

##对序号进行判断
if 模式=='1':
	print("答题模式:随机")
	print("\033[36m随机从所有科目中选择题目.\033[0m")
	a=0
	number=random.randint(a,b)
	act="wget "+rf.repo+str(number)+".yaml"
	os.system(act)
	do.练习(number)
	again=input("是/否继续?(y/n):")
	if again=="y":
		做题()
	else:
		print("Bye~")
		sys.exit(0)

if 模式=='2':
	new=数量+".yaml"
	act="cp model.x.yaml "+new
	os.system(act)
	write=input("是否直接编辑题目?(y/n):")
	if write=="y":
		act="nano "+new
		os.system(act)
	else:
		print("请稍后自己手动编辑"+new+"文件")

if 模式=="q":
	print("Bye~")
	sys.exit(0)
