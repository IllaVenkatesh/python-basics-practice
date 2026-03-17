# Scholarship Eligibility Checker
marks = int(input("Enter your marks: "))
income= int(input("Enter your family income: "))

if marks >= 90 :
    if income <200000 :
      print("Eligible for FULL Scholorship")
    else:  
      print("NOT eligible for FULL Scholorship -> HIGH income ")

elif marks >= 75 and income <300000 :
    print("Eligible for HALF scholarship")

elif marks >= 60 :
    print("Eligible for Fee reduction")

else :
    print("NOt Eligible for scholarship")
