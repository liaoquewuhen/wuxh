import os
import shutil
import re


files_name = [x for x in os.listdir() if '.md' in x]  #取出当前目录下面所有md文件
sep_here = os.sep
for i in range(len(files_name)):
	file_date = ""
	print("正在修改文件：",files_name[i])
	with open(files_name[i],'r',encoding='gbk') as f:
		lines = f.readlines()		
		for j in range(len(lines)):
			if('![' in lines[j]):
				first = lines[j].find('(')
				thisline = lines[j][first+1:-1]     #取出这一行的图片路径				
				path,name = os.path.split(thisline)
				new_path = './image/' + name      #这里默认存在image目录，TODO
				lines[j] = lines[j].replace(thisline,new_path)  #替换md笔记里路径
				try:
					shutil.move(thisline,new_path)      #移动文件（不使用复制是因为图片一般存在C盘）
				except:
					pass                    #忽略已经是相对路径的文件
			file_date = file_date + lines[j]        #存储新的文件内容
	with open(files_name[i],'w') as f:	
		f.write(file_date)


