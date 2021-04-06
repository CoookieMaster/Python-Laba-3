from abc import ABC, abstractmethod

class Passenger(object):
    def __init__(self, name, mobile, luggage, sex):
        self.name = name
        self.mobile = mobile
        self.luggage = luggage
        self.sex = sex

class Luggage:
    def __init__(self, weight, size_h, size_w):
        self.weight = weight
        self.size_h = size_h
        self.size_w = size_w

class Taxi(ABC):
    def __init__(self, taxiNumber, taxiModel, driverName):
        self.taxiNumber = taxiNumber
        self.taxiModel = taxiModel
        self.driverName = driverName

    @abstractmethod
    def Compute_cost(self, passengers):
        pass

class PassengerCar(Taxi):
    def __init__(self, taxiNumber, taxiModel, driverName):
        self.taxiNumber = taxiNumber
        self.taxiModel = taxiModel
        self.driverName = driverName
    @property
    def cost(self):
        return 50
    def Compute_cost(self, passengers):
        if len(passengers) <= 4 and all_luggage < 50:
            for i in passengers:
                if i.luggage.size_h <= 40 and i.luggage.size_w <= 50:
                    continue
                else:
                    break
            print("К Вам приедет пассажирское такси, цена поездки ", self.cost * int(x))
            print('Номер машины ', self.taxiNumber, ', модель ', self.taxiModel, 'имя водителя ', self.driverName)
            check = 1
            return check
        else:
            print("Сожалеем, но подходящей легковой машины не найдено!")
            check = 2
            return check

class Truck(Taxi):
    def __init__(self, taxiNumber, taxiModel, driverName):
        self.taxiNumber = taxiNumber
        self.taxiModel = taxiModel
        self.driverName = driverName
        self.cost = 150
    def Compute_cost(self, passengers):
        if len(passengers) <= 2:
            print("К Вам приедет грузовое такси, цена поездки ", self.cost * int(x))
            print('Номер машины ', self.taxiNumber, ', модель ', self.taxiModel, 'имя водителя ', self.driverName)
        else:
            print("Сожалеем, но подходящей грузовой машины не найдено!")
if __name__ == '__main__':
    passengers = [Passenger('Петя', '89135856612', Luggage(10, 5, 50), 'м'),
                  Passenger('Маша', '89024571702', Luggage(45, 15, 45), 'ж')]
                  #Passenger('Катя', '89509712434', Luggage(20, 5, 20), 'ж'),
                  #Passenger('Вася', '89235691200', Luggage(20, 7, 15), 'м')]
    all_luggage = 0
    check = 0
    for i in passengers:
        all_luggage += i.luggage.weight
    print(all_luggage)
    pass_car = PassengerCar('ва456а', 'Nissan Note', 'Ашот Узбек')
    truck = Truck('хз902я', 'KAMAZ', 'Владимир ХорошийВодитель')
    x = input('Введите расстояние до Красноярска в км ')
    check = pass_car.Compute_cost(passengers)
    if check == 2 :
        truck.Compute_cost(passengers)
