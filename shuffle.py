import random
import csv

open_file="./all_ok.csv"         #要洗牌的檔案

output_name="./all_ok_shaf.txt"  #要輸出的檔名

#記得刪除原本的 all_ok_shaf.txt

output = open(output_name,'a')
lines=[]

with open(open_file) as csvfile:        
    reader = csv.reader(csvfile)
    for row in reader:
        lines.append(str(row[0]))
        
        
random.shuffle(lines)
for line in lines:
    input_txt = str(line)+"\n"
    output.write(input_txt)
    
output.close()
print("OK...請打開all_ok_shaf.txt")
