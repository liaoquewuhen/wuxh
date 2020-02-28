#!/bin/bash
#echo 'message:hi' | zenity --notification --listen
#notify-send "My name is bash and I rock da house"

#就这么简单
word=`xclip -out`
mean=`sdcv -n ${word}|grep "^[a-z]"`
pkill notify-osd
notify-send   "$mean"
echo "<${word}>" >> ~/git_wuxh/划词翻译/words.txt
echo "{${mean}}" >> ~/git_wuxh/划词翻译/words.txt

echo "**${word}**" >> ~/git_wuxh/划词翻译/words.md
echo ">${mean}" >> ~/git_wuxh/划词翻译/words.md
echo " " >> words.md
