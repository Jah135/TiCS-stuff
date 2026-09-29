import matplotlib.pyplot as plot
import pandas as pd

data = pd.read_csv("data.csv")

pathway_counts = data["Pathway"].value_counts()

# plot.pie(
#     pathway_counts,
#     labels=pathway_counts.index,
#     explode=[0.5, *(0,) * (len(pathway_counts) - 1)],
# )
plot.xlabel("Credits Completed")
plot.ylabel("GPA")
plot.scatter(data["Credits Completed"], data["GPA"])
plot.show()
