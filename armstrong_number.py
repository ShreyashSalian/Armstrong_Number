num = input("Enter The Number :")
lenOfNum=len(num)
num=int(num)
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** lenOfNum
    temp //= 10

if num == sum:
    print(num,"is a armstring number")

else:
    print(num,"is not armstrong number")
