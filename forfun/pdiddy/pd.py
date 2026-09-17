from pandas import DataFrame, read_csv

# d = DataFrame(
#     [[1, 2, 3], [2, 3, 4], [4, 5, 6]],
#     index=["Lee", "Aaron", "John"],
#     columns=["C0", "C1", "C2"],
# )
d = read_csv("data.csv")

print(d)
