rot = int(input())
text = input()

text_int = [ord(x)+rot for x in text]
output = [chr(x) if x <= 90 else chr(x-26) for x in text_int]
print("".join(output))
