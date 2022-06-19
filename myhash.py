def hash_main():
    while True:
        print("1.计算hash函数")
        print("2.返回上一级")
        h=input("请选择：")
        if h=='1':
            hash1=input("请输入：")
            print("Hash: %s"%hash(hash1))
        elif h=='2':
            break
if __name__ == '__main__':
    hash_main()
