hon = (2, 4, 5, 7, 9)
pon = (0, 1, 6, 8)
bon = (3, )

s = input().strip()

last = int(s[-1])

if last in hon:
    print("hon")
elif last in pon:
    print("pon")
else:
    print("bon")
