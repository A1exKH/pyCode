#FizzBuzz on Python

amountOfNumbers=0
amountOfBuzz=0
amountOfFizz=0
amountOfFizzBuzz=0

start=1
finish=20

for i in range(start,finish+1): # finish+1 was done to include last value in range
    if i%15==0:
        print "FizzBuzz"
        amountOfFizzBuzz +=1
    elif i%5==0:
        print "Buzz"
        amountOfBuzz +=1
    elif i%3==0:
        print "Fizz"
        amountOfFizz +=1
    else:
        print i
        amountOfNumbers +=1
print "In range from "+str(start)+" to "+str(finish)+ " there are: \n Numbers: "+str(amountOfNumbers)+"\n Fizz: "+str(amountOfFizz)+"\n Buzz: "+str(amountOfBuzz)+"\n FizzBuzz: "+str(amountOfFizzBuzz)
