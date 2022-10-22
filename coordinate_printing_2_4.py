#坐标-图 v2.4   10/16/2022

def draw_c(coordinate,spot='██',space='  ',y_axis = True,x_limit = False,int_color = True):
    '''支持24色彩色输出 坐标格式为coordinate={y:{x:color}}
    color应为3或4位integer 前两位表示颜色 第三位为 暗/默认/高亮 第四位可选为闪烁
         或为如 '\033[1;36;5m██\033[0m' 的格式
    
    spot 为表示点的字符 默认为██
    space 为表示空的字符 默认为  (两个空格)
    y_axis 默认为False 不显示纵坐标 0或False为不显示 1或True为显示
    x_limit 默认为True 不限制
    int_color 默认为True 把int颜色改为包含 颜色 点(默认██) 空(默认  ) 的字符串   建议保持默认
    '''
    def xline(start_value):
        '''用来把单行的颜色/空添加到列表coor里面用的'''
        for x in range(start_value,max(coordinate[y].keys())+1):
            if x in coordinate[y].keys():   
                coor.append(coordinate[y][x])
            else:   
                coor.append(space)
        coor.append('\n')
        return coor

    if int_color and type(tuple(tuple(coordinate.values())[0].values())[0]) == int:   #把int颜色改为包含 颜色 点(默认██) 空(默认  ) 的字符串   建议保持默认开启
        for y in coordinate.keys():
            for x in coordinate[y].keys():
                color = str(coordinate[y][x])   # str 颜色
                if len(color) == 4:
                    coordinate[y][x] = f'\033[{color[2]};{color[:2]};{color[3]}m{spot}\033[0m'
                else:
                    coordinate[y][x] = f'\033[{color[2]};{color[:2]}m{spot}\033[0m'

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
        elif y not in coordinate.keys():    
            coor.append('\n')
        
    print(''.join(coor))   #把列表coor变为一个很长的字符即最终图像并输出


if __name__ == '__main__':
    #介绍
    print('坐标-图 v2.4')
    print('1 修复了颜色的bug')
    print('2 对于重复的坐标有小幅性能提升')
    print('\n对于部分重复的坐标(一部分颜色是数字 一部分为字符串)会有bug 会报错')

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
        5:{0:321,1:301,2:300,3:321,4:320,5:300,6:301,7:321,-1:370},
        4:{0:321,1:320,2:321,3:301,4:301,5:371,6:320,7:321},
        3:{0:370,1:320,2:301,3:300,4:300,5:301,6:321,7:371},
        2:{0:371,1:320,2:300,3:300,4:300,5:300,6:320,7:321,9:361},
        1:{0:321,1:321,2:300,3:321,4:370,5:300,6:320,7:321},
        -3:{0:300,1:310,2:320,3:330,4:340,5:350,6:360,7:370},
        -4:{0:301,1:311,2:321,3:331,4:341,5:351,6:361,7:371},
        -2:{0:302,1:312,2:322,3:332,4:342,5:352,6:362,7:372},
        -6:{0:3005,1:3105,2:3205,3:3305,4:3405,5:3505,6:3605,7:3705},

    }


    draw_c(coordinate,)