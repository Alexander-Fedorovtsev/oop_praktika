from typing import List


class Trip:
    def __init__(self, distance: float, comment: str = "Просто поездка") -> None:
        self.distance = distance
        self.comment = comment


class Transport:
    def __init__(self, fuel: int, trips: List[Trip]) -> None:
        self.fuel = fuel
        self.trips = trips
        

    def add_trip(self, trip: Trip):
        """Добавляет поездку"""
        self.trips.append(trip)

    def sum_trip_distance(self) -> float:
        """Рассчитывает всю пройденную дистанцию"""
        return sum([trip.distance for trip in self.trips])

    def calc_reachable_distance(self):
        """Расчитывает оставшийся путь ТС с учетом совершенных поездок"""
        pass
        

class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12 # л/км

    def calc_reachable_distance(self) -> str:
        result = self.fuel - (self.sum_trip_distance() * self.FUEL_CONSUMPTION_CAR) // self.FUEL_CONSUMPTION_CAR
        return f'Машине осталось проехать {result} км'


class Airplanes(Transport):
    FUEL_CONSUMPTION_CAR = 200

    def calc_reachable_distance(self) -> str:
        result = self.fuel - (self.sum_trip_distance() * self.FUEL_CONSUMPTION_CAR) // self.FUEL_CONSUMPTION_CAR
        return f'Самолету осталось пролететь {result} км'


trips = [Trip(10,"Поездка1"), Trip(19.5)]

sum_distance = 0

for trip in trips:
    sum_distance += trip.distance

print(sum_distance) 

transport = Transport(100, [])
transport.calc_reachable_distance()

audi = Car(70, [
    Trip(200),
    Trip(50)
])

print(audi.calc_reachable_distance(git))