#坐标-图 v1.1
print('坐标-图 v1.1')
print('1 把坐标 x y 对应 列表索引 索引值 改为 x y 对应 字典key 字典value')
print('2 删了一些变量 简化了以下代码')

#给定整数坐标
coordinate = {1:[5,6],2:[1,2,5,6],3:[2,3,4],4:[2,3,4],5:[1,2,5,6],6:[5,6]}

#可能不需要的功能
#确保x连续 如果缺失了x值则自动填补
x_axis = []
for x in coordinate:
    x_axis.append(x)
x_axis.sort()
if len(x_axis) < len(range(x_axis[0],x_axis[-1]+1)):
    for x in range(x_axis[0],x_axis[-1]+1):
        try:
            coordinate[x] = coordinate[x]
        except:
            coordinate[x] = []

x_axis = tuple(range(x_axis[0],x_axis[-1]+1))
del x


#得到y从小到大的序列
y_axis = []
for coordinate_y in coordinate:
    y_axis.extend(coordinate[coordinate_y])
del coordinate_y
y_axis = list(set(y_axis))
y_axis.sort(reverse=True)
y_axis = tuple(y_axis)

#绘图
for y in range(y_axis[0],y_axis[len(y_axis)-1]-1,-1):   # y
    print('')
    print(y,'\t',end='')   #显示y轴坐标
    
    former_x = 0   # x
    for x in x_axis:
        if y in coordinate[x]:
            print('  '*(x-former_x),end='')
            print('██',end='')
            former_x = x+1
del x,former_x

#显示所有点的坐标
print('')
for x in coordinate:
    for y in coordinate[x]:
        print('(%d,%d)' % (x+1,y),end=' ')