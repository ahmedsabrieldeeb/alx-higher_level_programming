#!/usr/bin/python3

def roman_to_int(roman_string):
    thousands = {'M': 1000,
                 'MM': 2000,
                 'MMM': 3000}

    hunderds = {'C': 100,
                'CC': 200,
                'CCC': 300,
                'CD': 400,
                'D': 500,
                'DC': 600,
                'DCC': 700,
                'DCCC': 800,
                'CM': 900}

    tens = {'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90}

    units = {'I': 1,
             'II': 2,
             'III': 3,
             'IV': 4,
             'V': 5,
             'VI': 6,
             'VII': 7,
             'VIII': 8,
             'IX': 9}

    res = 0  # initial value for returned value

    if roman_string:
        # scanned windows
        temp_str = roman_string[0:4]

        while temp_str not in thousands and len(temp_str):
            temp_str = temp_str[:-1]
        if len(temp_str):
            # come here if you are in thousands
            res = res + thousands[temp_str]
            roman_string = roman_string[len(temp_str):]

        temp_str = roman_string[0:4]  # prepare for the next check

        while temp_str not in hunderds and len(temp_str):
            temp_str = temp_str[:-1]
        if len(temp_str):
            # come here if you are in hunderds
            res = res + hunderds[temp_str]
            roman_string = roman_string[len(temp_str):]

        temp_str = roman_string[0:4]  # prepare for the next check

        while temp_str not in tens and len(temp_str):
            temp_str = temp_str[:-1]
        if len(temp_str):
            # come here if you are in tens
            res = res + tens[temp_str]
            roman_string = roman_string[len(temp_str):]

        temp_str = roman_string[0:4]  # prepare for the next check

        while temp_str not in units and len(temp_str):
            temp_str = temp_str[:-1]
        if len(temp_str):
            # come here if you are in units
            res = res + units[temp_str]
            roman_string = roman_string[len(temp_str):]

        return res
    return res
