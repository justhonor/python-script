#!/usr/bin/python
# coding:utf-8
##
# Filename: closure.py
# Author  : aiapple
# Date    : 2017-07-18
# Describe:
##
#############################################

origin = [0,0]    # 坐标系统原点
legal_x = [0,50]  # x轴方向的合法坐标
legal_y = [0,50]  # y轴方向的合法坐标

def create(pos):
    def player(direction,step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等 
        # 然后还要对新生成的x，y坐标的合法性进行判断处理
        new_x = pos[0] + direction[0]*step
        new_y = pos[1] + direction[1]*step

        pos[0] = new_x
        pos[1] = new_y

        # 使用下面语句会报错,因为上面pos[0],已经使用列LEGB中E,默认pos是外部变量
        # 此时再想定义内部pos,会报错 UnboundLocalError: local variable 'pos' referenced before assignment
        #pos = [new_x,new_y]
        return pos
    return player

# 注意create(origin)是不行的,origin会和POS使用同一地址
# origin[:] --> copy.copy(origin) 
#player1 = create(origin)
player1 = create(origin[:])

print "向x轴正方向移动10步:",player1([1,0],10)   
print "向y轴正方向移动20步:",player1([0,1],20)   
print "向x轴负方向移动10步:",player1([-1,0],10)

print "origin:",origin

player2 = create(origin[:])

print "向y轴正方向移动10步:",player2([0,1],10)   
print "向x轴正方向移动20步:",player2([1,0],20)   
print "向x轴负方向移动10步:",player2([-1,0],10)
