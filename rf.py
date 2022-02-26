import time

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
	print("q. 退出程序")
