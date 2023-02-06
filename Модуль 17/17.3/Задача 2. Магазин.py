original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_list = [(original_prices[i] if original_prices[i] > 0 else 0) for i in range(len(original_prices))]
print(new_list)