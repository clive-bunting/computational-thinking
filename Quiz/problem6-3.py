def probTest(limit):
    prob = 1.0 / 6.0
    roll = 1
    while prob >= limit:
        roll += 1
        prob *= (5.0 / 6.0)

    return roll

print probTest(25/216.0)
