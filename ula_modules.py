#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b
    return comb

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b ^ c 
        carry.next = (a and b) or (b and c) or (a and c)

    return instances()

@block
def adder2bits(x, y, soma, carry):
    s0 = Signal(bool(0))
    s1 = Signal(bool(0))
    c0 = Signal(bool(0))
    c1 = Signal(bool(0))

    h1 = halfAdder(x[0], y[0], s0, c0)
    f2 = fullAdder(x[1], y[1], c0, s1, c1)
    
    @always_comb
    def comb():
        soma[0].next = s0
        soma[1].next = s1
        carry.next = c1
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
