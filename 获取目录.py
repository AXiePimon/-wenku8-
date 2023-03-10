import requests


from lxml import etree



global x
x=0
urls=['https://www.wenku8.net/book/{}.htm'.format(i) for i in range(0,5000)]

headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
def get_text(url,x):
    r=requests.get(url,headers=headers)
    r.encoding='gbk'
    selector=etree.HTML(r.text)
    title=str(x)
    text=selector.xpath('//*[@id="content"]/div[1]/table[1]/tr[1]/td/table/tr/td[1]/span/b/text()')
    #text2=selector.xpath('/html/body/pre/text()[2]')
    with open("name.txt","a",encoding='gbk') as f:
 
        f.write('\r\n'+title+"————"+str(text))
        #for i in text2:
            #f.write(i)#

if __name__ == "__main__":
    for url in urls:
        get_text(url,x)
        print(x,"finished")
        x+=1
input("全部小说已解析完成，按回车键自动退出",x)
