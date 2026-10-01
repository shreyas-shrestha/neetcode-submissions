class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [-1] * (amount + 1)
        arr[0] = 0
        for i in range(len(arr)):
            if i in coins:
                arr[i] = 1
        for value in range(len(arr)):
            for coin in coins:
                if value >= coin:
                    if arr[value - coin] == -1:
                        arr[value] = arr[value]
                    elif arr[value] == -1:
                        arr[value] = arr[value - coin] + 1
                    else:
                        arr[value] = min(arr[value], arr[value - coin] + 1)
        return arr[amount]