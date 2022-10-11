from random import randint
from copy import deepcopy
mon=0
at=0
class House:
    def __init__(self,name):
        self.citizens=[]
        self.name=name
        self.eat=0
        self.money=0
        self.feed=0
    def __str__(self):
        return f'*{self.name}*\nДомашні запаси: Money= {self.money}, Eat: {self.eat}, Feed: {self.feed}'
    def plus_human(self):
        print(ivan.name+' поселився до хати')
        self.money+=ivan.money
        self.eat+=ivan.eat
        ivan.eat=self.eat
        ivan.money=self.money
        self.citizens.append(ivan.name)
    #def plus_cats(self,name):
        #self.feed+=name.eat
        #self.feed=name.eat

class Human:
    def __init__(self,name,satiety,eat,money):
        self.name=name
        self.satiety=satiety
        self.eat=eat
        self.money=money
        self.health=100
        self.feed=15
    def __str__(self):
        return f'{self.name}, ситість: {self.satiety}, здоров\'я: {self.health}, гроші: {self.money}'
    def work(self):
        print(f'{self.name} пішов на роботу')
        self.money+=50
        self.satiety-=10
        self.health-=5
    def shopping(self):
        print(f'{self.name} пішов у магазин')
        if self.eat<=10:
            self.eat+=20
            self.money-=10
            print(f'{self.name} купив продукти!')
        if self.feed<10:
            self.feed+=15
            self.money-=5
            print(f'{self.name} купив корм!')
    def eats(self):
        print(f'{self.name} поїв')
        self.satiety+=10
        self.eat-=10
    def see_td(self):
        #if self.health<=40:
        print(f'{self.name} пішов до лікаря')
        self.health+=50
        self.money-=100
    def rest(self):
        print(f'{self.name} віддихав цілий день')
        self.satiety-=10
    def act(self):
        if self.eat<20:
            self.shopping()
        elif self.satiety<20:
            self.eats()
        elif self.money<150:
            self.work()
        elif self.health<=40:
            self.see_td()
        else: self.rest()

class Cats:
    def __init__(self ,name):
        self.name=name
        self.satiety_cat=10
        self.health_cat=100
        self.eat=10
    def __str__(self):
        return f'Кіт {self.name}, ситість: {self.satiety_cat}, здоров\'я: {self.health_cat}'
    def sleep(self):
        self.satiety_cat-=5
        self.health_cat+=10
    def catch(self):
        self.satiety_cat-=5
    def walk(self):
        self.satiety_cat-=5
        self.health_cat-=5
    def eats(self):
        self.eat-=5
        self.satiety_cat+=10
    def act(self):
        if self.satiety_cat<=10:
            if self.eat>=5:
                self.eats()
                return f'Кіт {self.name} поїв'
        else:
            numa=randint(1,20)
            if numa<=8:
                self.sleep()
                return f'Кіт {self.name}, спав цілий день'
            elif numa<=17:
                self.walk()
                return f'Кіт {self.name}, гуляв цілий день'
            else:
                self.catch()
                return f'Кіт {self.name} спіймав мишу!'

ivan=Human('Іван',30,10,40)
vasyl=Human('Vasyl',10,20,100)
murzik=Cats('Мурзік')
trap=House('Треп хата')
trap.plus_human()
for day in range(1,3):
    print(f'=====Day {day}======')
    print(murzik.act())
print(f'В {trap.name} живуть:',*trap.citizens)
#todo: дописати вхід в дім котів і зробити спосіб їх годування