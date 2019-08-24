"""
This program aims to solve Nebulous' coding challenge. The instructions to the challenge
can be found here: https://docs.google.com/document/d/1eurMI2z6JIfHM9zPg4gWz5NzB8TQxOmSAE4GN_3C8co/edit

The general idea of the program is to take two generators with their respective
passed-in constants and generate numbers up to a defined limit. Each step involves
generating a number and then bitwise ANDing the number with the bit_match integer.
If, during a single step, both of the generators bitwise ANDed numbers match, the
match_count is incremented.

Note: this program is extremely easy to expand upon. For example, if a list was
desired instead of a count, one could create a list of tuples of matching generated
numbers and then return the list.

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

    start = time.time()
    match_count = generator_matches_memo(start_a, multiplier_a, start_b, multiplier_b, limit, divisor, sixteen_bits_on)
    end = time.time()
    print("Number of matches:", match_count)
    print("The total elapsed time (memoized):", end-start) # 16.41 sec

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

def generator_matches_memo(start_a, multiplier_a, start_b, multiplier_b, limit, divisor, bit_match):
    """
    This function is like the generator_matches function, but this one is memoized
    to improve upon runtime.
    """
    memo = {}

    curr_a = start_a
    curr_b = start_b
    #matches = []
    match_count = 0
    for i in range(limit):
        if curr_a not in memo:
            old_a = curr_a
            curr_a = (curr_a * multiplier_a) % divisor
            least_bits_a = curr_a & bit_match

            memo[old_a] = (curr_a, least_bits_a)

        else:
            pair = memo[curr_a]
            curr_a = pair[0]
            least_bits_a = pair[1]

        if curr_b not in memo:
            old_b = curr_b
            curr_b = (curr_b * multiplier_b) % divisor
            least_bits_b = curr_b & bit_match

            memo[old_b] = (curr_b, least_bits_b)

        else:
            pair = memo[curr_b]
            curr_b = pair[0]
            least_bits_b = pair[1]

        if least_bits_a == least_bits_b:
            #matches.append((curr_a, curr_b))
            match_count += 1

    return match_count

if __name__ == '__main__':
    main()
