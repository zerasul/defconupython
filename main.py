import defconcontroller
import networkcontroller
import time
fcontroller = defconcontroller.FlashController()
dcontroller = defconcontroller.DefconController(1)
time.sleep(0.5)
dcontroller.changestate(2)
time.sleep(0.5)
dcontroller.changestate(3)
time.sleep(0.5)
dcontroller.changestate(4)
time.sleep(0.5)
dcontroller.changestate(5)
time.sleep(0.5)
dcontroller.changestate(fcontroller.read_from_flash(1))
print('DefconPlatino Initializated')

wcontroller = networkcontroller.WebController(fcontroller,dcontroller)
wcontroller.initServer(80)
