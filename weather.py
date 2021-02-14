# gets temperature
temp = 36.2

# round the temp
temp = temp.__round__()


# checks the daily status

def daily_status(t):
    if t < 7:
        return "freezing"
    elif t < 15:
        return "chilly"
    elif t < 21:
        return "normal"
    elif t < 30:
        return "warm"
    else:
        return "hot"


print(temp)
print(daily_status(temp))
