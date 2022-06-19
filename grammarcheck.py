
import re
def rm(lines):  #去除缩进
    text=[]
    for line in lines:
        line=line.strip()
        text.append(line)
    return text
def gettext(filename):#读取文本得到一个最终需要的列表
    textfile = open(filename,encoding="utf-8")
    txt=textfile.readlines()
    finaltext=rm(txt)
    return finaltext

def checkeachif(line,i):#用正则表达式来对单个if语法检查
    matchObj = re.match('^(\s*)(.*)(if)(\s*)(.*?)(\s*)(==|!=|<=|>=|<|>)(\s*)(.*?)[:]$', line)
    if matchObj == None:
        print("第",i,"行if使用错误")
    else:
        print("暂未发现错误")
def checkeachelif(line,i):#对单个elif语法检查
    result = re.match('^(\s*)(.*)(elif)(\s+)(.*)((>| <| ==| !=| >=| <=)*)(\s*)(.*)[:]$', line)
    if result is None:
        print("第", i, "行elif使用错误")
    else:
        print("暂未发现错误")
def checkeachelse(line,i):#对单个else语法检查
    result = re.match("^(\s*)(else)(\s*)[:]$", line)
    if result is None:
        print("第", i, "行else使用错误")
    else:
        print("暂未发现错误")
def checkeachfor(line,i):#对单个for语法检查
    result = re.match("^(\s*)(for)(\s+)(.*)(\s+)(in)(\s+)(.*)[:]$", line)
    if result is None:
        print("第", i, "行for使用错误")
    else:
        print("暂未发现错误")
def checkeachtry(line,i):#对单个try语法检查
    result = re.match("^(\s*)(try)(.*)[:]$", line)
    if result is None:
        print("第", i, "行try使用错误")
    else:
        print("暂未发现错误")
def checkeachexcept(line,i):#对单个except语法检查
    result = re.match("^(\s*)(except)(.*)[:]$", line)
    if result is None:
        print("第", i, "行except使用错误")
    else:
        print("暂未发现错误")

def checkfor(filename):#检查所得列表中的for
    i=1
    testfor=gettext(filename)
    for eachline in testfor :
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='for':
                checkeachfor(eachline,i)
        i=i+1
def checkif(filename):#检查所得列表中的if
    i=1
    testif=gettext(filename)
    for eachline in testif:
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='if':
                checkeachif(eachline,i)
        i=i+1
def checkelif(filename):#检查所得列表中的elif
    i=1
    testelif=gettext(filename)
    for eachline in testelif :
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='elif':
                checkeachelif(eachline,i)
        i=i+1
def checkelse(filename):#检查所得列表中的else
    i=1
    testelse=gettext(filename)
    for eachline in testelse :
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='else':
                checkeachelse(eachline,i)
        i=i+1
def checktry(filename):#检查所得列表中的try
    i=1
    testtry=gettext(filename)
    for eachline in testtry :
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='try':
                checkeachtry(eachline,i)
        i=i+1
def checkexcept(filename):#检查所得列表中的except
    i=1
    testexcept=gettext(filename)
    for eachline in testexcept :
        lines=str(eachline)
        lines=lines.split()
        for line in lines:
            if line =='except':
                checkeachexcept(eachline,i)
        i=i+1
def run():
    filename=input("请输入要检查的文件路径(采用绝对路径):") 
    while True:
        print("请选择要检查的语法")
        print("1.检查if")
        print("2.检查elif")
        print("3.检查else")
        print("4.检查for")
        print("5.检查try")
        print("6.检查except")
        print("7.返回上一级")
        a=input("请选择:")
        if   a=='1':
            checkif(filename)
        elif a=='2':
            checkelif(filename)
        elif a=='3':
            checkelse(filename)
        elif a=='4':
            checkfor(filename)
        elif a=='5':
            checktry(filename)
        elif a=='6':
            checkexcept(filename)
        elif a=='7':
            break
        else:
            print("暂无更多词法分析，请选择1-6")
if __name__ == '__main__':
    run()




