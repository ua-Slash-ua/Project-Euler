units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
exeption = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_of = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
sum = 0

# одиниці
for a in units:
    number = a
    sum+=len(number)
    print(number)
# винятки від 10 до 19
for b in exeption:
    number = b
    sum += len(number)
    print(number)
# десятки
for a in tens_of:
    number_10 = a
    sum += len(number_10)
    print(number_10)
    for b in units:
        number = number_10 + '' + b
        sum += len(number)
        print(number)
# сотні

for a in units:
    number_100 = a+'hundred'
    sum += len(number_100)
    print(number_100)
    for aa in units:
        number_001 = number_100+'and'+aa
        sum += len(number_001)
        print(number_001)
    for bb in exeption:
        number_010 = number_100 + 'and' + bb
        sum += len(number_010)
        print(number_010)
    for cc in tens_of:
        number_10 = number_100 + 'and'+ cc
        sum += len(number_10)
        print(number_10)
        for dd in units:
            number = number_10 + '' + dd
            sum += len(number)
            print(number)

sum += len('onethousand')

print(sum)
