# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# Based on Cycle area which is S = Pi* r**2

r =float(input("Enter the Radius of the cycle that you want to find the Area of it :"))
Pi = 3.14156
S = Pi* r**2
# print("The are of the cycle is :",S)
print(format((S),"0.2f"))