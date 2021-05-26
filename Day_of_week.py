"""
The following Python algorithm is based upon one provided by Dr. Arthur Benjamin of Harvey Mudd College.
It is explained in his lecture in The Great Courses course "The Secrets of Mental Math" and his book
"Secrets of Mental Math" with Dr. Michael Shermer. To preserve the attribution of his method of mental math,
I have deliberately omitted the memorization secrets. You will have to purchase his materials for that.
I simply offer this simple calculation for the day of the week for any date since 1600 on the Gregorian calendar.
Note that not all countries adopted the Gregorian calendar at the same time.
Please include the above comments if you use this algorithm in your code.
Jerald Cogswell
"""

def get_day_of_week(month, date, year): # integers as input. Leading zeros are optional.
    # If you do not wish the program to terminate upon the following condition, consider a try or if statement.
    assert int(year) > 1599, "No Gregorian calendar before 1600 for most countries, even later for others."

    is_a_leap = bool( (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
    century_list = [0, 5, 3, 1, 0]    # 17th through 21st centuries (1600 - 2099)
    day_list = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    #               Jan  Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    #days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #month_codes   = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]  # These codes describe the day offset since first of year
    month_dict = {1 : (31,6), 2 : (28,2), 3 : (31,2), # key is month. value is tuple of days_in_month and month_code
                  4 : (30,5), 5 : (31,0), 6 : (30,3),
                  7 : (31,5), 8 : (31,1), 9 : (30,4),
                  10: (31,6), 11: (30,2), 12: (31,4)
    }

    days_in_month, month_code = month_dict[month]
    if month ==2 and is_a_leap:
        days_in_month += 1
    if date>days_in_month:  # Check date for valid range for that month
        return("Invalid date", 9)         # Your program can check for error code 9 as an invalid day number

    century_code = century_list[(year // 100) - 16] # No Gregorian calendar before 17th century, and not in all countries
    year_code = century_code + ((year % 100) // 4) + (year % 100) # number of leaps this century plus year number
    if is_a_leap and month<3: # Leap year: For January and February the leap hasn't happened yet, so decrement month code
        month_code -=1
    day_number = (year_code + month_code + date) % 7
    day_of_week = day_list[day_number]

    return(day_of_week, day_number) # Day of Week as string. Day number 0 - 6 for Sunday through Saturday, respectively.


def main():  # Sample Input Routine for above function
        flag = True
        while flag:
            try:
                month,date,year = [int(i) for i in input("Input date as mm/dd/yyyy. Leading zeros optional: ").split('/',2)]
                day_of_week, day_no = get_day_of_week(month, date, year)
                mm, dd, yyyy = [str(i) for i in (month, date, year)]
                print(mm, "/", dd, "/", yyyy, " is a ", day_of_week, " , Day number ", day_no, '\n', sep='')
            except:
                flag = False

        print("Finished")

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
