import os
import shutil
import re


files_name = [x for x in os.listdir() if '.md' in x]            #取出当前目录下面所有md文件
sep_here = os.sep
folder_name = input("可输入本地存在的文件夹名以存放图片:（默认为image）")
find_folder = False

while find_folder == False:
	if folder_name == "":
		folder_name = "image"
	if folder_name not in os.listdir():
		chocie = input("文件夹不存在，是否直接创建文件夹[y]/n")
		if chocie == "" or chocie == "y":
			os.mkdir(folder_name)
		else:
			folder_name = input("可输入本地存在的文件夹名以存放图片:（默认为image）")
	else:
		find_folder = True
	

for i in range(len(files_name)):
	file_date = ""
	print("正在修改文件：",files_name[i])
	with open(files_name[i],'r',encoding = 'UTF-8') as f:
		lines = f.readlines()		
		for j in range(len(lines)):
			if('![' in lines[j]):
				first = lines[j].find('(')
				next = lines[j].find(')')
				thisline = lines[j][first+1:next]                 #取出这一行的图片路径	
				#print('原图片存放在：',thisline)
				path,name = os.path.split(thisline)
				new_path = './'+folder_name+'/' + name                    #这里默认存在image目录，TODO
				lines[j] = lines[j].replace(thisline,new_path)  #替换md笔记里路径				
				if path[0] != '.':
					shutil.copy2(thisline,new_path)
					#print('将文件复制到:',new_path)
			if('<img' in lines[j]):                                   #html格式插入的图片
				first = lines[j].find('\"')
				next = lines[j].find("\"",first+1)
				thisline = lines[j][first+1:next]                 #取出这一行的图片路径	
				#print('原图片存放在：',thisline)
				path,name = os.path.split(thisline)
				new_path = './'+folder_name+'/' + name                    #这里默认存在image目录，TODO
				lines[j] = lines[j].replace(thisline,new_path)  #替换md笔记里路径				
				if path[0] != '.':
					shutil.copy2(thisline,new_path)
					#print('将文件复制到:',new_path)
			file_date = file_date + lines[j]                    #存储新的文件内容
	with open(files_name[i],'w',encoding = 'UTF-8') as f:	
		f.write(file_date)


