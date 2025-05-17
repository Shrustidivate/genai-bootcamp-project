# day5_matplotlib_charts.py

import matplotlib.pyplot as plt

categories = ['Math', 'Science', 'History']
scores = [241, 258, 0]

plt.bar(categories, scores, color='skyblue')
plt.title("Total Scores by Category")
plt.xlabel("Category")
plt.ylabel("Total Score")
plt.savefig("category_scores.png")
plt.show()
