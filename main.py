from datetime import date

def numerologyPrint(numerologyNumber):
    print("Your numerology number is: " + str(numerologyNumber))
def numerologyOutcome(numerologyNumber):
    if numerologyNumber == 1:
        print("Numerology: You are independant, original, self driven, ambitous, a leader, a visionary, individualistic, determined, and ruthless")

    elif numerologyNumber == 2:
        print("Numerology: You are intuitive, diplomatic, sensitive, supportive, a peacemaker, spontaneous, warm, insightful, and unrealistic")

    elif numerologyNumber == 3:
        print("Numerology: You are creative, a communicator, energetic, inventive, bouncy, artistic, broadminded, imaginitive, and scattered")

    elif numerologyNumber == 4:
        print("Numerology: You are traditional, orderly, helpful, persevering, steady, logical, self-disciplined, and practical")

    elif numerologyNumber == 5:
        print("Numerology: You are expansive, a visionary, adventurous, magnetic, witty, adaptable, resourceful, and curious")

    elif numerologyNumber == 6:
        print("Numerology: You are responsible, protective, nurturing, stable, balanced, sympathetic, compassionate, and loving")

    elif numerologyNumber == 7:
        print("Numerology: You are analytical, logical, reserved, inventive, knowledgeable, studious, introspective, and intuitive")

    elif numerologyNumber == 8:
        print("Numerology: You are ambitious, a big Thinker, successful, a leader, authoritative, courageous, and influential")

    elif numerologyNumber == 9:
        print("Numerology: You are aiving, a humanitarian, selfless, sophisticated, idealistic, creative, and expressive")

    elif numerologyNumber == 11:
        print("Numerology: You are intuitive, inspirational, a dreamer, illuminated, considerate, sensitive, and understanding")

    elif numerologyNumber == 22:
        print("Numerology: You are logical, intuitive, a master builder, a powerful force, a leader, an achiever, and resourceful")

    elif numerologyNumber == 33:
        print("Numerology: You are the master number 33 which is nicknamed the master teacher and has deep spiritual and religious meaning. The appearance of the number 33 indicates the need for proper understanding, that which is acquired before communicating that understanding with others.")


def numerology(name):
    print("Name: " + name)
    name = name.upper()
    number = 0

    for i in range(len(name)):
        if (name[i] == 'A' or name[i] == 'J' or name[i] == 'S'):
            number += 1
        elif (name[i] == 'B' or name[i] == 'K' or name[i] == 'T'):
            number += 2
        elif (name[i] == 'C' or name[i] == 'L' or name[i] == 'U'):
            number += 3
        elif (name[i] == 'D' or name[i] == 'M' or name[i] == 'V'):
            number += 4
        elif (name[i] == 'E' or name[i] == 'N' or name[i] == 'W'):
            number += 5
        elif (name[i] == 'F' or name[i] == 'O' or name[i] == 'X'):
            number += 6
        elif (name[i] == 'G' or name[i] == 'P' or name[i] == 'Y'):
            number += 7
        elif (name[i] == 'H' or name[i] == 'Q' or name[i] == 'Z'):
            number += 8
        elif (name[i] == 'I' or name[i] == 'R'):
            number += 9

    if (number == 11 or number == 22 or number == 33):
        numerologyNumber = number
    else:
        nums = str(number)
        ten = nums[0]
        ones = nums[1]
        numerologyNumber = int(ten) + int(ones)
    numerologyOutcome(numerologyNumber)
    numerologyPrint(numerologyNumber)


def monthCalc(month):
    if birthMonth == 1:
        monthName = "January"
    elif birthMonth == 2:
        monthName = "February"
    elif birthMonth == 3:
        monthName = "March"
    elif birthMonth == 4:
        monthName = "April"
    elif birthMonth == 5:
        monthName = "May"
    elif birthMonth == 6:
        monthName = "June"
    elif birthMonth == 7:
        monthName = "July"
    elif birthMonth == 8:
        monthName = "August"
    elif birthMonth == 9:
        monthName = "September"
    elif birthMonth == 10:
        monthName = "October"
    elif birthMonth == 11:
        monthName = "November"
    elif birthMonth == 12:
        monthName = "December"
    return monthName


# Sub algorithm 1
def todayIsBday(birthMonth, birthDate, todayDate, todayMonth):
    if todayMonth == birthMonth and birthDate == todayDate:
        print("Today is your Birthday!")


# Sub algorithm 2
def birthdaySameMonth(birthMonth, birthDate, todayDate, todayMonth):
    if todayMonth == birthMonth and birthDate != todayDate:
        if birthDate > todayDate:
            daysBetween = birthDate - todayDate
            totalDays = daysBetween
        elif birthDate < todayDate:
            daysBetween = todayDate - birthDate
            totalDays = 365 - daysBetween
        print("Your Birthday is in this month! There are " + str(totalDays) + " days till your birthday!")


# Start of main algorithm
def daysUntilCalculation(todayMonth, todayDate, todayYear, birthMonth, birthDate, birthYear, name):
    count = 0
    totalDays = 0
    monthsOfTheYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    todayIsBday(birthMonth, birthDate, todayDate, todayMonth)

    birthdaySameMonth(birthMonth, birthDate, todayDate, todayMonth)

    # birthday is going to happen this year
    count = 0
    if todayMonth < birthMonth:
        for i in (monthsOfTheYear):
            count += 1
            if (count) == todayMonth:
                totalDays += i - todayDate
            elif (count) == birthMonth:
                totalDays += birthDate
            elif (count) > todayMonth and (count) < birthMonth:
                totalDays += i

    # birthday was already this year
    if todayMonth > birthMonth:
        for i in (monthsOfTheYear):
            count += 1
            if (count) == birthMonth:
                totalDays += i - birthDate
            elif (count) == todayMonth:
                totalDays += todayDate
            elif (count) > birthMonth and (count) < todayMonth:
                totalDays += i
        totalDays = 365 - totalDays

    if count != 0:
        print("There are " + str(totalDays) + " days till your birthday!")
    numerology(name)


# inputs
name = input("Enter your name: ")
today = str(date.today())
todaysDateString = today[5:7] + '/' + today[8:] + '/' + today[0:4]
print("Todays date is: ", todaysDateString)


birthdayDateString = input("Enter your birthday in MM/DD/YYYY: ")

todayMonth = todaysDateString[0:2]  # finding todays month
todayDate = todaysDateString[3:5]  # finding todays date
todayYear = todaysDateString[6:10]  # finding todays year

birthMonth = birthdayDateString[0:2]  # finding birth month
birthDate = birthdayDateString[3:5]  # finding birth date
birthYear = birthdayDateString[6:10]  # finding birth year

todayMonth = int(todayMonth)
todayDate = int(todayDate)
todayYear = int(todayYear)

birthMonth = int(birthMonth)
birthDate = int(birthDate)
birthYear = int(birthYear)

# put birthday on screen
monthName = monthCalc(birthMonth)
print("Your birthday is " + str(monthName) + " " + str(birthDate) + ", " + str(birthYear))

# Main algorithm
daysUntilCalculation(todayMonth, todayDate, todayYear, birthMonth, birthDate, birthYear, name)