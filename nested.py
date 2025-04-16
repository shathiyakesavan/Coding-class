medical_cause=input("Did you attend medical school, Y or N")
atten=int(input("How many days did you attend"))


if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>= 75:
        print("Allowed")
    else:
        print("Not allowed")