#!/bin/python3

import sys

def meal_cost_calculator(base_cost):
        tip_decimal = (12*(20/100))
        tax_decimal = (12*(8/100))
        total_cost = base_cost + tip_decimal + tax_decimal
        print("Your total meal cost is {} dollars".format(round(total_cost)))

meal_cost_calculator(12)

