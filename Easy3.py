def generate(numRows):
    if numRows == 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, numRows):
        prev_row = triangle[-1]
        new_row = [1]  # Each row starts with 1
        
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)
    
    return triangle

# Test cases
numRows1 = 5
print(generate(numRows1))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows2 = 1
print(generate(numRows2))  # Output: [[1]]
