import yaml
import os
import check

def 练习(number):
	config=yaml.load(open(str(number)+'.yaml'),Loader=yaml.FullLoader)
	科目=config['必需项']['科目']
	题目=config['必需项']['题目']
	答案=config['必需项']['答案']
	选项=config['非必需项']['选项']
	解析=config['非必需项']['解析']
	出题者=config['非必需项']['出题者']
	os.system("clear")
	print("所属科目:\033[36m"+科目+"\033[0m\n")
	print("题目:\n")
	print(题目)
	if 选项==0:
		pass
	else:
		print("\n")
		print(选项)
	answer=input("\n请输入答案:")
	print("\n")
	print("你的答案:"+answer)
	print("\n\033[36m[正确答案]\033[0m")
	print(答案)
	if answer==答案:
		print("\n\033[32m回答正确！\033[0m")
		check.pure()
		print("虽然回答正确了，但还是看看解析吧！\n")
		print("\033[36m[解析]\033[0m\n"+解析)
	else:
		print("\n\033[31m回答错误！\033[0m")
		print("不要灰心，看看解析吧！\n")
		print("\033[36m[解析]\033[0m\n"+解析)
	if 出题者==0:
		pass
	else:
		print("\n本题提供者:\033[36m"+出题者+"\033[0m\n")
	os.system("rm -rf "+str(number)+".yaml")
