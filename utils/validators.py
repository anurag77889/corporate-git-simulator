def validateAmount(amount):
    if amount < 0 and amount > float('inf'):
        print("Not a valid amount")
    else:
        return amount