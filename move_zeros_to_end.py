def move_zeros_to_end(arr):
    #array for non zeros
    result = []
    
    # array for zeros
    zero = []

   
    for num in arr:
        if num != 0:
            result.append(num)  # Add non-zero elements to result
        else:
            zero.append(num)  # Append zeros to the zero list

    # Append zeros at the end of the result
    result.extend(zero) 
    
    return result

# Example usage:
arr = [0, 1, 9, 0, 3, 12]
result = move_zeros_to_end(arr)
print(result)  # Output: [1, 9, 3, 12, 0, 0]
