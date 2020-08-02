import ssl
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

file=open("venmurasu_blog_url_list.txt",'w')
def scraping(url,count):
        file2=open("blogs/venmurasu_blog_{}.txt".format(count),'wb')
        f = urlopen(url, context=CTX).read()
        file2.write(f)
        file2.close() 
        soup=bs(f,'html.parser')
        try:
            url=soup.find(class_='nav-next')
            next_url=url.find('a').attrs['href']
        except:
            return None
        else:        
            if next_url:
                file.write(str(next_url))
                file.write('\n')
            return next_url                    
count=0
url="https://venmurasu.in/2014/01/01/%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AE%E0%AF%81%E0%AE%B0%E0%AE%9A%E0%AF%81-%E0%AE%A8%E0%AF%82%E0%AE%B2%E0%AF%8D-%E0%AE%92%E0%AE%A9%E0%AF%8D%E0%AE%B1%E0%AF%81/"
file.write(str(url))
file.write('\n')
while True:
    print(count)
    url=scraping(url,count)
    count=count+1
    if url is None:
        break      
file.close()