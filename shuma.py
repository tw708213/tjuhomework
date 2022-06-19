
import turtle as t
import datetime as d
def drawgap(): #绘制数码管的间距
    t.penup()
    t.fd(95)
    t.right(90)
    t.fd(8)
def drawline(draw): #绘制单段数码管
    if draw:  #采用begin_fill填充所需要显示的单段数码管
        t.pendown()
        t.begin_fill()
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.end_fill()
        drawgap()
    else:     #不需要显示的数码管不填充，只显示其边框
        t.pendown()
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        t.fd(83)
        t.right(45)
        t.fd(6)
        t.right(90)
        t.fd(6)
        t.right(45)
        drawgap() 
def drawdigit(d): #根据数字绘制七段数码管
    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    t.right(180)
    t.fd(8)
    t.right(90)
    t.fd(3)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in[0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in[0,1,2,3,4,7,8,9] else drawline(False)
    t.right(180)
    t.fd(40)
    t.left(90)
    t.fd(4.5)
    t.right(90)
def drawdata(data):#能够画出任意所输入的数字
    for x in data:
        drawdigit(eval(x))
def drawdate(date):  #画出当前的日期，并按**年**月**日格式输出
    t.color("black","black")
    for i in date:
        if i == '-':
            t.write('年',font=("Arial",18,"normal"))
            t.color("black","black")
            t.fd(40)
        elif i =='=':
            t.write('月',font=("Arial",18,"normal"))
            t.color("black","black")
            t.fd(40)
        elif i=='+':
            t.write('日',font=("Arial",18,"normal"))
        else:
            drawdigit(eval(i))
def shuma_main():      #定义了一个可选择的菜单，其可以选择输出当前的日期，输出任意所输入的数字
    while True:
        print("请选择以下功能")
        print("1.当前日期")
        print("2.显示输入的数据")
        print("3.返回上一级")
        a=input("请选择：")
        if a=='1':#当前日期
            screen()
            drawdate(d.datetime.now().strftime('%Y-%m=%d+'))
            t.done()
            t.hideturtle()              
        elif a=='2':#输入数字
            b=input("请输入数据：")
            screen()
            drawdata(b)
            t.done()
            t.hideturtle()
        elif a=='3':
            break
def screen():
    t.setup(1000.1000,0,0)
    t.speed(50)
    t.penup()
    t.bk(500)
if __name__ == '__main__':
    shuma_main()
    





            




