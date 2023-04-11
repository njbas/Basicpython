numbers = {1: "One", 2: "Two", 3: "Three"}

province = {
    "bkk": "Bangkok",
    "cha": "Chiang Mai",
    "kan": "Khon Kaen",
    "nkh": "Nakhon Ratchasima"
}

print(numbers)
print(numbers[1])
print(numbers[3])

print("---------------------")

print(province["bkk"])

print("---------------------")

# loop dictionary
for p in province.keys():
    if p == "cha":
        print("AAA")
        continue
    print(p)


print("---------------------")

for p in province.values():
    print(p)

print("---------------------")

print("########################")
for i in province.keys():
    print(i + " " + province[i])
print("---------------------")
