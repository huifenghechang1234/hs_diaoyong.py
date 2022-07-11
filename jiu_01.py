def  multiple_table():



    row = 1   #row 行号
    while row <= 9:
            col  = 1              #col 列号
            while col <= row:
                print("%d  * %d = %d" % (col, row, col *row),end=    "\t")
                col += 1
            print("")
            row += 1


