#coding: utf-8
import re
text = 'site sea sue sweet see case sse ssee loses'
n = text.split()
print(n)
for m in n:
    j =re.findall(r'\b[Ss].*e\b',m)
    if j != []:
        print(j)


