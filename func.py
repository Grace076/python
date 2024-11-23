def calculate_discount(price, discount_percent):
  
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Return the final price after applying the discount
        return price - discount_amount
    else:
        # Return the original price
        return price

#2 usage
original_price = 100.0  # Original price in currency
discount = 25.0         # Discount percentage
final_price = calculate_discount(original_price, discount)

print(f"Original Price: ${original_price}")
print(f"Discount Percentage: {discount}%")
print(f"Final Price: ${final_price}")


