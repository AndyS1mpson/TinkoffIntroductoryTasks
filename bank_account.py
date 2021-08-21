"""Bank task."""

TRANSFER_FEE = 0.05

n = int(input()) # number of bank accounts
bank_money = list(map(int, input().split(' ')[:n]))
fee = 0.0

for _ in range(n-1):
    min_el = min(bank_money)
    bank_money.remove(min_el)
    second_smallest_num = min(bank_money)
    bank_money.remove(second_smallest_num)
    new_el = (min_el + second_smallest_num)
    fee += round(new_el  * TRANSFER_FEE, 2)
    bank_money.append(new_el)

print(fee)