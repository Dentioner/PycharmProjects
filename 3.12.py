#coding:utf-8
jojo = {
    'Johnathan Joestar' : '--Phantom Blood',
    'Joseph Joestar': '--Battle Tendency',
    'Kujo Jotaro': '--Stardust Crusaders',
    'Higashikata Josuke':'--Diamond is Unbreakable'

}
print jojo['Johnathan Joestar']

for jo in jojo:
    print jojo[jo]

jojo['Kujo Jotaro']= '--JOJO3'
jojo['Giorno Giovanna'] = '--Golden Wind'
del jojo['Joseph Joestar']

for jo in jojo:
    print jo,jojo[jo]

