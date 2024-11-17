import matplotlib.pyplot as plt
from interweave import is_interweaving 

def test_runtime_complexity():
    x = "101"
    y = "0"
    input_sizes = [10, 20, 50, 100, 200, 500, 1000]
    comparisons_count = []

    for size in input_sizes:
        s = "1010" * (size // 4)  # Generate input string s with the required size
        _, comparisons = is_interweaving(s, x, y)
        comparisons_count.append(comparisons)

    # Plot the results
    plt.plot(input_sizes, comparisons_count, marker='o')
    plt.title("Comparisons vs Input Size")
    plt.xlabel("Length of s")
    plt.ylabel("Number of Comparisons")
    plt.grid(True)
    plt.show()