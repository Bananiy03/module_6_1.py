class Mammal(Animal):

    def eat(self, food):
        self.food = food
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{self.name} не может есть {food.name}')


class Predator(Animal):

    def eat(self, food):
        self.food = food
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
            else:
                print(f'{self.name} не стал есть {food.name}')
        else:
            print(f'{self.name} не может есть {food.name}')


class Fruit(Plant):

        def __init__(self, name):
            super(Fruit, self).__init__(name)
            self.edible = True


class Flower(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)