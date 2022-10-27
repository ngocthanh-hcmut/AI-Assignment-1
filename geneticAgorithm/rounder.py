def round(number):
    afterDot = number % 1
    beforDot = int(number)
    if afterDot >= 0.5: 
        return beforDot + 1
    else:
        return beforDot