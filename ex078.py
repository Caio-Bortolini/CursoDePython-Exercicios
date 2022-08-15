
nums = []

for c in range(0,5):
    nums.append(int(input(f"Digite o valor para a posição {c}: ")))

print(f"O maior valor digitado foi {max(nums)} e esta na posição {nums.index(max(nums))}")
print(f"O menor número digitado foi {min(nums)} e esta na posição {nums.index(min(nums))}")



