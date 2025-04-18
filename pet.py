class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  
        self.energy = 5
        self.happiness = 5
        self.tricks = []  

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        print(f"{self.name}'s tricks: {', '.join(self.tricks) if self.tricks else 'No tricks yet'}")


pet = Pet("doggie")
pet.eat()
pet.sleep()
pet.play()
pet.train("sit")
pet.train("roll over")
pet.get_status()
pet.show_tricks()
