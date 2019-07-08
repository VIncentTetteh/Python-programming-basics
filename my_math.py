import  math
def calculate(enter, number1, number2):
    print("choose from the list.")
    print(" 1. ADD \n 2. SUBTRACT \n 3. MULTIPLY")
    if enter == "add" or enter == "ADD":
        #number1 = input("enter first number ")
        #number2 = int(input(" enter second number "))
        answer = number1 + number2
        return answer
    elif enter == "subtract" or enter == "SUBTRACT":
        #number1 = int(input("enter first number "))
        #number2 = int(input(" enter second number "))
        answer = number1 - number2
        return answer

    elif enter == "multiply" or enter == "MULTIPLY":
        #number1 = int(input("enter first number "))
        #number2 = int(input(" enter second number "))
        answer = number1 * number2
        return answer
    else:
        print("wrong input !!")


print("your answer is ", calculate("ADD",10,2))