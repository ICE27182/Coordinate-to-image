# coding: UTF-8

# coordinate_image_3_0   10/17/2022 - 10/22/2022

class CoordinateImageC:
    def __init__(self,coordinate,state=None,y_axis=False,xy_range=None,spot='██',space='\033[0m  '):
        '''
        coordinate should be a dictionary in the form of {y:{x:val,etc.},etc.}
        y & x should be int
        y's value can be an empty dict like {1:{}} but it can only be a dict
        x's value should be an int or a string
            int: 361   340   331   36147   31043
                361 -> \\033[1;36m   36147 -> \\033[1;36;47m
            str: '332/\\'   '36147||'
                '332/\\' -> \\033[2;33m/\\   '36147||' -> \\033[1;36;47m||
        
        state   -2 - 7str   -1 - 5str    0 - no_need_for_trans   1 - 3int   2 - 5int   31 - match

        xy_range should be in form like (range(1,8),range(6,-4,-1)), which is a tuple;
        The former one is x_range, which should be in the form of range(x_min,x_max+1);
        The latter one is y_range, which should be in the form of range(y_max,y_min-1,-1).
        '''
        if state == None:
            for y in coordinate.keys():
                if len(coordinate[y]) >= 1:   # To ignore empty line
                    for x in coordinate[y].keys():
                        example = coordinate[y][x]
                        if type(example) == int:
                            if example in range(300,373):
                                state = 1
                            elif example in range(30040,37248):
                                state = 2
                        elif type(example) == str:
                            if example[0] == '\x1b':
                                state = 0
                            elif len(example) == 5:
                                state = -1
                            elif len(example) == 7:
                                state = -2
                        if state != None: break
                    if state != None: break
        self.state = state
        
        self.coordinate = coordinate
        self.spot,self.space = spot,space
        self.y_axis = y_axis

        if xy_range == None:
            CoordinateImageC.xy_range(self)
        else: self.x_range,self.y_range = xy_range

    def xy_range(self):
        y_max = max(self.coordinate.keys())
        y_min = min(self.coordinate.keys())
        y_range = range(y_max, y_min-1, -1)
        x_min = min(self.coordinate[y_max].keys())
        x_max = x_min
        for y in self.coordinate.keys():
            for x in self.coordinate[y].keys():
                if x > x_max:
                    x_max = x
                elif x < x_min:
                    x_min = x
        x_range = range(x_min, x_max+1)
        self.x_range,self.y_range = x_range,y_range


    def init_color(self):
        '''
        To turn color codes like 361 or 36147 or '361██' or '36147██' into the form like'\033[1;36;47m██'
        '''
        if self.state == 1:
            for y in self.coordinate.keys():
                for x in self.coordinate[y].keys():
                    str_color = self.coordinate[y][x]
                    self.coordinate[y][x] = f'\033[{str_color%10};{str_color//10}m{self.spot}'
        elif self.state == 2:
            for y in self.coordinate.keys():
                for x in self.coordinate[y].keys():
                    str_color = self.coordinate[y][x]
                    self.coordinate[y][x] = f'\033[{str_color//100%10};{str_color//1000};{str_color%100}m{self.spot}'
        elif self.state == -1:
            for y in self.coordinate.keys():
                for x in self.coordinate[y].keys():
                    str_color = self.coordinate[y][x]
                    self.coordinate[y][x] = f'\033[{str_color[2]};{str_color[:2]}m{str_color[-2:]}'
        elif self.state == -2:
            for y in self.coordinate.keys():
                for x in self.coordinate[y].keys():
                    str_color = self.coordinate[y][x]
                    self.coordinate[y][x] = f'\033[{str_color[2]};{str_color[:2]};{str_color[3:5]}m{str_color[-2:]}'
        
        elif self.state == 31:
            for y in self.coordinate.keys():
                for x in self.coordinate[y].keys():
                    str_color = self.coordinate[y][x]
                    if type(str_color) == int and str_color in range(300,373):
                        self.coordinate[y][x] = f'\033[{str_color%10};{str_color//10}m{self.spot}'
                    elif type(str_color) == int and str_color in range(30040,37248):
                        self.coordinate[y][x] = f'\033[{str_color//100%10};{str_color//1000};{str_color%100}m{self.spot}'
                    elif type(str_color) == str and len(str_color) == 5:
                        self.coordinate[y][x] = f'\033[{str_color[2]};{str_color[:2]}m{str_color[-2:]}'
                    elif type(str_color) == str and len(str_color) == 7:
                        self.coordinate[y][x] = f'\033[{str_color[2]};{str_color[:2]};{str_color[3:5]}m{str_color[-2:]}'

    def coordinate_text(self):
        '''
        Turn the coordinate(that has been transformed into the form like'\033[1;36;47m██')
        into a single string to print
        '''
        img = []
        for y in self.y_range:
            img.append('\033[0m\n')

            if self.y_axis:
                img.append(f'{y}\t')

            if y in self.coordinate:
                for x in self.x_range:
                    if x in self.coordinate[y].keys():
                        img.append(f'{self.coordinate[y][x]}\033[0m')
                    else:   img.append(f'{self.space}\033[0m')
            elif self.space != '\033[0m  ':
                img.append(self.space*len(self.x_range))
        self.img = ''.join(img)
    
    def draw_c(self):
        if self.state in (-2,-1,1,2,31):
            CoordinateImageC.init_color(self)
        CoordinateImageC.coordinate_text(self)
        print(self.img)


def main():
    creeper = {
    8:{0:370,1:320,2:321,3:321,4:371,5:321,6:320,7:320,9:36147},
    7:{0:320,1:321,2:320,3:321,4:320,5:321,6:320,7:370,11:'\033[1;31;44m**--/'},
    6:{0:321,1:301,2:301,3:321,4:320,5:301,6:301,7:371,-3:351},
    5:{0:321,1:301,2:300,3:321,4:320,5:300,6:301,7:321,-4:370},
    4:{0:321,1:320,2:321,3:301,4:301,5:371,6:320,7:321},
    3:{0:370,1:320,2:301,3:300,4:300,5:301,6:321,7:371},
    2:{0:371,1:320,2:300,3:300,4:300,5:300,6:320,7:321,10:361},
    1:{0:321,1:321,2:300,3:321,4:370,5:300,6:320,7:321},
    -3:{0:300,1:310,2:320,3:330,4:340,5:350,6:360,7:370},
    -4:{0:301,1:311,2:321,3:331,4:341,5:351,6:361,7:371},
    -2:{0:302,1:312,2:322,3:332,4:342,5:352,6:362,7:372},
    -5:{0:341,1:341,2:341,3:341,4:341,5:341,6:341,-1:341,},

    -6:{0:302,1:300,2:372,3:301,4:370,5:371,   6:341,-1:341},

    -7:{0:341,1:341,2:341,3:341,4:341,5:341,6:341,-1:341,},
    -8:{4:'36147/\\',6:'351||',8:'35147\\/',11:'\033[1;36;47mICE'}
    }

    creeper_face = CoordinateImageC(creeper,state=31,y_axis=True,space='U(',spot='??')
    # print(creeper_face.img)
    CoordinateImageC.draw_c(creeper_face)

if __name__ == '__main__':
    main()