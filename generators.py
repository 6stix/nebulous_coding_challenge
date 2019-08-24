"""
This program aims to solve Nebulous' coding challenge.

The general idea of the program is to take two generators with their respective
passed-in constants, generate numbers up to a defined limit, and return/print the
number of matched numbers (when bitwise ANDed with a bit_match integer).

Date: August 23rd, 2019
"""

import time

def main():
    """
    This main function runs through the example data and compares the runtime of
    a non-memoized approach and a memoized approach.
    """
    start_a = 65
    multiplier_a = 16807

    start_b = 8921
    multiplier_b = 48271

    limit = 40000000
    divisor = 2147483647
    sixteen_bits_on = (2 ** 16) - 1

    start = time.time()
    match_count = generator_matches(start_a, multiplier_a, start_b, multiplier_b, limit, divisor, sixteen_bits_on)
    end = time.time()
    print("Number of matches:", match_count)
    print("The total elapsed time (non-memo):", end-start) # 25.81 sec

def generator_matches(start_a, multiplier_a, start_b, multiplier_b, limit, divisor, bit_match):
    """
    This function generates numbers based-on two generators with their corresponding
    variables. After calculating each of the generator's next numbers, a bitwise AND
    is performed with the bit_match number with each of the next numbers.
    """
    curr_a = start_a
    curr_b = start_b
    #matches = []
    match_count = 0
    for i in range(limit):
        curr_a = (curr_a * multiplier_a) % divisor
        least_bits_a = curr_a & bit_match

        curr_b = (curr_b * multiplier_b) % divisor
        least_bits_b = curr_b & bit_match

        if least_bits_a == least_bits_b:
            #matches.append((curr_a, curr_b)) -> example of list usage
            match_count += 1

    return match_count

if __name__ == '__main__':
    main()
