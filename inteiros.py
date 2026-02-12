num1 = int(input("DIGITE UM NUMERO:"))
num2 = int(input("DIGITE UM NUMERO:"))
num3 = int(input("DIGITE UM NUMERO:"))

if num1 < num2 and num1 < num3:
    print(f"SEU MENOR NUMERO É: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"SEU MENOR NUMERO É: {num2}")
else:
    print(f"SEU MENOR NUMERO É: {num3}")

if num1 > num2 and num1 > num3:
    print(f"SEU MAIOR NUMERO É: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"SEU MAIOR NUMERO É: {num2}")
else:
    print(f"SEU MAIOR NUMERO É: {num3}")


