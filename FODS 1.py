import numpy as np

student_scores = np.array([
    [70, 85, 78, 90],
    [88, 90, 85, 92],
    [80, 78, 82, 85],
    [95, 88, 91, 89]
])

subjects = ['Math', 'Science', 'English', 'History']

# Calculate and store in a dictionary
avg_dict = {subjects[i]: np.mean(student_scores[:, i]) for i in range(4)}

# Print nicely
for subj, avg in avg_dict.items():
    print(f"{subj} average: {avg:.2f}")

# Get subject with max average
best = max(avg_dict, key=avg_dict.get)
print(f"\nHighest average is in: {best}")

