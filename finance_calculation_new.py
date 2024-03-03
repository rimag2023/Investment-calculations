

import math
'''
Finance Calculators Task. 
Working out the interest rates: an investment calculator ('Simple' interest or 'Compound' interest) or bond calculator.

'''

# Display welcome message and calculation options.
# "RG Consultancy Services Ltd". Rima Gray is the owner and CEO of the company. "RG Consultancy Services Ltd" offers financial
# services to small and middle size companies.


print("""
           Welcome to "RG Consultancy Services Ltd".
           We offer financial calculations in these two areas:
      """      
)

while True:
    print("""
             Investment - to calculate the amount of interest you will earn on your investment
             Bond       - to calculate the amount you will have to pay on a home loan
          """)
    selection = input("""Enter either 'investment' or 'bond' from the menu above to proceed : 
                      type in exit to terminate: """).lower()# it does not matter whichever way the words 'Investment' or 'Bond' are entered:
    # It could be: 'INVESTMENT', 'investment', 'InVeStMeNt' or 'BOND', 'bond' 'BoNd'.

    if selection == 'investment':

    # the user enters the amount of money they want to deposit, an interest rate and the number of years for the money to be deposited
    # P is the amount to be deposited. The user inputs the amount, expressed as a float: numbers, which are decimal
    # numbers or fractional numbers.        
        
        P = float(input("Please enter the amount you would like to deposit: "))

    # r is the rate of interest (%). The user should not add the % symbol to input. Instead of 8% the user enters 8.
    # r = the interest entered , then divided by 100. For e.g.: if 8% is entered, then r = 0.08
        r = float(input("Please enter the rate of interest (exclude '%' symbol): ")) 
        r = r/100
        print(r)

    # t = number of years the money being invested (investment)
        t = int(input("Please enter the years for investment: "))
        print(t)
        calculation_selection = input("Please select either 'Simple' or 'Compound' interest: ").lower()
    

    # Using the formula to calculate the amount of interest the user will earn on their investment, using the 'Simple' interest calculation.
        if calculation_selection == 'simple':
            
            total_with_simple_interest = P * (1 + r * t)
            # r is the interest entered into formula: A = P * (1 + r * t); 
            
            print(f"The total amount you'll receive using simple interest is: { total_with_simple_interest :,.2f}")
        
    #The second given option to the user is to calculate the amount of interest rate the user will earn, using the 'Compound' caculation method
        elif calculation_selection == 'compound':
         
            total_with_compound_interest = P * math.pow((1 + r), t)
            # r is the interest entered into formula: A = P * math.pow((1 + r), t); 

            print(f"The total amount you'll receive using compound interest is: { total_with_compound_interest :,.2f}")
            

        else:

            print("Error. Please enter the correct data.")
            

    # P is the present value of the user's house. The user inputs the amount, expressed as a float: numbers, which are decimal numbers or fractional numbers.  
    elif selection == 'bond':

        P = float(input("Enter the present value of your house : "))# the house value is 100000. We do not use any signs to indicate the money: dollars, Euros or Pounds.
    
    # i is the rate of interest (%). The user should not add the % symbol to input. Instead of 7% the user enters 7.
    # i = the interest entered, then divided by 100. For e.g.: if 7% is entered, then r = 0.07
    # i = r/12: the interest rate payable per calendar month
        i = float(input("Please enter the rate of interest (exclude '%' symbol) : ")) / 100
        i = i / 12
        # n = time needed to repay the home loan. Time is expressed in months: 120 months.
        n = float(input("Please enter the number of months over which the bond will be repaid: "))
        
        
    # Calculating the repayment on a home loan: firstly, annually and secondly, per calendar month.
    # Rounding the total repayment amount annually and then, monthly to 2 decimal points after comma.
        repayment = (i * P)/ (1 - (1 + i)**(-n))
        print(f"The total amount you'll have to repay annually is: {repayment :,.2f}")

        repayment_month = repayment/ 12
        print(f"The total amount you'll have to repay per calendar month is: {repayment_month :,.2f}")
      
              
        continue

    elif selection == 'exit':

    # Thank the customer for using my services.
        print("Thank you for using 'RG Consultancy Services Ltd'.")
        break

    else:

        print('Invalid input')
        continue