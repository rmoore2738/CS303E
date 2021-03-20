#Assignment 5
#Rebecca Moore rrm2738

#question 1
def reverse(s):
#this takes the length of the string and reverses it
    length = len(s)
    result = ''
    for i in range(length):
        result = result + s[length - (i + 1)]
    return result

user_string = input("Enter a string: ")
print(reverse(user_string))
#this prints the reversed string

#Question 2
def is_palindrome(s):
#this function determines is a number is a palindrome
#it does this by seeing if it is the same reversed
    reversed_string = reverse(s)
    return reversed_string == s

#Question 3
def palindrome_test():
    for i in range(3):
        string = input("Enter a word: ")
        if is_palindrome(string):
            print("Palindrome!")
        else:
            print("Not a palindrome.")

#this function tells the user if their input is a palidrome
#based on question 2 function

palindrome_test()

#Question 4
def is_prime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

user_integer = eval(input("Enter and integer: "))
print(is_prime(user_integer))
#this determines if a number is prime
# by seeing if it is divisible by more than 1 and itself

# Question 5
def emirp(n):
    reverse_n = reverse(str(n))
    reverse_n = eval(reverse_n)
    if not is_palindrome(str(n)):
        if is_prime(n):
            if is_prime(reverse_n):
                return True

    return False

int = eval(input("Enter an integer: "))
print(emirp(int))
#this function determines if a number and its reverse are both prime
#it does this by taking an input, reversing it, and runing it through Q4

#Question 6
def twin_primes():
    for i in range(2, 998):
        if is_prime(i):
            if is_prime(i + 2):
                print(str(i) + ", " + str(i + 2))

twin_primes()
#this prints all prime numbers until 1000 in pairs
#it uses the same function from Q4 to do this 
