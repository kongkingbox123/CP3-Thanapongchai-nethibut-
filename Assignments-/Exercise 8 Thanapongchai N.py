usernameInput = input("Username : ")
userpasswordInput = input("password : ")
if usernameInput == "user101" and userpasswordInput == "121212":
    print("-DONE-")
    print(">>I Zone Shop<<")
    print("สินค้า")
    print("1.ดินสอ = 2 บาท ")
    print("2.ยางลบ = 5 บาท ")
    print("3.ไม้บรรทัด = 10 บาท ")
    print("4.กระดานวาดรูป = 150 บาท ")
    cargo = int(input("โปรดเลือกตัวเลขสินค้า : "))
    if cargo == 1 :
        products1 = 2
        Number = int(input("จำนวนสินค้า :X "))
        print(products1 * Number,"บาท")
    elif cargo == 2 :
        products2 = 5
        Number = int(input("จำนวนสินค้า :X "))
        print(products2 * Number,"บาท")
    elif cargo == 3 :
        products3 = 10
        Number = int(input("จำนวนสินค้า :X "))
        print(products3 * Number,"บาท")
    elif cargo == 4 :
        products4 = 150
        Number = int(input("จำนวนสินค้า :X "))
        print(products4 * Number,"บาท")
else:
    print(" ข้อมูลไม่ถูกต้อง !!! ")
