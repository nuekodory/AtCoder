max_len = int(input())
s = input()

if len(s) > max_len:
    print(f"{s[:max_len]}...")
else:
    print(s)
