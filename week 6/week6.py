def main():
 
    beg_balance,annual_interest,monthly_payment= input_data()

    end_balance, reduction_principle = calculate_values(beg_balance,annual_interest,monthly_payment)

    display_value(end_balance, reduction_principle)

def  input_data():
    beg_balance=float(input("enter the beg of month balance "))
    annual_interest=float(input("enter the annual intrest "))
    monthly_payment=float(input("enter monthly payment "))
                          
    return beg_balance,annual_interest,monthly_payment

def calculate_values(beg_balance,annual_interest,monthly_payment):
    interest_amount_per_month=beg_balance*(annual_interest)/12/100
    reduction_principle=monthly_payment-interest_amount_per_month
    end_balance=beg_balance-reduction_principle
    return end_balance,reduction_principle

def display_value(end_balance,reduction_principle):
   print("reduction principle amount is:",reduction_principle)
   print("end of month balance is:",end_balance)

main()