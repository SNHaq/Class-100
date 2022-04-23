class Car(object):
    def __init__(self, model, color, company, speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def changeGear(self):
        print("gear changed")
        
audi = Car("A5", "black", "Audi", 80)
print(audi.start())
print(audi.changeGear())
print(audi.accelerate())
print(audi.stop())