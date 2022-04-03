import sys
import os

type="*.yaml"
act="ls "+type+" >> tem.txt"
os.system(act)
result=[]
with open('tem.txt','r') as f:
	for line in f:
		result.append(line.strip('\n').split(',')[0])
os.system("rm tem.txt")
l=result[:-2]
want=max(l)
final=want[:-5]
real=int(final)+1
name=str(real)+".yaml"
do="cp model.x.yaml "+name+" && nano "+name
edit=input("是否直接编辑题目?(y/n):")
if edit=="y":
	os.system(do)
else:
	do="cp model.x.yaml "+name
	os.system(do)
	print("请稍后自己手动编辑"+name+"文件")
