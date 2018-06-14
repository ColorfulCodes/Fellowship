def money(goal, money_available, money_used):
    if sum(money_used) == goal:
        yield money_used
    elif sum(money_used) > goal:
        pass
    elif money_available == []:
        pass
    else:
        # for coin in copy of list of coins
        for change in money(goal,money_available[:], money_used+[money_available[0]]):
            yield change
        for change in money(goal,money_available[1:], money_used):
            yield change


def changePossibilities(goal,coins):
    #count possibilities
    results = []
    # for coin goal in coins
    for s in money(goal,coins, []):
        results.append(s)
    
    count = 0
    for num in results:
        count+=1
        num = str(num)
        print (count, num)
    
    return len(results)

changePossibilities(5, [1,2,5,10,20,50])

# result should return 4
