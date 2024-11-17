import csv

def is_interweaving(s: str, x: str, y: str) -> tuple:
    # Initialize pointers for s, x, and y
    i, j, k = 0, 0, 0
    n, m, p = len(s), len(x), len(y)
    comparison_count = 0  # Counter for character comparisons

    # Traverse the string s
    while i < n:
        if j < m and s[i] == x[j]:  # Match with x
            comparison_count += 1
            j += 1
            i += 1
            if j == m:  # Reset j if a full repetition of x is matched
                j = 0
        elif k < p and s[i] == y[k]:  # Match with y
            comparison_count += 1
            k += 1
            i += 1
            if k == p:  # Reset k if a full repetition of y is matched
                k = 0
        else:  # No match found
            comparison_count += 1
            return False, comparison_count

    # Check if the entire s is consumed and ends with valid repetitions
    return i == n and j == 0 and k == 0, comparison_count

def main():
    with open("interweavedStrings.csv", mode='r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            s, x, y = row
            s, x, y = s.split('=')[1], x.split('=')[1], y.split('=')[1]
            result, comparisons = is_interweaving(s, x, y)
            print(f"For s={s}, x={x}, y={y}: Is interweaving? {result}")
            print(f"Num comparisons: {comparisons}")
            
if __name__ == "__main__":
    main()
    
    # Import and run tests
    import testComplexity
    testComplexity.test_runtime_complexity()