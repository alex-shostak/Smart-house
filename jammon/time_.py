import ntptime
import utime
import log


def set_time():
    try:
        ntptime.settime()
        log.append('time: ' + get_time())
    except Exception as e:
        log.append('Main._set_time: ' + str(e))


def add_seconds(time, seconds):
    """
    adds seconds to specified time.
    :param time: 8-tuple
    :param seconds: seconds to add. !current implementation supports only values <= 60 seconds
    """
    yy, mm, dd, hh, mi, ss, mss, mcss = time
    if ss + seconds < 60:
        ss += seconds
    else:
        ss = seconds - (60 - ss)
        mi += 1
    return yy, mm, dd, hh, mi, ss, mss, mcss


def get_time():
    yy, mm, dd, hh, mi, ss, mss, mcss = utime.localtime()
    return '%s.%s.%s %s:%s:%s' % ('{0:02d}'.format(dd), '{0:02d}'.format(mm), yy, '{0:02d}'.format(hh+ 2), '{0:02d}'.format(mi),'{0:02d}'.format(ss))