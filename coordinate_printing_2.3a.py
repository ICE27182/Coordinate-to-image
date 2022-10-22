#坐标-图 v2.3a   10/9/2022
from time import time as tm

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

def draw_c(coordinate,y_axis = True,x_limit = False):
    t1,t2 = [],[]

    def xline(start_value):
        '''将单行的x坐标存入列表 会用2次'''
        for x in range(start_value,max(coordinate[y].keys())+1):
            if x in coordinate[y].keys() and len(str(coordinate[y][x])) == 3:
            #点  无闪烁
                coor.append(f'\033[{str(coordinate[y][x])[2]};{str(coordinate[y][x])[:2]}m██\033[0m')
            elif x in coordinate[y].keys() and len(str(coordinate[y][x])) == 4:
            #点  闪烁
                coor.append(f'\033[{str(coordinate[y][x])[2]};{str(coordinate[y][x])[:2]};{str(coordinate[y][x])[3]}m██\033[0m')
            elif x in coordinate[y].keys() and coordinate[y][x] == 0:
                coor.append('██')
            elif x not in coordinate[y].keys():
            #空
                coor.append('  ')
        coor.append('\n')   #这行画好了 换行
        return coor

    for t in range(10000):
        st=tm()
        if not x_limit:   #如果没有限制 x ≥ 0 那么找到x最小值
            x_min = 0
            for y in coordinate.keys():
                if x_min > min(coordinate[y].keys()):
                    x_min = min(coordinate[y].keys())

        coor = []   #字典coordinate 转为 列表coor
        for y in range(max(coordinate.keys()),min(coordinate.keys())-1,-1):
            if y_axis:   #显示纵坐标
                coor.append(f'{y}\t')
            
            if y in coordinate.keys():   #改行有点
                if x_limit:
                    coor = xline(0)
                else:
                    coor = xline(x_min)
            elif y not in coordinate.keys():   #空行 那么换行
                coor.append('\n')
        t1.append(tm()-st)

        st = tm()
        print(''.join(coor))   #把列表coor变为一个很长的字符即最终图像并输出
        t2.append(tm()-st)
    return sum(t1)/len(t1),sum(t2)/len(t2),(sum(t2)/len(t2))/(sum(t1)/len(t1))

T = draw_c(coordinate)
print(T)
