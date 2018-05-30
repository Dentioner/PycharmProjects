# coding: utf-8
from __future__ import division
def ta_ban(K):
    plate = open('plate.txt', 'w')
    init_c = 100.0
    ci_shu = raw_input('分配次数=')
    ci_shu = float(ci_shu) + 1
    density = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    m_density = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    i = float(1)
    K = float(K)
    ratio = K/(K+1)

    while i < ci_shu:

        density[0] = init_c*(ratio**i)
        m_density[0] = init_c*((1-ratio)**i)

        density[0] = float('%.10f' % density[0])
        m_density[0] = float('%.10f' % m_density[0])

        for j in range(7, 0, -1):
            density[j] = density[j] + m_density[j-1] - m_density[j]
            density[j] = float('%.10f' % density[j])
            m_density[j] = density[j]*(1-ratio)
            m_density[j] = float('%.10f' % m_density[j])

        print '第%d次：' %i,
        print density[7]
        a = density[7]
        a = str(a)
        plate.write(a+'\n')

        print
        i += 1
    plate.close()

print 'version 1.2'
print
k = raw_input('分配系数K=？')
k = float(k)
ta_ban(k)
