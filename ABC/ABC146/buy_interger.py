num_price, digit_price, budget = map(int, input().split())
min_by_digit = {x: int('1'+'0'*x) * num_price + (x+1) * digit_price for x in range(0, 10)}

max_digit = 0
for i in range(0, 10):
    if min_by_digit[i] > budget:
        break
    else:
        max_digit = i+1

if max_digit == 0:
    print("0")
    exit(0)

if max_digit == 10:
    print("1000000000")
    exit(0)

least = int('1'+'0'*(max_digit-1))
ans = min((budget - (digit_price * max_digit)) // num_price, least*10-1)
print(ans)
