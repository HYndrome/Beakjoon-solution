def compound_interest_amount(p,r,t,n):
    amount = p
    for i in range(n*t):
        amount *= (1 + r/n)
    return amount
result = compound_interest_amount(1500000, 0.043, 6, 4)
print(f'{result:.0f}')