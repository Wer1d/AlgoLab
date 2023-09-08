import time


# O(n^2)
def coin_change_recursive(coins,target):
    if target == 0: # base case : get our result!
        return [[]]
    if target < 0 or len(coins) == 0 : # base case ถ้าเหรียญหมด หรือ เกิน target
        return []
    all_changes = []

    # มองเป็นต้นไม้ ซ้ายคือ include coin ขวาคือ exclude coin

    # include first coin
    # บรรทัด 18 จะวนไปทำบรรทัด 8 เรื่อยๆจนกว่าจะถึง base case
    include_first_coin = coin_change_recursive(coins,target-coins[0])

    # change งอกทุกรอบที่ recursive return value 
    # บรรทัด 22 ทำงานเมื่อ base case ทีทำงานแล้ว
    for change in include_first_coin:
        all_changes.append([coins[0]] + change)


    # exclude first coin -> do this when base case is trigered, continue from above level of tree
    exclude_first_coin = coin_change_recursive(coins[1:],target)
    all_changes += exclude_first_coin
    return all_changes

def coin_change_bottomUp(coins, target):
    table = [[] for _ in range(target + 1)]
    table[0] = [[]] # base case 
    
    # table[1] would be result of target=2
    # ลองใช้แต่ละเหรียญ
    for coin in coins:
        for i in range(coin, target + 1):
            for prev_combination in table[i - coin]: # ของที่ exitst แล้วช่วยเติม
                table[i].append(prev_combination + [coin])    
            
    return table[target]

def coin_change_topDown(coins, amount):
    def find_combinations(target):
       
        if target == 0: # base case!
            return [[]]
        
        if target in memo: # ถ้าเคยคำนวนแล้ว ก็เรียกใช้ memo
            return memo[target]
        
        all_combinations = []
        for coin in coins:
            if coin <= target: # ถ้าเหรียญยังใส่ได้

                # Recursive remaining amount
                remaining_combinations = find_combinations(target - coin)
                
                # Add the current coin to each combination and sort it
                for comb in remaining_combinations:
                    all_combinations.append(sorted([coin] + comb))
                print("memo2:",memo)

        # Remove duplicates 
        unique_combinations = {tuple(comb) for comb in all_combinations}
        # Convert back to lists
        memo[target] = [list(comb) for comb in unique_combinations]
        return memo[target]
    
    memo = {}  
    combinations = find_combinations(amount)
    
    return combinations if combinations else [[]]


with open("./input.txt", "r") as file:
    # Read the first line as the target
    target = int(file.readline().strip())
    
    # Read the rest of the lines and split them into a list
    coins = list(map(int, file.readline().strip().split()))

print(coins)
print(target)
# print(f"Combinations recur of coins to make change for {target}:")
# time_start = time.perf_counter()
# combinations_recur = coin_change_recursive(coins, target)
# time_end = time.perf_counter()
# print(f"Time elapsed: {time_end - time_start} seconds")
# print("recur:",combinations_recur)

# print(f"Combinations bot of coins to make change for {target}:")
# time_start = time.perf_counter()
# combinations_bot = coin_change_bottomUp(coins, target)
# time_end = time.perf_counter()
# print(f"Time elapsed: {time_end - time_start} seconds")
# print("bot:",combinations_bot)

print(f"Combinations top of coins to make change for {target}:")
time_start = time.perf_counter()
combinations_top = coin_change_bottomUp(coins, target)
time_end = time.perf_counter()
print(f"Time elapsed: {time_end - time_start} seconds")
print("top:",combinations_top)