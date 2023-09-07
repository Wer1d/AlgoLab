def coin_change_bottomUp(coins, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = []  # Base case

    for i in range(1, target + 1): # travel on dp table
        for coin in coins: 
            if i - coin >= 0 and dp[i - coin] is not None: # ถ้ายังเติมเหรีญได้ 
                if not dp[i] or len(dp[i - coin]) + 1 < len(dp[i]):
                    #check if either dp[i] is an empty list (no previous combination for
                    #  the current amount) or if adding the current coin results in a combination
                    #  with fewer coins than the existing combination for the current amount
                    dp[i] = dp[i - coin] + [coin]

    if not dp[target]:
        return []  # No combination found for the target amount

    return dp[target]  # Return the combination with the fewest coins

def coin_change_topDown(coins, amount):
    memo = [-1] * (amount + 1)

    # recur func
    def min_coins(target):

        if target == 0:
            return []
        
        if memo[target] != -1:
            return memo[target]
        
        min_coin_list = []
        
        # Iterate through each coin denomination
        # ลองใช้แต่ละเหรียญ
        for coin in coins:
            # ถ้าเหรียญยังใส่ได้
            if coin <= target:
                # Recursive remaining amount
                remaining_coins = min_coins(target - coin)
                
                # If a valid combination is found and it has fewer coins than the current minimum
                if remaining_coins is not None and (not min_coin_list or ( (len(remaining_coins) + 1 ) < len(min_coin_list) ) ):
                    min_coin_list = remaining_coins + [coin]
        
        # Update memo
        memo[target] = min_coin_list if min_coin_list else None
        return memo[target]
    
    result = min_coins(amount)
    return result if result is not None else [] 

coins =  [1, 7, 10, 25]
target = 63
minCoin = coin_change_topDown(coins, target)
print(minCoin)
print(len(minCoin))