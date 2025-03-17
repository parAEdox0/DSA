def isDuplicates(arr):
    hash_table = set()
    for x in arr:
        if x in hash_table:
            return True
        hash_table.add(x)
    return False


arr = [1, 3, 2, 1]

print(isDuplicates(arr))

