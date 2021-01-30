numbers = [10, 22, 27, 30, 29, 18, 21, 1, 28, 20, 18, 5, 19, 9, 11, 22, 15, 20, 0, 6, 12, 7, 17]    



def fizzbuzz(number):
    if(number % 3 == 0 and number % 5 == 0):
        print("fizzbuzz")
    elif(number % 3 ==0):
         print("fizz")
    elif(number % 5 == 0):
         print("buzz")
    else:
         print("something went wrong")
         

for number in numbers:
    fizzbuzz(number)         
