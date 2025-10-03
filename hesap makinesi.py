# This function adds two numbers
def toplama(x, y):
    return x + y

# This function subtracts two numbers
def çıkarma(x, y):
    return x - y

# This function multiplies two numbers
def çarpma(x, y):
    return x * y

# This function divides two numbers
def bölme(x, y):
    return x / y


print("Select operation.")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

while True:
    # take input from the user
    choice = input("Dört işlemden birini seç(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("İlk sayını yaz: "))
            num2 = float(input("İkinci sayını yaz: "))
        except ValueError:
            print("Invalid input. Lütfen yazan sayılardan birini giriniz.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", toplama(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", çıkarma(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", çarpma(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", bölme(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input( "Bir sonraki hesaplamayı yapalım mı? (Evet/Hayır): ")
        if next_calculation == "Hayır"   "":
          break
    else:
        print("Invalid Input")