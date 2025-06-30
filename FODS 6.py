# Prices and quantities of 3 different products
prices = [15.5, 9.75, 4.25]
units_sold = [4, 1, 6]

# Discount and tax in percentages
discount = 10  # 10%
tax = 8        # 8%

# Calculate item-wise total costs
line_totals = [price * qty for price, qty in zip(prices, units_sold)]
gross_total = sum(line_totals)

# Apply discount
discount_value = gross_total * (discount / 100)
net_total = gross_total - discount_value

# Apply tax
tax_value = net_total * (tax / 100)
grand_total = net_total + tax_value

# Output
print(f"Total before discount: ${gross_total:.2f}")
print(f"Discount applied: ${discount_value:.2f}")
print(f"Tax added: ${tax_value:.2f}")
print(f"Final amount to pay: ${grand_total:.2f}")

#OUTPUT
Total before discount: $100.25  
Discount applied: $10.03  
Tax added: $7.22  
Final amount to pay: $97.44
