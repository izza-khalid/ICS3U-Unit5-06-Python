#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: Dec 2019
# This program uses a function by reference


def round_number(new_num):
    # function finds new number

    new_num[0] = new_num[0] * 10**new_num[1]
    new_num[0] = new_num[0] + 0.5
    new_num[0] = int(new_num[0]) / 10**new_num[1]


def main():
    # this function gets a decimal number and calls the round_number function

    number_list = []
    # input
    print("Enter a decimal number to round it off")
    decimal = float(input("Enter a number with decimal: "))
    round_off = int(input("How many decimal places you want to round off: "))

    number_list.append(decimal)
    number_list.append(round_off)
    round_number(number_list)

    # output
    print(number_list[0])


if __name__ == "__main__":
    main()
