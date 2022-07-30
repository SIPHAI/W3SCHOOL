
# my code
num1 = int(input("Enter any number :"))
num2 = int(input("Enter any number :"))
num3 = int(input("Enter any number :"))
print(num1, num2, num3)
def sum_thrice(num1,num2,num3):
    sum = num1+num2+num3
    if num1 == num2 == num3:
        sum = sum*3
    return sum
print(sum_thrice(num1,num2,num3)) 
print(sum_thrice(num1,num1,num1))

# Source code

# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
