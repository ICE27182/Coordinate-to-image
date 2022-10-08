#坐标-图 v2.2   10/2/2022

#介绍
print('坐标-图 v2.2')
print('1 对齐x')

#参数
#显示方式  0 默认值   1 高亮   2 很暗     4 下划线    5 闪烁
#前景色   30 黑色   31 红色   32 绿色    33 黄色   34 蓝色   35 红紫   36 蓝绿   37 白色
#背景色   40 黑色   41 红色   42 绿色    43 黄色   44 蓝色   45 红紫   46 蓝绿   47 白色
#30 - 37 黑 深红 深绿 土黄 蓝 紫 天蓝 浅灰
#30;1 - 37;1 深灰 亮红 绿 亮黄 浅蓝 红紫 湖蓝 白
coordinate = {   #色彩 前两位为颜色 第三位为默认/高亮/暗 第四位可选 为闪烁
    8:{0:370,1:320,2:321,3:321,4:371,5:321,6:320,7:320},
    7:{0:320,1:321,2:320,3:321,4:320,5:321,6:320,7:370},
    6:{0:321,1:301,2:301,3:321,4:320,5:301,6:301,7:371,-3:351},
    5:{0:321,1:301,2:300,3:321,4:320,5:300,6:301,7:321,-1:0},
    4:{0:321,1:320,2:321,3:301,4:301,5:371,6:320,7:321},
    3:{0:370,1:320,2:301,3:300,4:300,5:301,6:321,7:371},
    2:{0:371,1:320,2:300,3:300,4:300,5:300,6:320,7:321,9:361},
    1:{0:321,1:321,2:300,3:321,4:370,5:300,6:320,7:321},
    -3:{0:300,1:310,2:320,3:330,4:340,5:350,6:360,7:370},
    -4:{0:301,1:311,2:321,3:331,4:341,5:351,6:361,7:371},
    -2:{0:302,1:312,2:322,3:332,4:342,5:352,6:362,7:372},
    -6:{0:3005,1:3105,2:3205,3:3305,4:3405,5:3505,6:3605,7:3705},

}
y_axis = True
x_limit = False

x_max,x_min = 0,0
for y in coordinate.keys():
    for x in coordinate[y].keys():
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = x
print(x_min,x_max)
#绘图
def x_line(former_x):   #后面要用两次 所以干脆变成函数了
    if x in coordinate[y].keys():   
            print('  '*(x-former_x-1),end='')
            if coordinate[y][x] == 0:
                print(f'\033[0m██\033[0m',end='')
            elif coordinate[y][x] < 1000:
                print(f'\033[{str(coordinate[y][x])[2]};{str(coordinate[y][x])[0:2]}m██\033[0m',end='')
            elif len(str(coordinate[y][x])) == 4:   #闪烁与否
                print(f'\033[{int(str(coordinate[y][x])[2])};{int(str(coordinate[y][x])[3])};{int(str(coordinate[y][x])[0:2])}m██\033[0m',end='')
            former_x = x
    return former_x

for y in range(max(coordinate.keys()),min(coordinate.keys())-1,-1):
    if y_axis == True:   #是否显示y坐标
        print(y,'\t',end='')
    
    if y not in coordinate.keys() or coordinate[y]=={}:
        print('')
        continue 
   
    if x_limit == False:   #允许 x < 0
        former_x = x_min-1
        for x in range(x_min,x_max+1):
            former_x = x_line(former_x)
    elif x_limit == True:   #忽略 x < 0 的坐标
        former_x = 0
        for x in range(0,x_max+1):
            former_x = x_line(former_x)
    print('')
print('')