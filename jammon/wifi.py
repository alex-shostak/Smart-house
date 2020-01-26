import network
import machine
import config
import log


def disable_ap():
    try:
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)
        #log.append('AP disabled')
    except Exception as e:
        #log.append('wifi.disable_ap: ' + str(e))
        raise


def connect():
    try:
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            sta_if.active(True)
            sta_if.connect(config.WiFi.SSID, config.WiFi.pwd)
            while not sta_if.isconnected():
                machine.idle()
        sta_if.ifconfig((config.WiFi.ip, config.WiFi.mask, config.WiFi.gate, '8.8.8.8'))
        #log.append('connected to WIFI')
    except Exception as e:
        #log.append('wifi.connect: ' + str(e))
        raise
