import cars
def main():
    Car1 = cars.Car("20", "toyota","corolla","1993")
    # Car1.print_car()
    
    Car2 = cars.Car("40", "Mercedes Benz","Avatar","2017")
    # Car2.print_car()
    
    Car3 = cars.Car("30", "Honda","Accord","2004")
    Car4 = cars.Car("10", "Tesla","ModelT","2020")
    Car5 = cars.Car("50", "Huge","PP","2023")
    print(Car2==Car3)
    print(Car1==Car3)
    # print(str(Car1))
    print(Car2)
    # car_list = [Car1,Car2,Car3,Car4,Car5]
    # print(car_list)
    # car_list.sort()
    # print(car_list)
    # car_set = set(car_list)
    
main()