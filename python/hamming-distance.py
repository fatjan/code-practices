def hammingDistance(x,y):
        # convert x and y into bits format as required
        x_b = "{0:b}".format(x)
        y_b = "{0:b}".format(y)
        
        # add a required amount of 0 in front of the converted input
        if len(x_b) < 4:
            x_b = '0'*(4-len(str(x_b))) + x_b
        if len(y_b) < 4:
            y_b = '0' * (4 - len(str(y_b))) + y_b
        if len(x_b) < len(y_b):
            x_b = '0' * (len(y_b) - len(x_b)) + x_b
        elif len(x_b) > len(y_b):
            y_b = '0' * (len(x_b) - len(y_b)) + y_b
       
        count = 0  # used to count the difference occurrence
        # loop through the formatted x and y to check the hamming distance
        for i in range(len(x_b)):
            if x_b[i] != y_b[i]:  # when bits are not the same
                count += 1  # increase the count
        #finally return the number of count
        return count


print(hammingDistance(680142203, 1111953568))

