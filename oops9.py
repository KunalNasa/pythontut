class Dad:
    Basketball = 1
class Son(Dad):
    Dance = 1
    def isdance(self):
        return f"yes I can dance {self.Dance} number of times"
class Grandson(Son):
    Dance = 6
    def isdance(self):
        return f"Yeah Baby!! I can dance  {self.Dance} number of times"

channu = Dad()
mannu = Son()
kannu = Grandson()

# print(kannu.Basketball)



class Electronic_device():
    power_source = "Alternating current or Direct Current"
    use = "Automates works and make the work very faster and efficient"
    start = "It is a kind of device which uses"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}".capitalize()


class Pocket_gadget(Electronic_device):
    power_source = "Direct current"
    addon_features = "It is portable and looks super awesome"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


class Phone(Pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}".capitalize()


computer = Electronic_device()
miband = Pocket_gadget()
redmi = Phone()

print(computer.printdetails())
print(miband.printdetails())
print(redmi.printdetails())

class electronicdevice():
    power = "AC or DC current"
    use = "Help humans to make their work easy"
    start = "start using start button"

    def usegadets(self):

       return f"This device run on {self.power} and  {self.use} and {self.start}"


class pocketgadget(electronicdevice):
    power = "AC or DC"
    addon = "it is easy to carry"

    def usegadets(self):
        return f"This device run on {self.power} and  {self.use} and {self.start} and {self.addon}"

class phone(pocketgadget):
    power = "AC"
    use = " used to communicate"

    def usegadets(self):
        return f"This device run on {self.power} and {self.use} and {self.start}"

computer = electronicdevice()
speakers = pocketgadget()
iphone = phone()

print(iphone.usegadets())
print(computer.usegadets())
print(speakers.usegadets())
