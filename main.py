import network,time
import machine
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if.active(True)
CONFIG_SSID = "NYX Dev"
CONFIG_PASSWORD = "0815158010"
LED_R = machine.Pin(14,machine.Pin.OUT)
LED_B = machine.Pin(33,machine.Pin.OUT)
while True:
  LED_R.value(1)
  LED_B.value(1)
  time.sleep(1)
  LED_R.value(0)
  LED_B.value(0)
  time.sleep(1)
