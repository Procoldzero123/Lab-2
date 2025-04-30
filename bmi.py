def calculate_bmi(height, weight):
    print("height " +str(height))
    print("weight " +str(weight))
    bmi = weight/(height**2)
    print("bmi "+str(bmi) )
    return bmi

def classify_bmi(bmi):
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<=25):
        print("Normal Weight")
    else:   
        print("Overweight,better exercise!")
    return


def main():
    output = calculate_bmi(1.7,60)
    classify_bmi(output)
    return

if __name__ == "__main__":
    main()