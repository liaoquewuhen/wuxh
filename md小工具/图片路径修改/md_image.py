import os
import shutil
import re


files_name = [x for x in os.listdir() if '.md' in x]  #取出当前目录下面所有md文件
sep_here = os.sep
for i in range(len(files_name)):
	file_date = ""
	print("正在修改文件：",files_name[i])
	with open(files_name[i],'r') as f:
		lines = f.readlines()		
		for j in range(len(lines)):
			if('![' in lines[j]):
				first = lines[j].find('(')
				thisline = lines[j][first+1:-2]     #取出这一行的图片路径	
				print(thisline)
				path,name = os.path.split(thisline)
				new_path = './image/' + name      #这里默认存在image目录，TODO
				lines[j] = lines[j].replace(thisline,new_path)  #替换md笔记里路径				
				if path[0] != '.':
					shutil.copy2(thisline,new_path)  
			file_date = file_date + lines[j]        #存储新的文件内容
	with open(files_name[i],'w') as f:	
		f.write(file_date)


