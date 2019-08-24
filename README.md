# nebulous_coding_challenge

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
