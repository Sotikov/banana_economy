#!/usr/bin/env python3

def simple_interest(period,
                    interest,
                    amount_of_money):
    # period - the amount of time for which money is invested
    # interest - the interest rate at which money is invested
    # amount_of_money - the amount of money invested
    simple_int = (1 + interest / 100) * period * amount_of_money
    return simple_int

def compound_interest(period,
                      replenishment_period,
                      interest,
                      amount_of_money,
                      amount_of_money_for_replenishment):
    # period - the amount of time for which money is invested
    # replenishment_period - the investment replenishment period
    # interest - the interest rate at which money is invested
    # amount_of_money - the amount of money invested
    # amount_of_money_for_replenishment - the amount of money to replenish investments
    compound_int = amount_of_money
    for i in (period / replenishment_period - 1):
        compound_int = compound_int * (1 + interest / 100) + amount_of_money_for_replenishment
    return compound_int


# TODO Visit JB Web resources:
# 11
# 12
# todo
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
