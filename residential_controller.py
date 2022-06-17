from pyparsing import null_debug_action


elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1


class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        
        self.elevatorList = []
        self.callButtonList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButton(_amountOfFloors)

    def createCallButton(self, _amountOfFloors):
        buttonFloor = 1
        for i in range(_amountOfFloors):
                if i < _amountOfFloors:
                    callButton = CallButton(i, "Off", i+1, "up")
                    self.callButtonList.append(callButton)
                    i += 1
                if i > 1:
                    callButton = CallButton(i, "Off", i+1, "down")
                    self.callButtonList.append(callButton)
                    i += 1
                buttonFloor += 1


    def createElevators(self, _amountOfFloors, _amountOfElevators):
        for i in range(_amountOfElevators):
                elevator = Elevator(i+1, _amountOfFloors)
                self.elevatorList.append(elevator)
    
    def requestElevator(self, floor, direction):
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()
        return elevator  

    def findElevator(self, requestedFloor, requestedDirection):
        bestElevatorInformations = {
        "bestElevator" : None,
        "bestScore" : 5,
        "referenceGap" : 10000000
        }
        

        for elevator in self.elevatorList:
            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
                
            elif requestedFloor > elevator.currentFloor and elevator.status == "up" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                
            elif requestedFloor < elevator.currentFloor and elevator.status == "down" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                
            elif elevator.status == "idle":
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
                
            else : bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
            

        elevator = bestElevatorInformations.get("bestElevator")
        return elevator

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        if (scoreToCheck < bestElevatorInformations.get("bestScore")):
            print(scoreToCheck)
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = newElevator
            bestElevatorInformations["referenceGap"] = abs(newElevator.currentFloor - floor)
        elif (bestElevatorInformations.get("bestScore") == scoreToCheck):
            gap = abs(newElevator.currentFloor - floor)
            if bestElevatorInformations["referenceGap"] > gap:
                bestElevatorInformations["bestElevator"] = newElevator
                bestElevatorInformations["referenceGap"] = gap
        return bestElevatorInformations


class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = "idle"
        self.currentFloor = 1
        self.direction = None
        self.door = Door(_id, "closed") 
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(self, _amountOfFloors):
        buttonFloor = 1
        for i in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(i, "online", i+1)
            self.floorRequestButtonList.append(floorRequestButton)
            i += 1

    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    def move(self,):
        while self.floorRequestList != 0:
            destination = self.floorRequestList[0]
            self.status = "moving"
            if self.currentFloor < destination:
                self.direction = "up"
                self.sortFloorList()
                while self.currentFloor < destination:
                        self.currentFloor +=1
                        self.screenDisplay = self.currentFloor
            else : 
                if self.currentFloor > destination:
                    self.direction = "down"
                    self.sortFloorList()
                    while self.currentFloor > destination:
                        self.currentFloor -=1
                        self.screenDisplay = self.currentFloor
            self.status = "stopped"
            self.floorRequestList.pop()
        self.status = "idle"

    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()
        else :
            self.floorRequestList.reverse()

    def operateDoors(self):
        self.door.status = "opened"
        print("wait 5 seconds")
        if self.isOverweight == "false":
                self.door.status = "closing"
                if self.obstruction == "false":
                    self.door.status = "closed"
        else :
            while self.isOverwieight == "true":
                print("Activate overweight alarm")
        self.operateDoors()

class CallButton:
    def __init__(self, _id, _status, _floor, _direction):
        self.ID = _id
        self.status = _status
        self.floor = _floor
        self.direction = _direction


class FloorRequestButton:
    def __init__(self, _id, _status, _floor):
        self.ID = _id
        self.status = _status
        self.floor = _floor


class Door:
    def __init__(self, _id, _status):
        self.ID = _id
        self.status = _status

column = Column(1,10,2)
column.elevatorList[0].currentFloor = 2
column.elevatorList[1].currentFloor = 6

elevator = column.requestElevator(3, "up")
elevator.requestFloor(7)