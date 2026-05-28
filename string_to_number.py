keywords = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
    "billion": 1000000000,
    "trillion": 1000000000000,
    "quadrillion": 1000000000000000,
    "quintillion": 1000000000000000000,
    "sextillion": 1000000000000000000000,
    "septillion": 1000000000000000000000000,
    "octillion": 1000000000000000000000000000,
    "nonillion": 1000000000000000000000000000000,
    "decillion": 1000000000000000000000000000000000,
    "undecillion": 10000000000000000000000000000000000,
    "duodecillion": 100000000000000000000000000000000000,
    "tredecillion": 1000000000000000000000000000000000000,
    "quattuordecillion": 10000000000000000000000000000000000000,
    "quindecillion": 100000000000000000000000000000000000000,
    "sexdecillion": 1000000000000000000000000000000000000000,
    "septendecillion": 10000000000000000000000000000000000000000,
    "octodecillion": 100000000000000000000000000000000000000000,
    "novemdecillion": 1000000000000000000000000000000000000000000,
    "vigintillion": 10000000000000000000000000000000000000000000,
    "unvigintillion": 100000000000000000000000000000000000000000000,
    "duovigintillion": 1000000000000000000000000000000000000000000000,
    "trevigintillion": 10000000000000000000000000000000000000000000000,
    "quattuorvigintillion": 1000000000000000000000000000000000000000000000000,
    "quinvigintillion": 10000000000000000000000000000000000000000000000000,
    "sexvigintillion": 100000000000000000000000000000000000000000000000000,
    "septenvigintillion": 1000000000000000000000000000000000000000000000000000,
    "octovigintillion": 10000000000000000000000000000000000000000000000000000,
    "novemvigintillion": 100000000000000000000000000000000000000000000000000000,
    "trigintillion": 1000000000000000000000000000000000000000000000000000000,
    "untrigintillion": 10000000000000000000000000000000000000000000000000000000,
    "duotrigintillion": 100000000000000000000000000000000000000000000000000000000,
}


# Counting total digits in a number
def digitCounter(number):
    return len(str(abs(number)))


input_keywords = input("Enter the string number: ").lower().strip().split()
results = list()
total_result = 0
temp = 0

for keyword in input_keywords:
    if keyword in keywords:
        if digitCounter(keywords[keyword]) >= 4:
            temp *= keywords[keyword]
            results.append(temp)
            temp = 0
        elif digitCounter(keywords[keyword]) == 3:
            temp *= keywords[keyword]
        else:
            temp += keywords[keyword]
results.append(temp)

for result in results:
    total_result += result


print(total_result)
