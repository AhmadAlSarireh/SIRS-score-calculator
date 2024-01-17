print("Welcome to the SIRS score calculator")

sirs_score = 0


#TEMPERATURE
while True:
    temp = input("Enter patient temperature: ")
    try:
        temp = float(temp)
    except ValueError:
        print("That is not a valid value. Please enter a number.")
        continue
    else:
        break

if temp > 38 or temp < 36:
    sirs_score += 1
    print("That is within the range of SIRS")
    print("Score = " + str(sirs_score))
else:
    print("This is not within the range of SIRS")
    print("Score = " + str(sirs_score))


#HEART RATE
while True:
    heart_rate = input("Enter patient heart rate per minute: ")
    try:
        heart_rate = float(heart_rate)
    except ValueError:
        print("That is not a valid value. Please enter a number.")
        continue
    else:
        break

if heart_rate > 90:
    sirs_score += 1
    print("That is within the range of SIRS")
    print("Score = " + str(sirs_score))
else:
    print("This is not within the range of SIRS")
    print("Score = " + str(sirs_score))


#RESPIRATORY RATE
while True:
    resp_rate = input("Enter patient respiratory rate per minute: ")
    try:
        resp_rate = float(resp_rate)
    except ValueError:
        print("That is not a valid value. Please enter a number.")
        continue
    else:
        break

if resp_rate > 20:
    sirs_score += 1
    print("That is within the range of SIRS")
    print("Score = " + str(sirs_score))
else:
    print("This is not within the range of SIRS")
    print("Score = " + str(sirs_score))


#WHITE BLOOD CELL COUNT
while True:
    wbc = input("Enter patient white blood count per mm^3: ")
    try:
        wbc = float(wbc)
    except ValueError:
        print("That is not a valid value. Please enter a number.")
        continue
    else:
        break

if wbc > 12000 or wbc < 4000:
    sirs_score += 1
    print("That is within the range of SIRS")
    print("Score = " + str(sirs_score))
else:
    print("This is not within the range of SIRS")
    print("Score = " + str(sirs_score))



if sirs_score > 1:
    print("POSITIVE for SIRS")
else:
    print("NEGATIVE for SIRS")
