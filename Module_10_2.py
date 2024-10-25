import time
from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name=str, power=int, day=int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        power = 100
        days = 0
        print(f"{self.name}, на нас напали!")
        for i in range(100):
            if power > 0:
                power -= self.power
                time.sleep(1)
                days += 1
                print(f'{self.name} сражается {days} день(дня), осталось {self.power} войнов.''\n')
                if power <= 0:
                    print(f'{self.name} одержал победу, спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')