from json import dumps
from json import loads
import xlrd


dic = {'question': "问题", 'answer': "答案"}

js = dumps(dic, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
print(js)

# data = xlrd.open_workbook('./test.xlsx')
# table = data.sheets()[0]
# question = table.cell(0,0).value
# answer = table.cell(0,1).value
#
# print("q="+question)
# print("a="+answer)


