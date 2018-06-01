# coding: utf-8
from __future__ import division


def ta_ban(K):
    plate = open('plate.txt', 'w')
    init_c = 100.0
    ci_shu = raw_input('分配次数=')
    ci_shu = float(ci_shu)
    density = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    m_density = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    i = float(0)
    K = float(K)
    ratio = K/(K+1)

    while i < ci_shu:
        density[0] = init_c*(ratio**i)
        m_density[0] = density[0]*(1-ratio)
        density[0] = float('%.10f' % density[0])
        m_density[0] = float('%.10f' % m_density[0])
        for j in range(7, 0, -1):
            density[j] = density[j] + m_density[j-1] - m_density[j]
            density[j] = float('%.10f' % density[j])
            m_density[j] = density[j]*(1-ratio)
            m_density[j] = float('%.10f' % m_density[j])


        i += 1
        density[0] = init_c*(ratio**i)
        m_density[0] = density[0]*(1-ratio)

        print '第%d次：' %i,

        print m_density[6]

        a = m_density[6]

        a = str(a)
        plate.write(a+'\n')

        # print density
        # 如果要输出一个表格的话，就把这一项注释解开，把上面那五行代码变成注释

        print

    plate.close()


print ('version 2.0')
print
k = raw_input('分配系数K=？')
k = float(k)
ta_ban(k)
