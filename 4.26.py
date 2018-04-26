# coding: utf-8
# print 'abc\txyz'
# print 'abcd\txyz'
# print 'abcde\txyz'
# print 'abcdef\txyz'
# print 'abcdefg\txyz'
# print 'abcdefgh\txyz'
# print 'abcdefghi\txyz'
# 注意每行输出的时候，abc与xyz的间距的变化
# 制表符的位置是固定的，可见书上的例子

print 'Number \tSquare \tCube'
for i in range(1, 11):
    print i, '\t', i**2, '\t', i**3
