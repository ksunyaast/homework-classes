# Задача№1
from abc import ABC, abstractmethod


class Animal(ABC):
  """Домашнее животное"""
  type = 'Животное'
  satiety = 0 #кг
  state = 'Голодный'
  satiety_max = 5 #кг
  sound = 'Я не говорю!'

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feeding(self):
    """Кормление животного"""
    dose = int(input('Сколько корма насыпали?'))
    self.satiety += dose
    if self.satiety < self.satiety_max:
      self.weight += dose 
      print(self.name, 'не наелся, нужно покормить еще!')
    elif self.satiety >= self.satiety_max:
      self.weight += self.satiety_max
      difference = self.satiety - self.satiety_max
      self.state = 'Сытый'
      print('{} наелся! Осталось {}кг корма.'.format(self.name, difference))
    else:
      self.state = 'Сытый'
      print(self.name, 'наелся!')

  @abstractmethod
  def collect(self):
    """Сбор продукта с животного"""

  def speak(self):
    """Животное издает звук"""
    print(self.sound)


class Cow(Animal):
  """Корова"""
  type = 'Корова'
  satiety = 0 #л
  satiety_max = 20 #кг
  milk_dugs = 0 #в
  dugs_max = 4 #вымя
  sound = 'Мууу!'

  def collect(self):
    """Дойка молока"""
    dug = int(input('Сколько подоили?'))
    if self.state == 'Сытый':
      self.milk_dugs += dug
      if dug > self.dugs_max:
        print('У {} не такое большое вымя!'.format(self.name))
      elif dug == self.dugs_max:
        print('{} подоена!'.format(self.name))
      else:
        print('{} подоена не полностью, нужно подоить еще!'.format(self.name))
    else:
      print('{} нельзя доить пока не покормили!'.format(self.name))


class Goat(Cow):
  """Коза"""
  type = 'Коза'
  satiety_max = 15#кг
  dugs_max = 2 #вымя
  sound = 'Меее!'


class Sheep(Animal):
  """Овечка"""
  type = 'Овечка'
  satiety_max = 18 #кг
  all_wool = 0 #кг
  wool_max = 7 #кг
  sound = 'Беее!'
  wool_status = 'Лохматая'

  def collect(self):
    """Стрижка"""
    wool = int(input('Сколько постригли шерсти?'))
    if self.state == 'Голодный':
      self.all_wool += wool
      self.weight -= wool
      if self.wool_max <= self.all_wool:
        self.wool_status = 'Без шерсти'
        print(self.name,'пострижен полностью!')
      else:
        print(self.name,'пострижен неполностью, постригите еще!')
    else:
      print(self.name, 'нельзя стричь на полный желудок!')


class Goose(Animal):
  """Гусь"""
  type = 'Гусь'
  satiety_max = 5 #кг
  sound = 'Га Га Га!'
  eggs_status = 'Не собраны'
  eggs = 0

  def collect(self):
    """Сборка яиц"""
    found_eggs = int(input('Сколько собрали яиц?'))
    if self.eggs_status == 'Не собраны':
      self.eggs += found_eggs
      if self.eggs == 0:
        print('Сегодня у {} яиц нет!'.format(self.name))
      else:
        self.eggs_status = 'Собраны'
        print('У {} собрано {} шт. яиц!'.format(self.name, self.eggs))
    else:
      print ('Уже собрали')


class Chicken(Goose):
  """Курица"""
  type = 'Курица'
  satiety_max = 3 #кг
  sound = 'Ко Ко Ко!'


class Duck(Goose):
  """Утка"""
  type = 'Гусь'
  satiety_max = 4 #кг
  sound = 'Кря Кря Кря!'

# Задача№2
animals = [Goose('Серый', 3), Goose('Белый', 3.5), Cow('Манька', 450), Sheep('Барашек', 50), Sheep('Кудрявый', 75),
Chicken('Ко-Ко', 0.7), Chicken('Кукареку', 0.85), Goat('Рога', 55), Goat('Копыта', 63), Duck('Кряква', 1.5)]


def routine():
  """Рутинные дела: кормление и сбор материала"""
  for animal in animals:
    print(animal.type + ': ' + animal.name)
    animal.feeding()
    animal.collect()
    print()

routine()

# Задача№3
animal_list = list()
for animal in animals:
  animal_list.append(animal.__dict__)


def sum_weight(animal_list):
  """Определение общего веса всех животных"""
  sum_weight = 0
  for animal in animal_list:
    sum_weight += animal['weight']
  print('Вес всех животных = {}кг.'.format(round(sum_weight, 2)))


def heaviest_weight(animal_list):
  animal_list.sort(key=lambda anml: anml['weight'])
  print('Самое тяжелое животное - {}, с весом {}кг.'.format(animal_list[-1]['name'], animal_list[-1]['weight']))

sum_weight(animal_list)
heaviest_weight(animal_list)