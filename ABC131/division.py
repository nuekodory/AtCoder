from fractions import gcd


a, b, c, d = map(int, input().split(' '))

cd = c * d // gcd(c, d)

div_by_c = b // c - (a-1) // c
div_by_d = b // d - (a-1) // d
div_both = b // cd - (a-1) // cd

dividable = div_by_c + div_by_d - div_both
non_dividable = (b - a + 1) - dividable

print(non_dividable)
