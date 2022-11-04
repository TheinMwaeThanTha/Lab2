def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    # Add code here to calculate BMI
    bmi = weight / (height * height)
    if 18.5 < bmi < 25.0:
        ans = "normal weight"
    elif bmi < 18.5:
        ans = "under weight"
    else:
        ans = "over weight"

    print(ans)


calculate_bmi(weight=57, height=1.73)