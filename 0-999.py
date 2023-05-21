import requests
import random
from lxml import etree

global x
x=0
urls=['https://dl1.wenku8.com/down/txtutf8/0/{}.txt'.format(i) for i in range(0,1000)]
path=r'D:\novels\novel'
headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
def get_text(url,x):
    r=requests.get(url,headers=headers)
    r.encoding='UTF-8'
    selector=etree.HTML(r.text)
    title=str(x)

    #text2=selector.xpath('/html/body/pre/text()[2]')
    with open(path+title+'.txt','w',encoding='UTF-8') as f:
        for i in str(r.text):
            f.write(i)
        #for i in text2:
            #f.write(i)#

if __name__ == "__main__":
    for url in urls:
        get_text(url,x)
        print(x,"finished")
        x+=1

