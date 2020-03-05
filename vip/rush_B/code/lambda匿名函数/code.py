"""lamdba匿名函数
特点我们使用一行代码可以是实现def自定义函数的效果
一般用于使用一次不重复使用的定义函数
"""


(lambda x,y,z : print(x+y+z))(1,2,3)
#lambda 参数1，参数2，参数3 : 表达式

# 传入多个参数

(lambda *args : print(args))(2,3)

"""lambda一般用于map() filter()"""

list1={1,2,3,4,5,6,7,8,9,10}

print(list(map(lambda x : x%2,list1))) 

#map() 将列表的每一值，都拿去执行函数

print(list(filter(lambda x : x%2==0,list1)))

# filter() 用于筛选，将满足条件的筛选出来
