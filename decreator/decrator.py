#!/usr/bin/python
# coding:utf-8
##
# Filename: decrator.py
# Author  : aiapple
# Date    : 2017-07-20
# Describe: 装饰器
#			两层装饰器--目标函数可带参数,导入是不会直接运行
# 三层装饰器--装饰器可带参数
#############################################
import time
import random
'''
# 两层装饰器
def time_cost(f):
    def _f(*arg, **karg):
        start = time.clock()
        # 下面f 即是外部参数,此参数是目标函数
        a = f(*arg, **karg)
        end = time.clock()
        print f.__name__, "run cost time is ", end - start
        return a
    return _f
'''

# 三层装饰器
def time_cost(times):
    def cost(f):
        def _f(*arg, **karg):
 			mine = 1000
 			sume = 0
 			for i in range(times):
 				start = time.clock()
 				a = f(*arg, **karg)
 				end = time.clock()
 				tm = end - start
 				sume = sume + tm
 				if mine > tm:
 					mine = tm
 			argv = sume / times
 			print f.__name__, "run %s times best time is %s" % (times, mine)
 			print f.__name__, "run %s times argv time is %s" % (times, argv)

 			return a
        return _f
    return cost


@time_cost(10)
def list_comp(length):
    print "in list_comp"
    return [(x, y) for x in range(length) for y in range(length) if x * y > 25]


@time_cost(10)
def for_loop(length):
    a = []
    print "in for_loop"
    for x in range(0, length):
        for y in range(0, length):
            if x * y > 25:
                a.append((x, y))
    return a

if __name__ == '__main__':
    a = list_comp(1000)
    # import pdb; pdb.set_trace()
    print len(a)
    a = for_loop(1000)
    print len(a)