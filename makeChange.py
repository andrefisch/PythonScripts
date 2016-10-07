def coin_perm(n, coins):
    memo = [1] * (n + 1)
    
    # from 1 -> n, populate memo
    i = 1
    while i <= n:
        #try each coin
        total = 0
        for coin in coins:
            if coin <= i:
                total += memo[i - coin]
            memo[i] = total
    
    return memo[n]
