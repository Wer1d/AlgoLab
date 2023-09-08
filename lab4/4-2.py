import time

def coin_change_bottomUp(coins, target):
    
    memo = [float('inf')] * (target + 1) # memo
    memo[0] = 0  # Base case

    for coin in coins:
        for i in range(coin, target + 1): # ปกติจะเริ่มที่ 1 แต่เราเริ่มที่ coin เพื่อoptimize
                memo[i] = min(memo[i], memo[i - coin] + 1)
        
    # Reconstruct the combination of coins.
    combination = []
    while target > 0:
        for coin in coins:
            if target >= coin and memo[target] == memo[target - coin] + 1:
                combination.append(coin)
                target -= coin
                break

    return combination

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
 
with open("./input.txt", "r") as file:
    # Read the first line as the target
    target = int(file.readline().strip())
    
    # Read the rest of the lines and split them into a list
    coins = list(map(int, file.readline().strip().split()))

print(coins)
print(target)
time_start = time.perf_counter()
minCoin = coin_change_bottomUp(coins, target)
time_end = time.perf_counter()
print(f"Time elapsed: {time_end - time_start} seconds")

print(minCoin)
print(len(minCoin))