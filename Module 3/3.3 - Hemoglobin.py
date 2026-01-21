gender = str(input("What is your biological gender? "))
gender = gender.lower()
hemoglobin = int(input("What is your hemoglobin? "))

# 117-155 g/l. female
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin is too low")
    elif hemoglobin > 155:
        print("Your hemoglobin is too high")
    else:
        print("Your hemoglobin is normal")

# 134-167 g/l. male
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin is too low")
    elif hemoglobin > 167:
        print("Your hemoglobin is too high")
    else:
        print("Your hemoglobin is normal")

else:
    print("Invalid gender, please try again.")