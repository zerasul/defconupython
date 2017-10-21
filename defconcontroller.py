from machine import Pin



class FlashController:
    FILENAME = 'state.txt'

    
    def write_2_flash(self, data):
        file = open(self.FILENAME, "wb")
        nbytes = file.write(str(data))
        file.close()
        return nbytes

    def read_from_flash(self, nbytes):
        file = open(self.FILENAME, "rb")
        data = int(file.read(nbytes))
        file.close()
        return data



class DefconController:

    current_state = 1
    pines = {1: 16, 2: 14, 3: 12 , 4: 13, 5: 15}
    pinactual=Pin(16, Pin.OUT)
    def __init__(self, state):
        self.current_state = state
        for pin in self.pines.values():
            Pin(pin,Pin.OUT).off()


    def changestate(self, state):
        if state < 0 or state > 5:
            raise Exception('Invalid State')
        self.pinactual.off()
        self.current_state = state
        self.pinactual=Pin(self.pines[self.current_state],Pin.OUT)
        self.pinactual.on()

   
    def get_current_state(self):
        return self.current_state


pass