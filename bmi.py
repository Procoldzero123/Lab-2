def calculate_bmi(height, weight):
    print("height " + str(height))
    print("weight " + str(weight))
    bmi = weight / (height ** 2)
    print("bmi " + str(bmi))

    # Classify and return value
    if bmi < 18.5:
        return -1  # Underweight
    elif 18.5 <= bmi <= 25:
        return 0   # Normal weight
    else:
        return 1   # Overweight

def classify_bmi(bmi_class):
    if bmi_class == -1:
        print("Underweight")
    elif bmi_class == 0:
        print("Normal Weight")
    elif bmi_class == 1:
        print("Overweight, better exercise!")
    return

def main():
    output = calculate_bmi(1.7, 90)
    classify_bmi(output)

if __name__ == "__main__":
    main()