#坐标-图 v1.0

#给定整数坐标
coordinate = [[5,6],[1,2,5,6],[2,3,4],[2,3,4],[1,2,5,6],[5,6]]

#得到y从小到大的序列
y_axis = []
for coordinate_y in coordinate:
    y_axis.extend(coordinate_y)
del coordinate_y
y_axis = list(set(y_axis))
y_axis.sort(reverse=True)
y_axis = tuple(y_axis)

#绘图
for y in range(y_axis[0],y_axis[len(y_axis)-1]-1,-1):   # y
    print('')
    print(y,'\t',end='')   #显示y轴坐标
    
    x_index,former_x = 0,0   # x
    for coordinate_x in coordinate:
        if y in coordinate_x:
            print('  '*(x_index-former_x),end='')
            print('██',end='')
            former_x = x_index+1
        x_index+=1

#显示所有点的坐标
x_index = 0
print('')
for coordinate_x in coordinate:
    for y in coordinate_x:
        print('(%d,%d)' % (x_index+1,y),end=' ')
    x_index+=1