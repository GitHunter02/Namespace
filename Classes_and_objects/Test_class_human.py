class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.surname} {self.name}, мне {self.age} (лет/годков)')

    def birthday(self):
        self.age += 1
        print(f'У меня сегодня день рождения, мне теперь {self.age}')


Tim = Human('Тимур', 'Филиппов', 25)
Alan = Human('Алан', 'Филиппов', 14)
Tim.birthday()
