#write a program to find sum of first n even numbers.
# n = int(input())
# i = 1
# sum = 0
# count = 0
# while (count <= n):
#     if (i%2==0):
#         sum += i
#         count += 1
#     i = i+1
# print(sum)        
# n = int(input())
# sum = 0
# while n > 0:
#     sum = sum + n % 10
#     n = n//10
# print(sum) 
# write a progra to find sum of square of digits of a given numbers.
# n = int(input())
# sum = 0
# while n>0:
#     sum = sum + (n%10)*(n%10)
#     n = n//10
# print(sum)    
# n = int(input())
# sum = 0
# while n > 0:
#     sum = sum + (n%10)*(n%10)
#     n = n//10
# print("sum of all digits", sum)    

#write a program to find the sum of cube of digoits of a given number
# i =  int(input())
# sum = 0
# while i > 0:
#     sum = sum +(i%10)*(i%10)*(i%10)
#     i = i//10
# print(sum)    

# check the armstrong number 
# n = int(input())
# b = n
# sum = 0
# while n > 0:
#     sum =sum + (n%10)*(n%10)*(n%10)
#     n = n//10
# if b==sum:
#     print("True")
# else:
#     print("False")   
#write a program to find product of a given numbers
# n = int(input())
# p = 1
# while n > 0:
#     p = p*(n%10)
#     n = n//10
# print(p)
# reverse of integer 
# n = int(input())
# r = 0
# while n > 0:
#     r = (r*10)+n%10
#     n = n//10
# print(r)    
#reverse of a string 
my_str = input("Please enter your own String : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed String is: ", str)  




