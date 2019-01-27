import ntptime
import utime
import log


def set_time():
    try:
        ntptime.settime()
        log.write('time: ' + get_time())
    except Exception as e:
        log.write('Main._set_time: ' + str(e))


def get_time():
    yy, mm, dd, hh, mi, ss, mss, mcss = utime.localtime()
    return '%s.%s.%s %s:%s:%s' % ('{0:02d}'.format(dd), '{0:02d}'.format(mm), yy, '{0:02d}'.format(hh+ 2), '{0:02d}'.format(mi),'{0:02d}'.format(ss))