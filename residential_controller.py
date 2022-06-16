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
        bestElevator = None
        bestScore = 5
        referenceGap = 10000000
        bestElevatorInformations = bestScore, referenceGap, bestElevator

        for elevator in self.elevatorList.forEach:
            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
                return bestElevatorInformations
            elif requestedFloor > elevator.currentFloor and elevator.status == "up" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                return bestElevatorInformations
            elif requestedFloor < elevator.currentFloor and elevator.status == "down" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
                return bestElevatorInformations
            elif elevator.status == "idle":
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
                return bestElevatorInformations
            else : bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)

            return bestElevatorInformations.bestElevator

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        if scoreToCheck < bestElevatorInformations.bestElevator:
            bestElevatorInformations.bestScore = scoreToCheck
            bestElevatorInformations.bestElevator = newElevator
            bestElevatorInformations.referenceGap = abs(newElevator.currentFloor - floor)
        elif bestElevatorInformations.bestScore == scoreToCheck:
            gap = abs(newElevator.currentFloor - floor)
            if bestElevatorInformations.referenceGap > gap:
                bestElevatorInformations.bestElevator = newElevator
                bestElevatorInformations.referenceGap = gap
        return bestElevatorInformations


class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        
        
        self.direction = None
        self.door = Door(_id, "closed") 
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

        def createFloorRequestButtons(_amountOfFloors):
            return self._amountOfFloors
            buttonFloor = 1
            for i in range(_amountOfFloors):
                self.floorRequestButton = FloorRequestButton(i+1, _buttonFloor)
                self.floorRequestButtonList.append(floorRequestButton)
                i += 1

        def requestFloor(floor):
            self.floorRequestList.append(floor)
            self.move()
            self.operateDoors()

        def move():
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
                self.floorRequestList.shift()
            self.status = "idle"

        def sortFloorList():
            if self.direction == "up":
                self.floorRequestList.sort()
            else :
                self.floorRequestList.reverse()

        def operateDoors():
            self.door.status = "opened"
            print("wait 5 seconds")
            if self.isOverweight == "false":
                    self.door.status = "closing"
                    if self.obstruction == "false":
                        self.door.status = "closed"
            else :
                while self.isOverwieight == "true":
                    print("Activate overweight alarm")
            operateDoors()

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

