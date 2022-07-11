
row = 1
while row <= 5:
    #每一行要打印的星星和当前的行号是一致的
#增加一个循环，专门负责当前行，每一‘列’的星星显示

#定义一个列计数器变量
    col = 1
    #开始循环
    while col <= row:
        #print("%d" % col)
        print("*",end="")
        col += 1
       # print("第%d行" % row)
    print("")
    row += 1