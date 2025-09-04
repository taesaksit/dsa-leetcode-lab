class BubbleSorted:
    def sort(self, val) -> list[int]:
        size = len(val) - 1
        for i in range(size):
            for j in range(size - i):
                if val[j] > val[j + 1]:
                    temp = val[j]
                    val[j] = val[j + 1]
                    val[j + 1] = temp

        return val


arr = [5, 6, 9, 8, 4, 2]
sol = BubbleSorted()
result = sol.sort(arr)
print(f"Result: {result} ")
