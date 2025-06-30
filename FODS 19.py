import numpy as np
from scipy import stats

# Updated sample data
drug_group = np.array([11, 13, 12, 14, 15, 15, 16, 14, 13, 13,
                       12, 14, 13, 15, 16, 12, 13, 11, 14, 13,
                       14, 15, 16, 14, 12])

placebo_group = np.array([5, 4, 5, 3, 5, 6, 4, 4, 3, 5,
                          4, 3, 5, 4, 3, 4, 5, 3, 4, 4,
                          4, 4, 3, 5, 4])

def get_confidence_interval(arr, confidence=0.95):
    n = len(arr)
    mean = np.mean(arr)
    stderr = stats.sem(arr)
    margin = stats.t.ppf((1 + confidence) / 2, df=n-1) * stderr
    return mean, (mean - margin, mean + margin)

drug_mean, drug_ci = get_confidence_interval(drug_group)
placebo_mean, placebo_ci = get_confidence_interval(placebo_group)

print(f"Drug Group Mean: {drug_mean:.2f}")
print(f"Drug Group 95% CI: {drug_ci[0]:.2f} to {drug_ci[1]:.2f}")

print(f"\nPlacebo Group Mean: {placebo_mean:.2f}")
print(f"Placebo Group 95% CI: {placebo_ci[0]:.2f} to {placebo_ci[1]:.2f}")

print(f"\nMean Difference (Drug - Placebo): {drug_mean - placebo_mean:.2f}")
