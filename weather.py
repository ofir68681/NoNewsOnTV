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
