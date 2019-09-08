smalest=None
largest=None
num = None

while True:
    num = input(" Enter any number please:\n")
    if num == "stop":
        break
    num = int(num)
    if smalest is None:
        largest = num
        smalest = num
    if num > largest:
        largest = num
    if num < smalest:
        smalest = num

print(largest)
print(smalest)
