import time
import os

try:
        import yaml
        pass
except ImportError:
        print("没有安装依赖，正在安装...")
        os.system('pip install pyyaml')

config=yaml.load(open('config.yaml'),Loader=yaml.FullLoader)
name=config['main']['username']
repo=config['main']['repo']
ok=config['main']['ok']

def gui():
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n欢迎前来学习的\033[36m"+name+"\033[0m同学！\n")
	print("1. 开始练习")
	print("2. 我要出题")
	print("3. 分析报告")
	print("4. 错题重做")
	print("5. 打包题目")
	print("a. 关于")
	print("q. 退出程序")

def fenxi():
	with open(".temp/all.txt",'r') as f:
		全部题数=f.read()
	with open(".temp/right.txt",'r') as f:
		正确题数=f.read()
	with open(".temp/wrong.txt",'r') as f:
		错误题数=f.read()
	os.system("clear")
	print(name+"同学:\n")
	print("你一共做了"+全部题数+"道题，其中:\n")
	print("\033[32m回答正确\033[0m的题数有:"+正确题数)
	print("\n\033[31m回答错误\033[0m的题数有:"+错误题数)
	print("\n\033[32m正确率为:\033[0m {:.2%}".format(int(正确题数)/int(全部题数)))
	print("\n\033[31m错误率为:\033[0m {:.2%}".format(int(错误题数)/int(全部题数)))
	if int(正确题数) > int(错误题数):
		print("\n总体来看，答对的题多于答错的题，继续保持吧！")
	else:
		print("\n结果看起来不尽人意啊..不过不要灰心，继续加油吧！")
