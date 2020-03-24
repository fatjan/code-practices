def countingValleys(n, s):
    pos = 0
    valCount = 0
    for i in s:
        if i == 'U':
            if pos + 1 == 0:
                valCount += 1
            pos += 1
        else:
            pos -= 1
    return valCount    
            
        

print(countingValleys(8,'UDDDUDUU'))
