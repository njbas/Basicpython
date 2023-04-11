import qrcode

# img = qrcode.make("http://www.itgenius.co.th")
# type(img)
# img.save('qrcode.png')

print("QRcode Generator Program")
print("Please type 'quit' to exit program")

while True:
    product_data = input("Please type product code: ")
    if product_data == 'quit':
        print("Thank you for using QRcode Generator Programming")
        break
    if len(product_data) == 5:
        # print(product_data)
        img = qrcode.make(product_data)
        type(img)
        img.save(f"product_qrcode/{product_data}.png")
    else:
        print("Please type 5 digits proiduct code")
