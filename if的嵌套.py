has_ticket = True
knife_length = 10
if has_ticket:
    print("车票检查通过，开始安检")
    if knife_length > 20:
        print("你带的刀太长了，有%d厘米长" % knife_length)
        print("不允许上车")
    else:
        print("可以上车")

else:
    print("请先买票")