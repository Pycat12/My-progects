class House():
    """"Описание дома"""
    def __init__(self, street, number):
        """"Свойства дома"""
        self.street = street
        self.number = number
        self.age = 0
    def build(self):
        """"Строть дом"""
        print("Дом на улице" + self.street + "Под номером" + str(self.number) + "Построен.")
    def age_of_House(self, year):
        """"Возраст дома"""
        self.age += year
House1 = House("Заливная",85)
House2 = House("Пушкина",15)
House1.age_of_House(4)
print(House1.street)
print(House1.number)
print(House1.age)
class ProspectHouse(House):
    """Дома на проспектк"""
    def __init__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect
PrHouse = ProspectHouse("Хамонов",1)
print(PrHouse.prospect)