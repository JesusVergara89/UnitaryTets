def calculate_total(products, discount=0):
    total=0
    for product in products:
        total+= product["price"] * (1-(discount/100))
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name" : "noteBook",
            "price" : 10
        }
    ]
    assert calculate_total(products,10) == 9

def test_calculate_total_with_multi_products():
    products = [
        {
            "name" : "noteBook",
            "price" : 10 
        },
        {
            "name" : "cellphone",
            "price" : 20
        },
        {
            "name" : "mouse",
            "price" : 15
        }
    ]
    assert calculate_total(products,20) == 36  
    

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multi_products()