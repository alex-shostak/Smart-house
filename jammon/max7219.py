from micropython import const
import framebuf

_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)


class Matrix8x8:
    def __init__(self, spi, cs, num):
        self.spi = spi
        self.cs = cs
        self.cs.init(cs.OUT, True)
        self.buffer = bytearray(8 * num)
        self.num = num
        fb = framebuf.FrameBuffer(self.buffer, 8 * num, 8, framebuf.MONO_HLSB)
        self.framebuf = fb
        self.fill = fb.fill
        self.pixel = fb.pixel
        self.hline = fb.hline
        self.vline = fb.vline
        self.line = fb.line
        self.rect = fb.rect
        self.fill_rect = fb.fill_rect
        self.text = fb.text
        self.scroll = fb.scroll
        self.blit = fb.blit
        self.init()

    def _write(self, command, data):
        self.cs(0)
        for m in range(self.num):
            self.spi.write(bytearray([command, data]))
        self.cs(1)

    def init(self):
        for command, data in (
                (_SHUTDOWN, 0),
                (_DISPLAYTEST, 0),
                (_SCANLIMIT, 7),
                (_DECODEMODE, 0),
                (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def show(self):
        for y in range(8):
            self.cs(0)
            for m in range(self.num):
                self.spi.write(bytearray([_DIGIT0 + y, self.buffer[(y * self.num) + m]]))
            self.cs(1)

    def show_num(self, num, side, clear=False):
        if clear:
            self.fill(0)

        pixels = None
        indent = 0
        if num == 0:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (3, 3), (1, 4), (3, 4), (1, 5), (2, 5),
                      (3, 5)]
        elif num == 1:
            indent = 0 if side == 'l' else 3
            pixels = [(2, 2), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
        elif num == 2:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (3, 2), (1, 3), (2, 3), (3, 3), (1, 4), (1, 5), (2, 5), (3, 5)]
        elif num == 3:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (3, 2), (1, 3), (2, 3), (3, 3), (3, 4), (1, 5), (2, 5), (3, 5)]
        elif num == 4:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (1, 2), (3, 1), (3, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5)]
        elif num == 5:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (1, 5), (2, 5), (3, 5)]
        elif num == 6:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (2, 3), (3, 3), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5)]
        elif num == 7:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (3, 2), (2, 3), (2, 4), (2, 5)]
        elif num == 8:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (2, 3), (3, 3), (1, 4), (3, 4), (1, 5), (2, 5),
                      (3, 5)]
        elif num == 9:
            indent = 0 if side == 'l' else 4
            pixels = [(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (2, 3), (3, 3), (3, 4), (1, 5), (2, 5), (3, 5)]
        self.pixels(pixels, indent)
        self.show()

    def pixels(self, pixels, indent):
        for p in pixels:
            self.pixel(p[0] + indent, p[1], 1)
