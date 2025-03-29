# Sumator from "Code: The Hidden Language of Computer Hardware and Software" by Charles Petzold
# Sum binari digits from 0000-0000 to 1111-1111 (wich 0 to 255 in decimal).
# Result can be up to 1-1111-1110, (or 510 in decimal).
#
# input: two list of 8 binary digits
# output: list with result digits


import doctest


doctest.testmod()


def half_adder(a:int, b:int) -> tuple:
    """add two binary digits a and b
    in result first element - carry digit, second - sum digit
    >>> half_adder(1, 1)
    (1, 0)
    >>> half_adder(0,1)
    (0, 1)
    """ 

    return a & b, a ^ b  # carry_out, sum_out


def adder(carry_bit, a, b):
    """
    >>> adder(0, 1, 1)
    (1, 0)
    >>> adder(1, 0, 1)
    (1, 0)
    """
    carry_out_1, sum_out_1 = half_adder(a, b)
    carry_out_2, sum_out_2 = half_adder(carry_bit, sum_out_1)
    carry_out = carry_out_1 | carry_out_2
    
    return carry_out, sum_out_2


# gpt solution for 8 bit sumator
def add_8bit(a, b):
    carry = 0
    result = []
    
    for i in range(8):  # Loop through each bit (LSB to MSB)
        carry, sum_bit = adder(carry, (a >> i) & 1, (b >> i) & 1)
        result.append(sum_bit)

    result.append(carry)  # Final carry (9th bit in case of overflow)
    return result[::-1]  # Reverse to get correct order

a = 0b10101010  # 170
b = 0b11001100  # 204

sum_result = add_8bit(a, b)
print("Result:", "".join(map(str, sum_result)))  # Output: '110101110'