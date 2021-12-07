#!/bin/bash

time=`date +%Y%m%d`
cd /home/ryan
wget https://www.twse.com.tw/fund/TWT44U?response=csv&date=$time
mv TWT44U\?response\=csv 1.txt
iconv -f BIG-5 -t UTF-8 1.txt > 2.txt
cat 2.txt | cut -d ' ' -f4,9-20 | cut -d \" -f3,5 | cut -d , -f1 | grep -v 0 | uniq | awk -F '"' '{print $1}' | uniq > 3.txt
sed -i '1d' 3.txt
sed -i '$d' 3.txt
awk -F, '{print $1}' output.csv > 4.txt
grep -v -f 4.txt 3.tx | grep -Ev '彰化銀|京城銀|台中銀|臺企銀|高雄銀|聯邦銀|遠東銀|安泰銀|華南金|富邦金|國泰金|開發金|玉山金|元大金|兆豐金|台新金|新光金|國票金|永豐金|中信金|第一金|王道銀|日盛金|上海銀|合庫金|永豐金|國票金|開發金' > $time\.txt
