class SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase



    def __str__(self):
        return f'Nick: {self.nickname}, Super: {self.superpower}, Health: {self.health_points}'
    
    def Hi(self):
        print(f'Name: {self.name}')

    def Hi1(self):
        print(self.health_points * 2)

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name="Clark Kent", nickname="Superman", superpower="Flight and Super Strength", health_points=100, catchphrase="Up, up, and away!")
print(str(hero))
hero.Hi()
hero.Hi1()
print(len(hero))


class Monster(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase,damage,fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    

    def her(self):
        print(self.health_points ** 2)
        self.fly = True

    def her1(sel):
        print('True in the True_phars')

hero1 = Monster(name="Rockman",nickname= "Earthshaker", superpower="Geokinesis", health_points=120, catchphrase="Earth beneath me!", damage=60)
hero1.her()
hero1.her1()


class Villian(Monster):
    people='monster'


    def gen_x(self):
        pass

    def crit(self):
        print(self.damage ** 2)
    


hero2 = Villian(name="evil guy",nickname= "ЧУдище", superpower="dark magic", health_points=120, catchphrase="You cannot escape!", damage=70)
hero2.crit()


