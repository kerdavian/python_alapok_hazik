class SpaceShip:
  def __init__(self):
      self.fuel = 400
      self.passengers = ["John", "Steve", "Sam", "Danielle"]
      self.shields = True
      self.speedometer = 0
  
  def list_passengers(self):
    for name in self.passengers:
      print("Passenger: {}".format(name))
  
  def add_passenger(self, new_passenger):
    self.passengers.append(new_passenger)
    print(f"{new_passenger} was added to the ship")
  
  def travel(self, distance):
    print("Trying to travel: {}".format(distance))

    if self.fuel == 0:
      print("cant go further, tank is empty")
      return

    remain_fuel = self.fuel - distance / 2

    if remain_fuel > 0: 
      if remain_fuel <= 30:
        self.shields = False
        print('fuel is low, turning off shields...')
        
      
      self.speedometer = self.speedometer + distance
      self.fuel = self.fuel - (distance / 2)
      
    else:
      doableDistance = self.fuel * 2
      print("can only travel: ", doableDistance)
      self.speedometer = self.speedometer + doableDistance
      self.fuel = 0
    

    print(f"the SpaceShip is at: {self.speedometer}")
    print(f"the SpaceShip has: {self.fuel} fuel")



passenger_list =["John", "Steve", "Sam", "Danielle"]
mySpaceShip = SpaceShip()

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)

