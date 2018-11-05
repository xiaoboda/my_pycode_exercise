# 我的第一个高阶函数
def my_add(x, y, f)
return f(x) + f(y)

# 示例解释
my_add(-5, 6, abs)
x = -5
y = 6
f =abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
