# importing modules
import addition
import subtraction
import multiplication
import division
import modulas_division

operations=(
    "1.Addition \n",
    "2.Subtraction \n",
    "3.Multiplication \n",
    "4.Division \n",
    "5.ModularDivision \n")


# main function
if __name__ == "__main__":
    print(*operations)
    choice = int(input("Please select your operation: "))
    if choice == 1:
        a, b =map(int,input("Please enter two values with space: ").split())
        res = addition.add(a, b)
        print("Sum of two numbers is: ", res)
    elif choice == 2:
        a, b =map(int,input("Please enter two numbers with spaces: ").split())
        res = subtraction.sub(a, b)
        print("Subtraction of two numbers is: ",res)
    elif choice == 3:
        a, b =map(int,input("Please enter two numbers with spaces: ").split())
        res = multiplication.mul(a, b)
        print("Product of two numbers are: ",res)
    elif choice == 4:
        a, b =map(int,input("Please enter two numbers with spaces: ").split())
        res = division.div(a, b)
        print("Division of two numbers are: ",res)
    elif choice == 5:
        a, b =map(int,input("Please enter two numbers with spaces: ").split())
        res = modulas_division.mod(a, b)
        print("Modular division of two numbers are: ",res)
    else:
        print("Please select in between 1 - 5")
      
      

    
