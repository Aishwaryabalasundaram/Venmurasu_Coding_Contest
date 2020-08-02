from tamil import utf8,numeral
num=int(input("Enter the number of words to be displayed:"))
 
if(num<=12000):
    f=open(r"venmurasu_tamil_word_file_13.txt",'r',encoding='utf8')
else:
    f=open(r"venmurasu_tamil_word_file_complete.txt",'r',encoding='utf8')
    
tamil_list=f.read().split(',')
f.close()  
word_list=dict()
for val in tamil_list:
    letters = utf8.get_letters(val) 
    length = len(letters)
    if length!=0:
        key=length
        word_list.setdefault(length,[])
        word_list[length].append(val)    
count=num
file=open("sorted_words_file.txt",'a',encoding='utf8')
i=1
for key in sorted(word_list,reverse=True):
    length=len(word_list[key])
    if count>0:
        print(numeral.num2tamilstr(key),u'எழுத்துக்கள்  :   ' ,key,'\n',i,':  ',end='')
        print(*word_list[key][:count],sep = '\n',end='\n\n')
        i+=length
        file.write(str(key))
        file.write(str(word_list[key][:count])[1:-1])
        count=count-length
        file.write(',')           
file.close()
