import defconcontroller
import networkcontroller
import time
import config
fcontroller = defconcontroller.FlashController()
dcontroller = defconcontroller.DefconController(1)
dcontroller.changestate(1)
time.sleep(0.25)
dcontroller.changestate(2)
time.sleep(0.25)
dcontroller.changestate(3)
time.sleep(0.25)
dcontroller.changestate(4)
time.sleep(0.25)
dcontroller.changestate(5)
time.sleep(0.25)
networkcontroller.Wifi_Controller.configure_Wifi(config.WIFI_ESSID, config.WIFI_PASS)
dcontroller.changestate(fcontroller.read_from_flash(1))
print('DefconPlatino Initializated')

wcontroller = networkcontroller.WebController(fcontroller,dcontroller)
wcontroller.initServer(80)
