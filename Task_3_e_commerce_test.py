class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def quicksort_products(products, ascending=True):
    if len(products) <= 1:
        return products

    pivot = products[len(products) // 2]
    left = [product for product in products if (product.price < pivot.price) ascending else (product.price > pivot.price)]

    middle = [product for product in products if product.price == pivot.price]
    right = [product for product in products  if (product.price > pivot.price)  ascending else (product.price < pivot.price)]

    return quicksort_products(left, ascending) + middle + quicksort_products(right, ascending)

# Example usage:
if __name__ == "__main__":
    products = [
        Product("Product A", 25.99),
        Product("Product B", 10.99),
        Product("Product C", 5.99),
        Product("Product D", 15.99),
    ]

    ascending_sorted_products = quicksort_products(products, ascending=True)
    descending_sorted_products = quicksort_products(products, ascending=False)

    print("Ascending order:")
    for product in ascending_sorted_products:
        print(f"{product.name}: {product.price}")

    print("\nDescending order:")
    for product in descending_sorted_products:
        print(f"{product.name}: {product.price}")
