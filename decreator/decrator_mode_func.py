#!/usr/bin/python
# coding:utf-8
##
# Filename: decrator_mode_func.py
# Author  : aiapple
# Date    : 2017-07-20
# Describe:
##
#############################################


def printInfo(info):  
    print unicode(info, 'utf-8')
    
    
def wearTrouser(f):
    def _f(*arg, **kwarg):
        printInfo("裤子")    
        return f(*arg, **kwarg)
    return _f
    
def wearSuit(f):
    def _f(*arg, **kwarg):
        printInfo("西服")    
        return f(*arg, **kwarg)
    return _f
    
def wearTShirt(f):
    def _f(*arg, **kwarg):
        printInfo("T恤")    
        return f(*arg, **kwarg)
    return _f

def wearCap(f):
    def _f(*arg, **kwarg):
        printInfo("帽子")    
        return f(*arg, **kwarg)
    return _f

def wearSportShoes(f):
    def _f(*arg, **kwarg):
        printInfo("运动鞋")    
        return f(*arg, **kwarg)
    return _f    

def wearLeatherShoes(f):
    def _f(*arg, **kwarg):
        printInfo("皮鞋")    
        # 注意装饰器将目标函数作为参数
        # 最后返回这个函数的结果才会达到原函数无感使用
        return f(*arg, **kwarg)
    return _f    
    
def wearedPerson(person,cloths):
	# 首先将person函数目标函数
    w = person
    for f in cloths:
    	# 将已装饰过的person继续作为目标函数进行装饰
        w=f(w)
    return w
    
    
    
#@wearTrouser    
#@wearTShirt    
def person(name):
    printInfo("装扮好的%s" % name)
    
if __name__ == '__main__':
            
    person("晓明")
    print "-----------------------"
    
    # 各类装饰器的组合
    business_wear=[wearLeatherShoes,wearSuit,wearTrouser]
    sports_wear = [wearSportShoes,wearCap,wearTShirt,wearTrouser]
    
    # 给某个人穿上装饰 返回的是闭包,这个闭包是嵌套形式,并等待调用
    weared_business_person = wearedPerson(person,business_wear)
    weared_sports_person = wearedPerson(person,sports_wear)

    weared_business_person("晓明")
    print "-----------------------"
    weared_sports_person("晓红")
    