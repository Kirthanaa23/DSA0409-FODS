import numpy as np

# Quarterly revenue in dollars for a product line
quarterly_revenue = np.array([22000, 24500, 27000, 29500])

# Compute yearly total revenue
yearly_total = np.sum(quarterly_revenue)

# Calculate growth from Q1 to Q4
q1_revenue = quarterly_revenue[0]
q4_revenue = quarterly_revenue[-1]
growth_rate = round(((q4_revenue - q1_revenue) / q1_revenue) * 100, 2)

# Display output
print(f"Yearly Revenue: ${yearly_total}")
print(f"Growth from Q1 to Q4: {growth_rate}%")

#OUPUT
Yearly Revenue: $103000
Growth from Q1 to Q4: 34.09%
