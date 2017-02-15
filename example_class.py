class Animal:
    def __init__(self, speed):
        print('TEST!')
        self.my_speed = speed

    def print_speed(self):
##        print('TEST2222!')
        print(self.my_speed)

a = Animal(45)
a.print_speed()


messages = ['hi', 'bi' ,'Wo!!']
for x in messages:
    Animal(5)
