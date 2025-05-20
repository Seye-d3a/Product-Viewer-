from objects import Product

def show_products(products):
    print("PRODUCTS AVAILABLE: ")
    for i, product in enumerate(products,start=1):
        print(f"{i}. {product.name}")
    print()

def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"Name:               {product.name}")
    print(f"Price:              {product.price:.2f}")
    print(f"Discount percent:   {product.discountPercent:d}%")
    print(f"Discount amount:    {product.getdiscountAmount():.2f}") #.2f denotes output should be rounded up to two decimal places.
    print(f"Discount price:     {product.getdiscountPrice():.2f}")

def list_products():
    return(Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
           Product('National Hardware 3/4" Wire Nails', 5.06, 0),
           Product("Economy Duct Tape, 60 yards, Silver", 7.24, 0))

def get_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                print("Product number out of range. Please try again.")
            else:
                return products[number-1]
        except ValueError:
            print("Invalid number. Please try again.")
        print() 

def main():
    print("The Product Viewer Program")
    print()

    products = list_products()
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        product = get_product(products)
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Done!")

if __name__ == "__main__":
    main()
