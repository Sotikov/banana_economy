#!/usr/bin/env python3

def simple_interest(period, interest, amount_of_money):
    # period - the amount of time for which money is invested
    # interest - the interest rate at which money is invested
    # amount of money - the amount of money invested
    simple_int = (1 + interest / 100) * period * amount_of_money
    return simple_int


# TODO:
# shorten variable names
