age=int(input("Enter your age: "))
income=int(input("Enter monthly income: "))
job=(input("Do you have a valid jo? (yes/no): "))
loan= float(input("Enter the amount of loan you want: "))

if age<=21:
    print("Loan Status: Not approved")
    print("Reason: Age must be 21 or above.")

elif income < 30000:
    print("Loan Status: Not approved")
    print("Reason: Monthly income must be Rs. 30,000 or above.")

elif job != "yes":
    print("Loan Status: Not approved")
    print("Reason: You must have a valid job.")
else:
    if income < 50000:
        maximum_loan = 300000
    elif income < 80000:
        maximum_loan = 5000000
    elif income < 100000:
        maximum_loan = 800000
    else:
        maximum_loan = 1000000
        print("Maximum loan available: Rs.", maximum_loan)
        print("Requested loan amount: Rs.", loan)

   
    if loan <= maximum_loan:
        print("Loan Status: Approved")
    else:
        print("Loan Status: Not Approved")
        print("Reason: Requested loan amount exceeds the maximum loan available.")