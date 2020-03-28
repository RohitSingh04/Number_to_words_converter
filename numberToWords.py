# Program translates a number into words. Supports numbers up to 15 digits

def spell_digit_ones(digit):

    ones_dict = {"0":"", "1":"One ", "2":"Two ", "3":"Three ", "4":"Four ", "5":"Five ", "6":"Six ", "7":"Seven ",
                 "8":"Eight ", "9":"Nine "}

    return ones_dict[digit]

def spell_digit_tens(digit):

    tens_dict = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy",
                 "8": "Eighty", "9": "Ninety"}

    return tens_dict[digit]

def spell_digit_teens(digit):

    teens_dict = {"0":"Ten ", "1":"Eleven ", "2":"Twelve ", "3":"Thirteen ", "4": "Fourteen ", "5": "Fifteen ",
                  "6":"Sixteen ", "7": "Seventeen ", "8": "Eighteen ", "9": "Nineteen "}

    return teens_dict[digit]


def translate_threes(three_digits):
    global num_spelt

    if three_digits[0] == three_digits[1] == three_digits[2] == "0":
        num_spelt += "Zero"

    elif three_digits[0] != "0":
        num_spelt += spell_digit_ones(three_digits[0]) + "Hundred "
        if three_digits[1] != "0" or three_digits[2] != "0":
            num_spelt += "and "

    if three_digits[1] == "0":
        if three_digits[2] != "0":
            num_spelt += spell_digit_ones(three_digits[2])

    elif three_digits[1] == "1":
        num_spelt += spell_digit_teens(three_digits[2])

    else:
        connector = "-"
        if three_digits[2] == "0":
            connector = " "
        num_spelt += spell_digit_tens(three_digits[1]) + connector + spell_digit_ones(three_digits[2])

def translate():
    global num_spelt
    global num_string
    three_digits = ""

    mod = 0
    while (len(num_string)-mod) %3 != 0:
        mod += 1

    if mod == 0:
        mod = 3
    three_digits += num_string[:mod]
    while len(three_digits) != 3:
        three_digits = "0" + three_digits
    translate_threes(three_digits)

    if 13 <= len(num_string) <= 15:
        num_spelt += "Trillion "

    if 10 <= len(num_string) <= 12:
        num_spelt += "Billion "

    if 7 <= len(num_string) <= 9:
        num_spelt += "Million "

    if 4 <= len(num_string) <= 6:
        num_spelt += "Thousand "

    if len(num_string) <=3:
        num_string = []
    else:
        num_string = num_string[mod:]
        if len(num_string) <= 3 and num_string[0] == "0": #accounts for the 'and' in 7,001(Seven hundred and one)
            num_spelt += "and "


while True:
    num = 0
    num_spelt = ""
    num_string = ""

    while True:
        num_string = input("Enter a positive integer: ")

        try:
            num = int(num_string)
        except:
            print("That is not a valid integer")
            continue

        if num < 0 or num > 10**15:
            print("That integer is out of range!")
            continue
        else:
            break

    while num_string[0] == "0" and len(num_string)!=1:
        num_string = num_string[1:]

    while num_string != []:
        translate()
    print(num_spelt)












