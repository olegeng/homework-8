from random import randint
from copy import deepcopy, copy
def game_on_off(gam):
    if game==False:
        return False
def chislo():
    global cop
    numb=''
    for _z in range(0,4):
        if _z==1:
            rand=randint(1,9)
            numb+=str(rand)
        else:
            rand=randint(0,9)
            while str(rand) in numb:
               rand=randint(0,9)
            numb+=str(rand)
    return str(numb)
cop=copy(chislo())
def proverka(nomer, baza=str(cop)):
    global vivod
    bull=0
    cow=0
    for num,z in enumerate(str(nomer)):
        if baza[num]==z:
            bull+=1
        elif z in baza:
            cow+=1
    vivod={'Bull':bull,
           'Cow':cow}
    if bull==4:
        print('Правильно! Ви відгадали число.')
        return True
    elif bull<4:
        print(vivod)
        return vivod