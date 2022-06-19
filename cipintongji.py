import os
def gettext(file):#获得文本数据
    f=open(file,encoding = "utf-8")
    txt=f.readlines()#读取文本
    txt=str(txt)
    for  ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':#去除一些不需要的字符
        txt=txt.replace(ch," ")
    return txt
def getkeyword(file):
    danci=gettext(file)
    words=danci.split()
    count={}
    keywords={'False','None','True','and','as','assert','break','class','continue','def','del','elif','else','except','finally','for','from','global','if','if','import','in','is','lambada','nonlocal','not','or','pass','raise','return','try','while','with','yield'}
    for word in words: 
        if word in keywords:
            count[word]=count.get(word,0)+1
    items=list(count.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(32):
        try:
            word,number=items[i]
            print("{0:<10}{1:>5}".format(word,number))
        except:
            print("空")
def cipin_main():
    file=input("请输入要统计的文件路径(采用绝对路径):")
    getkeyword(file)
if __name__ == '__main__':
    cipin_main()



