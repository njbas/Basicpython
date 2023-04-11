import time

r = 1
while True:
    # ถ้า loop = 30
    if r <= 30:
        if r % 2 == 1:
            print(r, "on")
        else:
            print(r, "off")
        time.sleep(1)
    else:
        break
    r = r+1
