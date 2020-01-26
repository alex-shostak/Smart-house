import ntptime
import utime
import machine
import log


def set_time():
    try:
        utc_shift = 2
        ntptime.settime()
        tm = utime.localtime(utime.mktime(utime.localtime()) + utc_shift * 3600)
        tm = tm[0:3] + (0,) + tm[3:6] + (0,)
        machine.RTC().datetime(tm)
        #log.append('time: ' + get_time())
    except:
        raise
        #log.append('_set_time: ' + str(e))


def add_seconds(time, seconds):
    return utime.localtime(utime.mktime(time) + seconds)