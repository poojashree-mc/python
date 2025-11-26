age = 21
message =  "ur aged" if age > 20 else " ur young "
print(message)

high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


    