# สร้าง function แบบไม่มีการรับค่า
def hello():
    print("Hello World")


# เรียกใช้งาน Function
hello()

# สร้าง Function แบบมีการรับค่าและไม่มีการส่งค่ากลับ


def info(msg):
    print("Welcome", msg)


# เรียกใช้งาน Function info()
info("Python")

# สร้าง Function แบบมีการรับค่าและมีการส่งค่ากลับ


def area(width=0, height=0, * args):
    result = width * height
    return result


# เรียกใช้งาน Function Area
print("Area = ", area(5, 6))
print("Area = ", area())
print("Area = ", area(5, 6, 7, 8, 9))
