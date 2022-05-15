from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("----------")

    limo_car = Car(100)
    limo_car.add_fuel(20)
    limo_car.drive(115)
    print("fuel =", limo_car.fuel)
    print("odo =", limo_car.odometer)
    print(limo_car)
    print("Car {}, {}".format(limo_car.fuel, limo_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo_car))

main()
