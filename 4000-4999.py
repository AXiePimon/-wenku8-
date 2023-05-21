import requests
import random
from lxml import etree

global x
x=4000
urls=['https://dl1.wenku8.com/down/txtutf8/4/{}.txt'.format(i) for i in range(4000,5000)]
path=r'D:\novels\4000-4999\novel'
headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
def get_text(url,x):
    r=requests.get(url,headers=headers)
    r.encoding='gdk'
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
input("全部小说已下载完成，按回车键自动退出",x)
