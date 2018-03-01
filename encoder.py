from math import floor


b62_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62Encoder(base10Num):
    # get the remainder
    remainder = ( base10Num % 62 )
    # first b62 result
    base62 = b62_alphabet[ remainder ]
    # while the result of the division isnt aprox to 0 keep looping
    res = floor( base10Num / 62 )
    while res:
        # remainder with the result of the division
        remainder = res % 62
        # append the base62 result
        base62 = b62_alphabet[int( remainder )] + base62
        # get the new result of the division
        res = floor( res / 62 )

    return base62
