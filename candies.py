"""Candy task."""

a = int(input()) # candies number in the first box
b = int(input()) # candies number in the second box
n = int(input()) # candies limit

print(min(a+b, n))
