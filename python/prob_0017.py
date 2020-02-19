def prob_17(n):
    # O(n) solution.

    ones = {
        '0':'',
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'
    }
    teens = {
        '0':'',
        '1':'eleven',
        '2':'twelve',
        '3':'thirteen',
        '4':'fourteen',
        '5':'fifteen',
        '6':'sixteen',
        '7':'seventeen',
        '8':'eighteen',
        '9':'nineteen'
    }
    tens = {
        '0':'',
        '1':'ten',
        '2':'twenty',
        '3':'thirty',
        '4':'forty',
        '5':'fifty',
        '6':'sixty',
        '7':'seventy',
        '8':'eighty',
        '9':'ninety'
    }

    char_sum = 0
    for i in range(1, n+1):

        d = str(i)
        d = '0'*(4-len(d)) + d
        
        name = ''
        name += 'onethousand' if d[0]=='1' else ''  # thousands place
        name += ones[d[1]] + 'hundred' if d[1]!='0' else ''  # hundreds place
        name += 'and' if (d[1]!='0' and d[2:4]!='00') else ''  # and
        name += tens[d[2]] if d[2]!='1' else tens[d[2]] if d[3]=='0' else ''  # tens place
        name += teens[d[3]] if d[2]=='1' else ''  # teens
        name += ones[d[3]] if d[2]!='1' else '' # ones place

        char_sum += len(name)
    
    return char_sum


if __name__ == '__main__':
    # Answer: 21124
    print(prob_17(1000))
