##导入模块
import sys	##退出程序
import os	##系统指令
import time	##显示时间
import do	##题目处理
import platform	##系统检测
import rf	##读取配置
import random	##随机抽取
import requests	##获取数据
import check	##签到机制

def 做题():
	number=random.randint(a,b)
	act="wget "+rf.repo+str(number)+".yaml"
	os.system(act)
	do.练习(number)
	again=input("是/否(y/n)继续:")
	if again=="y":
		做题()
	else:
		pass

def 处理错题():
	错题=os.listdir("错题本")
	print("\n错题都有:\n")
	for wrongti in 错题:
		print(wrongti)
	选择=input("\n请输入以上列出的一个文件的数字ID:")
	do.wrong(选择)
	again=input("是否(y/n)处理下一道错题:")
	if again=="y":
		处理错题()
	else:
		pass

os.system('clear')	##清屏
print('--- Terminals Exercises (高中) ---\n')

print("正在检查配置...")
##检查config是否配置好
if rf.ok!=1:
	print('请打开config.yaml进行配置后再运行脚本！')
	writeconf=input("是否(y/n)直接进行配置:")
	if writeconf=="y":
		os.system("nano config.yaml")
		os.system("clear")
	else:
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

check.check()

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
	if os.path.exists(new):
		os.system("python3 chongfu.py")
	else:
		act="cp model.x.yaml "+new
		os.system(act)
		write=input("是否直接编辑题目?(y/n):")
		if write=="y":
			act="nano "+new
			os.system(act)
		else:
			print("请稍后自己手动编辑"+new+"文件")

if 模式=="3":
	rf.fenxi()

if 模式=="4":
	处理错题()

if 模式=='5':
	print("此功能为:将已编辑过的题目进行打包方便发送给听话的便当.")
	pack=input("\n是否(y/n)继续:")
	print("\n")
	if pack=="y":
		name=rf.name+"的所有题目！.tar.gz"
		dirname=rf.name+"的所有题目"
		if os.path.exists(name):
			print("似乎已经存在已经打包但未发送的题目了...请先将\033[36m "+name+"\033[0m 发送给\033[36m听话的便当\033[0m！")
		else:
			do="mkdir "+dirname+" && cp *.yaml "+dirname+" && rm -rf "+dirname+"/config.yaml "+dirname+"/model.x.yaml"
			os.system(do)
			查重="ls "+str(dirname)+" >> 文件.txt"
			os.system(查重)
			with open("文件.txt","r") as f:
				重复=f.read()
				重复=重复.replace("\n"," ")
			act="rm "+重复
			os.system(act)
			tar="tar -zcvf "+name+" "+dirname+" && rm 文件.txt && rm -rf "+dirname
			os.system(tar)
			print("\n已经将你出的所有题目打包至压缩文件 \033[36m"+name+"\033[0m 啦！请尽快发给\033[36m听话的便当\033[0m(联系方式在编辑题目时应该看见了吧🤔)")

if 模式=="a":
	os.system("clear")
	time.sleep(1.5)
	print("Hello！没想到你真的会打开这个诶...")
	time.sleep(1.5)
	print("(早知道这样的话我就好好写'关于'了🤔\n")
	time.sleep(1.5)
	print("* 关于作者")
	time.sleep(1.5)
	print("除了我\033[36m听话的便当\033[0m之外还有谁会做这样一个项目呢?🌚")
	time.sleep(1.5)
	print("不过啊不过，还是有用户的嘛！(就比如说正在阅读的\033[36m"+rf.name+"\033[0m)")
	time.sleep(1.5)
	print("\n* 关于程序")
	time.sleep(1.5)
	print("出于'想玩'的想法制作了这个小程序，算是我最认真，码字量最大的程序了！")
	time.sleep(1.5)
	print("\n* 关于积分")
	time.sleep(1.5)
	print("(积分其实是没有用的..某种意义上，因为你不能用积分换钱💰，或者从我手里换些什么东西.")
	time.sleep(1.5)
	print("不过，你可以将你的积分数目截图发给我(联系方式在博客: https://wzk0.github.io/about)，在我闲(或者投送人数比较多)的时候，我会做一个积分榜单，供大家'攀比'！")
	time.sleep(1.5)
	print("喂！不要想着直接修改积分数目！虽然是以明文储存在本地的方式，不要欺骗自己！")
	time.sleep(1.5)
	print("\n最后，谢谢你！"+rf.name+"，我的少数用户之一，让我更新下去的动力源泉！")
	time.sleep(1.5)
	print("\n❤️")

if 模式=="q":
	print("Bye~")
	sys.exit(0)
