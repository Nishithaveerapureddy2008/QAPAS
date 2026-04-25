# analytics.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([60, 70, 80, 90])

print("Average:", np.mean(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))

df = pd.DataFrame({"Students": ["A", "B", "C", "D"], "Marks": scores})

# Bar chart
plt.bar(df["Students"], df["Marks"])
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("bar_chart.png")
plt.show()