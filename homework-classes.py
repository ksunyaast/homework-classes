# Задача№1
class animal(object):
  """Домашнее животное"""
  satiety = 0 #кг
  state = 'Голодный'

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def feeding(self, dose):
    """Кормление животного"""
    self.satiety += dose
    self.weight += dose 
    if self.satiety < self.satiety_max:
      print(self.name, 'не наелся, нужно покормить еще!')
    elif self.satiety > self.satiety_max:
      difference = self.satiety - self.satiety_max
      self.state = 'Сытый'
      print('{} наелся! Осталось {}кг корма.'.format(self.name, difference))
    else:
      self.state = 'Сытый'
      print(self.name, 'наелся!')

  def speak(self):
    print(self.sound)

class cow(animal):
  """Корова"""
  satiety = 0 #л
  satiety_max = 20 #кг
  milk_dugs = 0 #в
  dugs_max = 4 #вымя
  sound = 'Мууу!'

  def milk(self, dug):
    """Дойка молока"""
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

class goat(cow):
  """Коза"""
  satiety_max = 15#кг
  dugs_max = 2 #вымя
  sound = 'Меее!'

class sheep(animal):
  """Овечка"""
  satiety_max = 18 #кг
  all_wool = 0 #кг
  wool_max = 7 #кг
  sound = 'Беее!'
  wool_status = 'Лохматая'

  def cut(self, wool):
    """Стрижка"""
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

class goose(animal):
  """Гусь"""
  satiety_max = 5 #кг
  sound = 'Га Га Га!'
  eggs_status = 'Не собраны'
  eggs = 0

  def pick_up_eggs(self, found_eggs):
    """Сборка яиц"""
    if self.eggs_status == 'Не собраны':
      self.eggs += found_eggs
      if self.eggs == 0:
        print('Сегодня у {} яиц нет!'.format(self.name))
      else:
        self.eggs_status = 'Собраны'
        print('У {} собрано {} шт. яиц!'.format(self.name, self.eggs))
    else:
      print ('Уже собрали')

class chicken(goose):
  """Курица"""
  satiety_max = 3 #кг
  sound = 'Ко Ко Ко!'

class duck(goose):
  """Утка"""
  satiety_max = 4 #кг
  sound = 'Кря Кря Кря!'

# Задача№2
goose_1 = goose('Серый', 3)
goose_2 = goose('Белый', 3.5)
cow_1 = cow('Манька', 450)
sheep_1 = sheep('Барашек', 50)
sheep_2 = sheep('Кудрявый', 75)
chicken_1 = chicken('Ко-Ко', 0.7)
chicken_2 = chicken('Кукареку', 0.85)
goat_1 = goat('Рога', 55)
goat_2 = goat('Копыта', 63)
duck_1 = duck('Кряква', 1.5)

goose_1.feeding(5)
goose_2.feeding(2)
cow_1.feeding(30)
sheep_1.feeding(9)
sheep_2.feeding(25)
chicken_1.feeding(2)
chicken_2.feeding(4)
goat_1.feeding(20)
goat_2.feeding(9)
duck_1.feeding(4)
print('')
goose_1.pick_up_eggs(6)
goose_2.pick_up_eggs(3)
cow_1.milk(4)
sheep_1.cut(6)
sheep_2.cut(8)
chicken_1.pick_up_eggs(1)
chicken_2.pick_up_eggs(0)
goat_1.milk(1)
goat_2.milk(2)
duck_1.pick_up_eggs(3)

# Задача№3
animal_list = [goose_1.__dict__, goose_2.__dict__, cow_1.__dict__, sheep_1.__dict__, sheep_2.__dict__, chicken_1.__dict__, chicken_2.__dict__, goat_1.__dict__, goat_2.__dict__, duck_1.__dict__]

def sum_weight(animal_list):
  """Определение общего веса всех животных"""
  sum_weight = 0
  for animal in animal_list:
    sum_weight += animal['weight']
  print('Вес всех животных = {}кг.'.format(round(sum_weight, 2)))

def heaviest_weight(animal_list):
  weight_list = list()
  for animal in animal_list:
    weight_list.append(animal['weight'])
  sorted(weight_list)
  for animal in animal_list:
    if animal['weight'] == sorted(weight_list)[-1]:
      print('Самое тяжелое животное - {}, с весом {}кг.'.format(animal['name'], animal['weight']))
      break
  else:
    print('Животного с таким весом нет!')
print('')
sum_weight(animal_list)
heaviest_weight(animal_list)