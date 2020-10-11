class Goose:
# здесь, под первым по очереди классом, я расписал комментарии, которые актуальны для каждого класса ниже.
# задаем аттрибуты класса
# некоторые атрибуты из этого класса схожи с атрибутами других классов
    weight = 0 # это атрибут веса для методов (функций)
    weight_special_task_2 = 0 # это атрибут веса ТОЛЬКО для задания № 1.2
    egg = 0
    voice = '' # банально, чтобы воплотить различие голосов, я буду выводить разные тексты
    eggs_counter = 0
# и еще для задания № 1.2 задаем атрибут имени
    name = ''
# пишем все методы таким образом, чтобы при вызове не было обязательных аргументов. Чтобы все было уже по умолчанию
    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_goose='Внимание! Я гусь, я говорю на гусином языке!'):
        self.voice = voice_of_goose
        print(self.voice)
# прописываем экземпляры
gray_goose = Goose()
white_goose = Goose()

# Проверяем работоспособность методов
# gray_goose.collect_eggs()

# далее прописываем алгоритм выявления самого толстого животного в классе.
# для этого нам нужно все атрибуты и прочее перевести в переменные, чтоб можно было писать циклы, у.к. и тд
# все это я делаю, чтобы создать хоть какое-то подобие автоматизации процесса
gray_goose.name = 'Gray_goose'
value_1 = gray_goose.name
gray_goose.weight_special_task_2 = 22
attr_1 = gray_goose.weight_special_task_2
white_goose.name = 'White_goose'
value_2 = white_goose.name
white_goose.weight_special_task_2 = 33
attr_2 = white_goose.weight_special_task_2

list_attr = [attr_1, attr_2]
list_values = [value_1, value_2]
t = zip(list_values, list_attr)
tt = dict(t)

max = 0
for name, value in tt.items():
    if value > max:
        max = value
        nickname = name
print(f'Среди {Goose} самый тяжелый у нас - {nickname}. Общий же вес всех животных этого класса составляет {sum(list_attr)} единиц.')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Cow:
    milk_volume = 0
    weight = 0
    weight_special_task_2 = 0
    voice = ''
    milk_counter = 0

    name = ''

    def collect_milk(self, milk_volume = 1):
        self.milk_counter += milk_volume
        print(self.milk_counter)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_cow='Внимание! Я корова, и вот я произношу мууу!'):
        self.voice = voice_of_cow
        print(self.voice)

manka = Cow()

# проверка кода
# manka.collect_milk()

manka.name = 'Manka'
manka.weight_special_task_2 = 15
single_weight = manka.weight_special_task_2
print(f'Ввиду отсутствия конкурентов, {manka.name} - тяжелейшее животное в {Cow}. Вес равен {single_weight} единиц.')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Sheep:
    weight = 0
    weight_special_task_2 = 0
    haircut_level = 0
    voice = ''

    name = ''

    def cut(self, haircut = 1):
        self.haircut_level += haircut
        print(self.haircut_level)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_sheep='Внимание! Я овен, и вот я произношу мееее!'):
        self.voice = voice_of_sheep
        print(self.voice)

curly = Sheep()
lamb = Sheep()

# проверка кода
# lamb.distinguish_by_voices()

curly.name = 'Curly'
value_1 = curly.name
curly.weight_special_task_2 = 44
attr_1 = curly.weight_special_task_2
lamb.name = 'Lamb'
value_2 = lamb.name
lamb.weight_special_task_2 = 49
attr_2 = lamb.weight_special_task_2

list_attr = [attr_1, attr_2]
list_values = [value_1, value_2]
t = zip(list_values, list_attr)
tt = dict(t)

max = 0
for name, value in tt.items():
    if value > max:
        max = value
        nickname = name
print(f'Среди {Sheep} самый тяжелый у нас - {nickname}. Общий же вес всех животных этого класса составляет {sum(list_attr)} единиц.')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Chicken:
    weight = 0
    weight_special_task_2 = 0
    egg = 0
    voice = ''
    eggs_counter = 0

    name = ''

    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_chicken='Внимание! Я курица, и вот я произношу кукареку!'):
        self.voice = voice_of_chicken
        print(self.voice)

ko_ko = Chicken()
kuka_re_ku = Chicken()

# проверка кода
# kuka_re_ku.collect_eggs()

ko_ko.name = 'Ko_ko'
value_1 = ko_ko.name
ko_ko.weight_special_task_2 = 50
attr_1 = ko_ko.weight_special_task_2
kuka_re_ku.name = 'Kuka_re_ku'
value_2 = kuka_re_ku.name
kuka_re_ku.weight_special_task_2 = 51
attr_2 = kuka_re_ku.weight_special_task_2

list_attr = [attr_1, attr_2]
list_values = [value_1, value_2]
t = zip(list_values, list_attr)
tt = dict(t)

max = 0
for name, value in tt.items():
    if value > max:
        max = value
        nickname = name
print(f'Среди {Chicken} самый тяжелый у нас - {nickname}. Общий же вес всех животных этого класса составляет {sum(list_attr)} единиц.')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Goats:
    milk_volume = 0
    weight = 0
    weight_special_task_2 = 0
    voice = ''
    milk_counter = 0

    name = ''

    def collect_milk(self, milk_volume = 1):
        self.milk_counter += milk_volume
        print(self.milk_counter)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_goat='Внимание! Я козел, и вот я говорю на козьем языке!'):
        self.voice = voice_of_goat
        print(self.voice)

horns = Goats()
hooves = Goats()

# проверка кода
# hooves.distinguish_by_voices()

horns.name = 'Horns'
value_1 = horns.name
horns.weight_special_task_2 = 60
attr_1 = horns.weight_special_task_2
hooves.name = 'Hooves'
value_2 = hooves.name
hooves.weight_special_task_2 = 64
attr_2 = hooves.weight_special_task_2

list_attr = [attr_1, attr_2]
list_values = [value_1, value_2]
t = zip(list_values, list_attr)
tt = dict(t)

max = 0
for name, value in tt.items():
    if value > max:
        max = value
        nickname = name
print(f'Среди {Goats} самый тяжелый у нас - {nickname}. Общий же вес всех животных этого класса составляет {sum(list_attr)} единиц.')
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Duck:
    weight = 0
    weight_special_task_2 = 0
    egg = 0
    voice = ''
    eggs_counter = 0

    name = ''

    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_duck='Внимание! Я утка, и вот я произношу говорю на утином языке!'):
        self.voice = voice_of_duck
        print(self.voice)

kryakva = Duck()

# проверка кода
# kryakva.collect_eggs()

kryakva.name = 'Kryakva'
kryakva.weight_special_task_2 = 90
single_weight = kryakva.weight_special_task_2
print(f'Ввиду отсутствия конкурентов, {kryakva.name} - тяжелейшее животное в {Duck}. Вес равен {single_weight} единиц.')

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
