# coding: utf-8
num = 12345.6789
print '%e'%num
print '%E'%num
print '%d'%num# %d只是取整，而不是四舍五入
print '%.2f'%num # %.2f会四舍五入
print '%+f'%num
print '%+.2f'%num
print '%g'%num #自动判断用浮点数还是科学计数
print '%g'%123456789.123456789
print '%G'%123456789.123456789



