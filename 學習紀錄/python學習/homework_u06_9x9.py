#
for i in range(1,10):
    for j in range(2,6):
        print('%d*%d=%-2d ' % (j,i,i*j),end="")
    print("")
print("\n")
for i in range(1,10):
    for j in range(6,10):
        print('%d*%d=%-2d ' % (j,i,i*j),end="")
    print("")

#老師作法

for y in range(1,10):  #一般九九乘法表
    for x in range(2,10):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')


print('')  #第一種方法
for y in range(1,10):
    for x in range(2,6):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')

print('')

for y in range(1, 10):
    for x in range(6,10):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
    else:
        print('')

print('\n------------------------------------')

for y in range(1,19): #第二種方法

    for x in range(2,6):
        if y < 10:
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
        else:
            x1 = x + 4
            y1 = y - 9
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format(x1, '×', y1, '= ', x1 * y1), end='')
    else:
        print('')
