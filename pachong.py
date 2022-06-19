from turtle import st
import requests
from bs4 import BeautifulSoup
LAYER=1
#url ="https://v.qq.com/"

def getHTML(url):#获取HTML文件
    try:
        r = requests.get(url)
        r.encoding = 'utf-8' #将文件格式都改为utf-8
        return r.text
    except:
        return ""

def getlinks(url):#获取链接并解析
    html = getHTML(url)
    soup = BeautifulSoup(html, "html.parser")#使用Beautifulsoup来解析获得的HTML文件
    links = soup.find_all('a')
    return links

def getprint(url,layers):#运用递归一层一层爬出所有的link
    global LAYER
    if LAYER <= layers : #layyer
        LAYER += 1
        link_list=[]
        links=getlinks(url)
        for link in links:
            each_link = link.get("href")
            if ("https" in str(each_link)) or ("http" in str(each_link)):               #对一些可能格式不对的网址进行清理，不然会造成访问错误
                link_list.append(each_link)
                getprint(each_link,layers)
        for i in link_list:
            print(i)
        LAYER-=1
    else:
        return 0

def pachong_main():

    url=input("请输入网址(格式为https://*****)：")
    layers=int(input("请选择要爬的层数："))
    getprint(url,layers)
if __name__ == '__main__':
    pachong_main()