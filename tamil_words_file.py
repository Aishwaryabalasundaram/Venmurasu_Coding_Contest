import timeit
from bs4 import BeautifulSoup
from tamil import utf8

START = timeit.default_timer() 

def tamil_words(count):
        f=open("blogs/venmurasu_blog_{}.txt".format(count),'rb')
        html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        
        for anchor in soup('a'):
            anchor.decompose()
            
        for strong in soup('strong'):
            strong.decompose()
        
        word = soup.find_all('p')
                
        word_list = []
        for i in range(len(word)):
            w=word[i].get_text()
            a=w.split(" ")
            word_list.extend(a)
            
        temp_list_1=[]    
        for val in word_list:
            a=utf8.has_tamil(val) #Only those words which have tamil letters are added to this list..english letters are eliminated
            if a:
                temp_list_1.append(val)
                
        temp_list_2=[]
        for line in temp_list_1:
            line=line.replace("!","\n").replace(".","\n").replace("?","\n").replace(";","\n").replace(":","\n").replace(",","\n").replace("“","\n").replace("”","\n").replace("‘","\n").replace("’","\n").replace("…","\n").replace("===========================================================","\n").replace("\xa0",'\n')                                     
            temp_list_2.append(line)
                
        tamil_list=[]
        for val in temp_list_2:
            val=val.split("\n")         #Splitting based on new line
            tamil_list.extend(val)
            
        avoid_list=[u'பின்னூட்டங்கள்', u'மூடப்பட்டுள்ளது', u'உங்கள்', u'மின்னஞ்சல்', u'இங்கே', u'கொடுத்து', u'அதன்', u'வழி', u'பதிவுகளைப்', u'பெறவும்', u'பின்', u'தொடர']
            
        file=open("venmurasu_tamil_word_file_13.txt",'a',encoding='utf8')
        for val in tamil_list:
            if val is not '' :
              if val not in avoid_list:
                  letters = utf8.get_letters(val) 
                  length = len(letters)
                  if length>=13:   #length>0 is stored in venmurasu_tamil_word_file_complete.txt
                      file.write(val)
                      file.write(',')
        file.close()
             
for count in range(1937):
    tamil_words(count)
    print(count)
    
STOP = timeit.default_timer()
execution_time = STOP - START  #Stop timer

print("Program Executed in "+str(execution_time))
              
                      
            

            
            