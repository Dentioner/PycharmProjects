# coding: utf-8
import my_module
tem = raw_input('多少摄氏度？')
tem = float(tem)
f = my_module.c_to_f(tem)
print '它等于%.f°F'%f
