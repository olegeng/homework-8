class House:
    eat=50
    money=100
    purity=105
    def __str__(self):
            return (f'HOME: eat:{self.eat}, money:{self.money}, purity:{self.purity}')
class Wife(House):
    def __init__(self,eat=House.eat,money=House.money,purity=House.purity):
        self.eat=eat
        self.money=money
        self.purity=purity
        self.satiety=50
        self.happy=100
    def __str__(self):
        return f'WIFE:satiety:{self.satiety}, happy:{self.happy}, eat in home:{self.eat}'
    def eating(self):
        self.eat-=10
        self.satiety+=20
        return 'Eating'
    def buy_coat(self):
        self.money-=20
        self.happy+=50
        self.satiety-=5
        return'Buy Coat'
    def clean_up(self):
        self.satiety-=20
        self.happy-=20
        self.purity+=50
        return 'Clean Up'
    def shopping(self):
        self.money-=30
        self.eat+=50
        self.satiety-=5
        return 'Shopping'
    def relax(self):
        self.happy-=20
        self.satiety-=10
        return 'Relax'
    def act(self):
        try:
            if self.satiety<=20:
                return self.eating()
            elif self.eat<=20:
                return self.shopping()
            elif home.purity<=30:
                return self.clean_up()
            elif self.money>=80:
                return self.buy_coat()
            else:
                return self.relax()
        except:
            print('Error')
        finally:
            House.eat=self.eat
            House.money=self.money
            self.purity-=5
            House.purity=self.purity
class Husband(House):
    def __init__(self,eat=House.eat,money=House.money,purity=House.purity):
        self.eat=eat
        self.money=money
        self.purity=purity
        self.satiety=50
        self.happy=100
    def __str__(self):
        return (f'HUSBAND:satiety:{self.satiety}, happy:{self.happy}, eat in home:{self.eat}')
home=House()
Tereza=Wife()
Ioan=Husband()
for day in range(1,20):
    print(f'=====day {day}=====')
    print(home)
    print(Tereza,
          Tereza.act())
    home.purity-=5
    print(Tereza.act())
#todo Дописати функцію HUSBAND and Children, настроїти satiety,happy для WIFE