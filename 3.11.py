#coding=utf-8
d=open('d.txt')
lines= d.readlines()
print(lines)
results = []
for line in lines:
    print(line)
    data = line.split()
    print(data)
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s\t: %d\n'%(data[0],sum)
    print(result)
    results.append(result)
    print(results)
output = open('final.txt','w')
output.writelines(results)
output.close()
d.close()


