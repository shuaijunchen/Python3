age = 20
name = 'Chen'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# 对于浮点数'0.333'保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用(^)定义'__chen__'字符串长度为11
print('{0:_^9}'.format('chen'))

# 基于关键字输出'Chen wrote A byte of Python'
print('{a} wrote {b}'.format(a='Chen', b='a byte of python3'))

print('a', end=' ')
print('b', end=' ')
print('c')
