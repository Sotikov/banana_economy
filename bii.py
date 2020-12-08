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


def differentiated_loan_payment(amount_of_money,
                                period,
                                interest):
    # period - the amount of time for which money is invested
    # interest - the interest rate at which money is invested
    # amount_of_money - the amount of money invested
    arr = []
    mp_cnt = period * 12
    rest = amount_of_money
    mp_real = amount_of_money / (period * 12.0)
    while mp_cnt != 0:
        mp = mp_real + (rest * interest / 1200)
        arr.append(round(mp, 2))
        rest = rest - mp_real
        mp_cnt = mp_cnt - 1
    return arr, round(sum(arr), 2)


def annuity_loan_payments(amount_of_money,
                          period,
                          interest):
    mp_cnt = period * 12
    r = interest / 1200.0
    ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
    mp = amount_of_money * ak
    total = mp * mp_cnt
    return round(mp, 2), round(total, 2)

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
