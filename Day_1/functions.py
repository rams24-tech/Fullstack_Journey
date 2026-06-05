number= int(input("Enter the number: "))
count=0
def is_prime(number):
 for i in range(2,number+1):
      i % number==0
      count=count+1
print(is_prime(number))     