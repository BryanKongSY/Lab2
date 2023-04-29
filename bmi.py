def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = float(weight/pow(height,2))
    print(bmi)
    if bmi < 18.5:
        print("Underweight")
    elif bmi > 25.0:
        print("Overweight")
    else:
        print("Normal weight")



calculate_bmi(weight=30, height=1.73)
