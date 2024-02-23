class Tesla:

    def __init__(self, maket,yeart,colort,costx,VIN) :
        self.make = maket
        self.year = yeart
        self.color = colort
        self.cost = costx
        self.autopilot = False
        self.VIN = VIN
    numVehicles = 0
    numVehiclesteslas = 0
    numVehiclesnontesla = 0
    TeslatononTeslaratio = numVehiclesteslas/(numVehiclesnontesla +1 )
    Vinlist =[]
    current_inv_value = 0
    def sellTesla(self,maket,costx):
        print("cost")
        self.cost += costx
        print("make")
        self.maket = maket
        Tesla.current_inv_value += costx
        Tesla.numVehicles=-1
        Tesla.numVehiclesteslas =-1
        Tesla.Vinlist.remove(input("Insert  VIN" ))



    def buycarTesla(self,maket,costx):
        import random
        print("cost")
        self.cost += costx
        print("make")
        self.maket = maket
        Tesla.numVehicles =+1
        Tesla.numVehiclesteslas =+1
        Tesla.current_inv_value =-costx
        self.Vin =Tesla.Vinlist.append(random.randint(11111111111,999999999999999999))
        return self.Vin

    def buyNonTesla(self,maket,Costx):
        import random
        print("cost")
        self.cost += Costx
        print("make")
        self.make =maket
        Tesla.numVehiclesnontesla =+1
        Tesla.numVehiclestes=+1
        self.Vin = Tesla.Vinlist.append(random.randint(11111111111, 999999999999999999))
        return self.Vin


    def sellnonTesla(self,maket,costx):

        print("cost")
        self.Cost =costx
        print("make")
        self.make =maket
        Tesla.Vinlist.remove(input("Enter VIN"))
    def AddAutoPiolit(self):
        self.autopilot = True

    def PaintCar(self):
        self.colort =()

    def Menu(self):
        print("------------------------Welcome to Tesla Rochester inventory system Ver 1.0-----------------------------")

        print("Options:"
              "(1) Sell Tesla"
              "(2) Add car to inventory(tesla)"
              "(3) Current inventory Count(Tesla only)"
              "(4) Current inventory count(all vehicles)"
              "(5) Add car to inventory (non Tesla)"
              "(6) Exit")
        menu = {'1': "Sell Tesla", '2': "Add car to inventory(tesla)", '3': "Current inventory Count(Tesla only)",
                '4': "Current inventory count(all vehicles)", '5': "Add car to inventory(Non Tesla) ","6":"Exit"}
        while True:
            options = menu.keys()
            for entry in options:
                print(entry, menu[entry])

            selection = input("Please Select:")
            if selection == '1':
                Tesla.sellTesla(Tesla.year, input("make"), input("vin"))
             elif selection == '2':
                Tesla.buycarTesla(self, input("make"),input("cost"))
            elif selection == '3':
                print(Tesla.numVehiclesteslas)
                print(Tesla.current_inv_value)
            elif selection == '4':
                print(Tesla.numVehicles)
                print(Tesla.TeslatononTeslaratio)
            elif selection == '5':
                Tesla.buyNonTesla(self, input("make"),input("cost"))
            elif selection == '6':
                print("bye bye")
                break
            else:
                print("Unknown Option Selected!")




class S(Tesla):
        def __init__(self, maket, yeart, colort, costx):
            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self,maket,yeart,colort,costx,"Models")

class Three(Tesla):
        def __init__(self, maket, yeart, colort, costx):
            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self, maket, yeart, colort, costx, "Model3")

class X(Tesla):
        def __init__(self, maket, yeart, colort, costx):
            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self, maket, yeart, colort, costx, "ModelX")

class Y(Tesla):
        def __init__(self, maket, yeart, colort, costx):
            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self, maket, yeart, colort, costx, "ModelY")

class Roadster(Tesla):
        def __init__(self, maket, yeart, colort, costx):
            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self, maket, yeart, colort, costx, "ModelRoad")

class Energy(Tesla):
        def __init__(self, maket, yeart, colort, costx):

            self.make = maket
            self.year = yeart
            self.color = colort
            self.cost = costx
            self.autopilot = False
            Tesla.__init__(self, maket, yeart, colort, costx, "ModelNRG")
Tesla.Menu(1)
