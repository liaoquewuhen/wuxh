from collections import defaultdict
words_dict = defaultdict(dict)
word = ""
means = ""
word_list = []
word_index = 0
mean_finish = False
'''  有些问题的版本（其实是文件的读取有问题）
with open("./words.txt","r") as f:
    for line in f.readlines():
        if(line[0] == "<"):
            word = line[1:-2]
            print (line[1:-2])
        elif (line[0] == "{"):    #如果这一行是以{开头，说明是解释的开始
            if (line[-1] == "}"):   #本行以}结尾说明解释已结束
                mean_finish = True
                words_finish = True
                means = means + line
            else:
                means = means + line
        elif(line[-1] != "}"):
            means = means + line
        elif(line[-1] == "}"):
            mean_finish = True
            words_finish = True
            means = means + line
        if(mean_finish and words_finish):   #顺利抓到单词和意思的情况
            words_dict[word] = means
            mean_finish = False
            words_finish = False
for key in words_dict:
    print(key," : ",words_dict[key])
	'''
with open("./words.txt","r",encoding="utf-8") as f:
	for line in f.readlines():
		
		if "<" in line:  #寻找出单词所在行数
			word = line
		elif "}" in line:  #找释义开始行数
			means = means + '\n' + line
			mean_finish = True
		else:              #除了上述两种情况，都是释义包括的行数
			means = means + '\n' + line
		
		if(mean_finish):
			word = word.replace('<','').replace('>','') #去除<>
			means = means.replace('{','').replace('}','') #去除{}
			words_dict[word] = means
			mean_finish = False    #开始下一个单词的查找  
			word = ""
			means = ""

for key in words_dict:
	word_list.append(key)
	
from tkinter import *

def next_word():
	global word_index
	word_index = word_index +1
	if (word_index > len(word_list)-1):
		word_index = len(word_list)-1
	
	txt_word.configure(text=word_list[word_index] + '\n'+ words_dict[word_list[word_index]])
	
def back_word():
	global word_index
	word_index = word_index -1
	if (word_index < 0):
		word_index = 0
	
	txt_word.configure(text=word_list[word_index] + '\n'+ words_dict[word_list[word_index]])
	
root = Tk()
root.title('英语单词')
root.configure(background='white')
root.geometry('720x720')
txt_word = Label(root,text=word_list[word_index] + '\n'+ words_dict[word_list[word_index]],bg='white')
txt_word.place(relx = 0.1,rely = 0.1, relwidth = 0.4, relheight=0.4,anchor='w')
btn_back = Button(root,text='back',command=back_word,bg='white')
btn_back.place(relx = 0.05,rely = 0.5, relwidth = 0.05, relheight=0.0889)
btn_next = Button(root,text='next',command=next_word,bg='white')
btn_next.place(relx = 0.1,rely = 0.5, relwidth = 0.05, relheight=0.0889)

root.mainloop()
