import fibonacci_recursion
import factorial
import string_reverse

while True:
    choice = int(input("1 - fibonacci, 2 - factorial, 3 - reverse string, 4 - exit"))
    if choice == 1:
        print(fibonacci_recursion.fib(int(input("ending  >>"))))
    elif choice == 2 :
        print(factorial.factorial(int(input("enter number >> "))))
    elif choice == 3:
        print(string_reverse.rev_str(input("enter a string ")))
    elif choice == 4:
        break
