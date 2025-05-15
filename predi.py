import numpy as np
import matplotlib.pyplot as plt

# Sample data: Hours studied vs. Exam scores
hours = np.array([1, 2, 3, 4, 5])
scores = np.array([50, 55, 65, 70, 75])

# Step 1: Calculate the slope (m) and intercept (c)
mean_x = np.mean(hours)
mean_y = np.mean(scores)

# Slope (m)
numerator = np.sum((hours - mean_x) * (scores - mean_y))
denominator = np.sum((hours - mean_x)**2)
m = numerator / denominator

# Intercept (c)
c = mean_y - (m * mean_x)

print(f"Model: y = {m:.2f}x + {c:.2f}")

# Step 2: Predict for a new student who studied 6 hours
new_hours = 6
predicted_score = m * new_hours + c
print(f"Predicted score for 6 hours of study: {predicted_score:.2f}")

# (Optional) Step 3: Plot the data and prediction
plt.scatter(hours, scores, color='blue', label='Actual Scores')
plt.plot(hours, m * hours + c, color='red', label='Regression Line')
plt.scatter(new_hours, predicted_score, color='green', label='Prediction (6 hrs)')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Predictive Analytics Example using NumPy')
plt.legend()
plt.grid(True)
plt.show()