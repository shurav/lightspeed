lightSpeed = (3.104*10**16)/3280.84
while True:
    try:
        distance = float(input("What is the distance between two cities (in km): "))
        while(distance <= 0):
           distance = float(input("Try again"))
    except:
        print("Incorrect value")
    else:
        break
years = distance/lightSpeed
months = years*12
days = years*365
weeks = days/7
hours = days*24
minutes = 60*hours
seconds = 60*minutes
years = str(years)
months = str(months)
days = str(days)
weeks = str(weeks)
hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)
print(("It would take %s years, %s months, %s weeks, %s days, %s hours, %s minutes, %s seconds for light to travel that distance") % (years, months, weeks, days, hours, minutes, seconds))

