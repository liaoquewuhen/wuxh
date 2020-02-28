#!/bin/bash
#echo 'message:hi' | zenity --notification --listen
#notify-send "My name is bash and I rock da house"

#就这么简单
word=`xclip -out`
mean=`sdcv -n ${word}|grep "^[a-z]"`
pkill notify-osd
notify-send   "$mean"
echo "<${word}>" >> ~/worker/bash/words.txt
echo "{${mean}}" >> ~/worker/bash/words.txt

echo "**${word}**" >> ~/worker/bash/words.md
echo ">${mean}" >> ~/worker/bash/words.md
echo " " >> ~/worker/bash/words.md
