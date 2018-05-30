# coding: utf-8
def ta_ban(K):
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
        # print ratio
        # print density[0]
        # print m_density[0]

        density[0] = float('%.2f' % density[0])
        m_density[0] = float('%.2f' % m_density[0])
        for j in range(7, 0, -1):
            density[j] = density[j] + m_density[j-1] - m_density[j]
            density[j] = float('%.2f' % density[j])
            m_density[j] = density[j]*(1-ratio)
            m_density[j] = float('%.2f' % m_density[j])
            # print 'j=%d'%j
            # print density[j]
            # print m_density[j]
            # print

        print '第%d次：' %i,
        print density
        # print m_density
        print
        i += 1



print 'version 1.1'
print
k = raw_input('分配系数K=？')
k = float(k)
ta_ban(k)



# coding: utf-8
def ta_ban(K):
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


        print
        i += 1


print 'version 1.1'
print
k = raw_input('分配系数K=？')
k = float(k)
ta_ban(k)
