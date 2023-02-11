def calculateAbsolute():
    
    # This first line is provided for you
    in_num = input("Enter a number: ")
    in_num = int(in_num)

    if in_num > 21:
        abs_num = (in_num - 21) * 2
    else:
        abs_num = abs(in_num) - 21

    print("Result:" , abs_num)
    
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
