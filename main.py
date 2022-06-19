import dazi
import shuma
import myhash
import cipintongji
import grammarcheck
import pachong
import playball
def menu():#定义主菜单
    while True:
        print("作业清单")
        print("1.写大字")
        print("2.Hash")
        print("3.七段数码管")
        print("4.词频统计")
        print("5.踢球")
        print("6.爬虫")
        print("7.词法分析")
        try:
            s=input("请选择:")
            if s=='1':
                dazi.dazi_main()   #写大字程序
            elif s=='2':
                myhash.hash_main()
            elif s=='3':
                shuma.shuma_main()     #七段数码管程序
            elif s=='4':     #词频统计程序
                cipintongji.cipin_main()
            elif s=='5':
                playball.play_main()
            elif s=='6':
                pachong.pachong_main()
            elif s=='7':
                grammarcheck.run()
            else:
                print("暂无更多选项,请输入一个1-7中的数")
                menu()
        except:
            print("未知错误")
            menu()

def main():
    menu()
if __name__ == '__main__':
    main()