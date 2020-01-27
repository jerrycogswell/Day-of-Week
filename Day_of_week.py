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
    day_list = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#    month_code_vals = (6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    #             Month code tuples include a day-of-week offset for that month and the number of days in that month.
    #                   Jan     Feb     March   April   May     June    July    Aug     Sept    Oct     Nov     Dec
    month_code_vals = ([6,31], [2,29], [2,31], [5,30], [0,31], [3,30], [5,31], [1,31], [4,30], [6,31], [2,30], [4,31])
    century_list = (0,5,3,1,0)
    if date>month_code_vals[month-1][1]:  # Check date for valid range for that month
        return("Invalid date", 9)         # Your program can check for error code 9 as an invalid date number

    century_code = century_list[(year // 100) - 16] # No Gregorian calendar before 17th century, and not in all countries
    year_code = century_code + ((year % 100) // 4) + (year % 100) # number of leaps this century plus year number
    month_code = month_code_vals[month-1][0]
    if is_a_leap and month<2: # Leap year: For January and February the leap hasn't happened yet, so decrement month code
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
