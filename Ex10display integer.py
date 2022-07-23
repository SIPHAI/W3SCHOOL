# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. G
# Sample value of n is 5
Input = int(input("Enter the integer n :"))
n1 = int("%s"%Input)
n2 = int("%s%s"%(Input,Input))
n3 = int("%s%s%s"%(Input,Input,Input))
print("The results is :",(n1+n2+n3))
#  be carefull with % "" etc.