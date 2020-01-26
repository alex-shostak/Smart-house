import ntptime
import utime
import machine


def set_time():
    utc_shift = 2
    ntptime.settime()
    tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift * 3600)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)


def add_seconds(time, seconds):
    return utime.localtime(utime.mktime(time) + seconds)