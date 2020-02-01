import network
import machine
import config


def disable_ap():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)


def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(config.WiFi.SSID, config.WiFi.pwd)
        while not sta_if.isconnected():
            machine.idle()
    #sta_if.ifconfig((config.WiFi.ip, config.WiFi.mask, config.WiFi.gate, '8.8.8.8'))
    sta_if.ifconfig()
