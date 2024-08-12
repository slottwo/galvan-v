from myhdl import *


@block
def clock(clk):

    @always(delay(10))  # 10 nano seconds
    def _clock():
        clk.next = not clk

    return _clock


@block
# Program Counter Selection Mux
def pc_mux(reset, pc, addr, jmp, select: bool):

    @always_comb
    def mux():
        if reset.next == ...:  # TODO: "INACTIVE_HIGH"
            if select:
                pc.next = jmp
            else:
                pc.next = addr

    return mux


@block
# Write Data Selection Mux
def write_data_mux(reset, write_data, mem_to_reg: bool, result, read_data):

    @always_comb
    def mux():
        if reset.next == ...:  # TODO: "INACTIVE_HIGH"
            if mem_to_reg:
                write_data.next = read_data
            else:
                write_data.next = result

    return mux


@block
def alu_mux(reset, im_gen, rdb, rdx, alu_src):

    @always_comb
    def mux():
        if reset.next == ...:  # TODO: "INACTIVE_HIGH"
            if alu_src:
                rdx.next = im_gen
            else:
                rdx.next = rdb

    return mux


if __name__ == "__main__":
    pass
