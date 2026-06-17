def FindMaxInArray(arr):
    if not arr:
        print("Array is empty")
        return
        
    max_val = max(arr)
    max_idx = arr.index(max_val)
    
    print(max_val)
    print(max_idx)


print("--- Test Case 1 ---")
FindMaxInArray([1, 5, 3, 9, 2]) 

print("\n--- Test Case 2 ---")
FindMaxInArray([-10, -5, -23, -2, -18]) 

print("\n--- Test Case 3 ---")
FindMaxInArray([4, 8, 2, 8, 1]) 
