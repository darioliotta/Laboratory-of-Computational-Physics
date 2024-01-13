ciao = ()
salute = 'cia'

for i in range(10):
    s = salute + 'o'
    salute = s
    ciao += (salute,)
    
print(ciao)