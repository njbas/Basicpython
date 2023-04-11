a = 10
b = 2.50
c = "Python Programming"

print(a)
print(b)
print(c)

x = y = z = 10
print(x, y, z)

j, k, l = 10, 20, 30
print(j, k, l)

status = True  # 1
msg = False  # 0
print(status, msg)

print(status == 1)
print(msg == 0)


price = 300.546878
qty = 10

# แบบที่ 1
print("ราคาสินค้า", "{:.2f}".format(price), "บาท จำนวน", qty, "ชิ้น")

# แบบที่ 2
print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น" % (price, qty))

# แบบที่ 3
print(f"ราคาสินค้า {price:.2f} บาท จำนวน {qty} ชิ้น")
