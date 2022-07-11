result = 0
i =0
while i <= 100:
    if i % 2 ==0:     #判断i的变量是否是一个偶数 判断奇数 if i % 2 != 0
        print(i)
        result += i
    i += 1
print("0-100之间偶数和为 = %d" % result)
