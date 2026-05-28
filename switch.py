choice = int(input("Enter number (1-4): "))

a = 10
b = 5

if choice == 1:
    print("Addition =", a + b)

elif choice == 2:
    print("Subtraction =", a - b)

elif choice == 3:
    print("Multiplication =", a * b)

elif choice == 4:
    print("Division =", a / b)

else:
    print("Invalid choice")
