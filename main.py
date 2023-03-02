data = ['mouse','keyboard', 'monitor', 'bottle']

data = [i.upper() for i in data ]

data2 = [True,False,True,False,True,False,True,False,True,False,True,False]
dataBits = [1 if b == True else 0 for b in data2]

gua = 'HaloNamaGuaRidho'
gua = ''.join(
    [i if i.islower() else ' '+ i for i in gua]
    )
print(data2)
print(dataBits)
print(gua)
