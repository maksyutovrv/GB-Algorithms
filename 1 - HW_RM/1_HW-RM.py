# # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
print ("*****TASK 1*****")
num = input("Введите трехзначное число: ")
len = len(num)

sum = 0
m = 1
if len == 3:
    for i in num:
        sum += int(i)
else:
    print("Необходимо ввести трехзначное число")

print("Сумма: ", sum)

if len == 3:
    for i in num:
        m *= int(i)
else:
    print("Необходимо ввести трехзначное число")

print("Произведение: ", m)



