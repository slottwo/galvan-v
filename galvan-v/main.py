from myhdl import *


@block
def clock(clk):

    @always(delay(10))  # 10 nano seconds
    def _clock():
        clk.next = not clk

    return _clock


if __name__ == "__main__":
    pass
