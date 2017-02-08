# Author: Prateek Tyagi
# Description:  This program asks the user for a quiz score and converts
#               that numeric score to a letter grade as follows:
#               score >= 93: A
#               90 <= score < 93: A-
#               87 <= score < 90: B+
#               83 <= score < 87: B
#               80 <= score < 83: B-
#               70 <= score < 80: C
#               <70: F

try:
    score = input ( "Enter your score out of 100: " ) #Ask user to input score
    
    if float (score) >100:                 #Checks if the score is not more than 100        
        print "\nInvalid score! \nTry again  by entering score less than 100"
    elif score >= 93:                       
        print "\nYour grade is A"
    elif 90 <= float (score) < 93:
        print "\nYour grade is A-"
    elif 87 <= float (score) < 90:
        print "\nYour grade is B+"
    elif 83 <= float (score) < 87:
        print "\nYour grade is B"
    elif 80 <= float (score) < 83:
        print "\nYour grade is B-"
    elif 70 <= float (score) < 80:
        print "\nYour grade is C"
    else:
            print "\nYour grade is F"
except:
    print("\nPlease enter a number and try again")   #Ask the user to input only a number