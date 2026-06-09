import pytest
from orders import process_orders


class TestProcessOrders:
    """process_orders ფუნქციის ტესტები"""
    
    # ა. პროდუქტის არსებობის ტესტი
    def test_product_not_found_in_inventory(self):
        """ტესტი: პროდუქტი არ არის საწყობში"""
        orders = [{"product": "banana", "quantity": 5}]
        inventory = {"apple": 10, "orange": 3}
        
        with pytest.raises(ValueError, match="Product 'banana' not found in inventory"):
            process_orders(orders, inventory)
    
    def test_multiple_products_one_not_found(self):
        """ტესტი: რამდენიმე ორდერიდან ერთი პროდუქტი არ არის საწყობში"""
        orders = [
            {"product": "apple", "quantity": 2},
            {"product": "banana", "quantity": 5}
        ]
        inventory = {"apple": 10}
        
        with pytest.raises(ValueError, match="Product 'banana' not found in inventory"):
            process_orders(orders, inventory)
    
    
    # ბ. საკმარისი ოდენობის ტესტი
    def test_not_enough_stock(self):
        """ტესტი: საკმარისი ოდენობა არ არის"""
        orders = [{"product": "apple", "quantity": 15}]
        inventory = {"apple": 10}
        
        with pytest.raises(ValueError, match="Not enough stock for 'apple'"):
            process_orders(orders, inventory)
    
    def test_not_enough_stock_exact_match_fails(self):
        """ტესტი: მოთხოვნილი ოდენობა სტეკზე მეტია"""
        orders = [{"product": "orange", "quantity": 6}]
        inventory = {"orange": 5}
        
        with pytest.raises(ValueError, match="Not enough stock for 'orange'"):
            process_orders(orders, inventory)
    
    def test_multiple_orders_insufficient_stock_on_second(self):
        """ტესტი: პირველი ორდერი წარმატებული, მეორეში საკმარისი ოდენობა არ არის"""
        orders = [
            {"product": "apple", "quantity": 5},
            {"product": "apple", "quantity": 10}  # მხოლოდ 5 დარჩა
        ]
        inventory = {"apple": 15}
        
        with pytest.raises(ValueError, match="Not enough stock for 'apple'"):
            process_orders(orders, inventory)
    
    
    # გ. საწყობის ოდენობის სწორად შემცირების ტესტი
    def test_inventory_reduced_correctly(self):
        """ტესტი: საწყობის ოდენობა სწორად შემცირდა"""
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"apple": 10}
        
        process_orders(orders, inventory)
        
        assert inventory["apple"] == 5, "საწყობის ოდენობა უნდა იყოს 5"
    
    def test_multiple_orders_inventory_reduced_correctly(self):
        """ტესტი: რამდენიმე ორდერის შემდეგ საწყობი სწორად შემცირდა"""
        orders = [
            {"product": "apple", "quantity": 3},
            {"product": "apple", "quantity": 2},
            {"product": "orange", "quantity": 1}
        ]
        inventory = {"apple": 10, "orange": 5}
        
        process_orders(orders, inventory)
        
        assert inventory["apple"] == 5, "apple-ის ოდენობა უნდა იყოს 5"
        assert inventory["orange"] == 4, "orange-ის ოდენობა უნდა იყოს 4"
    
    def test_inventory_zero_after_all_stock_taken(self):
        """ტესტი: საწყობი ხდება 0, როდესაც ყველა პროდუქტი აღებულია"""
        orders = [{"product": "apple", "quantity": 10}]
        inventory = {"apple": 10}
        
        process_orders(orders, inventory)
        
        assert inventory["apple"] == 0, "საწყობი უნდა იყოს 0"
    
    
    # დამატებითი ტესტები: წარმატებული ორდერებიანის დაბრუნება
    def test_successful_orders_returned(self):
        """ტესტი: წარმატებული ორდერები სწორად დაბრუნდა"""
        orders = [
            {"product": "apple", "quantity": 5},
            {"product": "orange", "quantity": 2}
        ]
        inventory = {"apple": 10, "orange": 5}
        
        result = process_orders(orders, inventory)
        
        assert len(result) == 2, "დაბრუნებული ორდერების რაოდენობა უნდა იყოს 2"
        assert result == orders, "დაბრუნებული ორდერები უნდა იყოს იგივე"
    
    def test_single_successful_order(self):
        """ტესტი: ერთი წარმატებული ორდერი"""
        orders = [{"product": "apple", "quantity": 3}]
        inventory = {"apple": 10}
        
        result = process_orders(orders, inventory)
        
        assert len(result) == 1
        assert result[0]["product"] == "apple"
        assert result[0]["quantity"] == 3
    
    def test_empty_orders_list(self):
        """ტესტი: ცარიელი ორდერების სია"""
        orders = []
        inventory = {"apple": 10}
        
        result = process_orders(orders, inventory)
        
        assert result == []
        assert inventory["apple"] == 10, "საწყობი არ უნდა შეიცვალოს"
    
    def test_exact_quantity_match(self):
        """ტესტი: მოთხოვნილი ოდენობა ზუსტად ემთხვევა საწყობის ოდენობას"""
        orders = [{"product": "apple", "quantity": 10}]
        inventory = {"apple": 10}
        
        result = process_orders(orders, inventory)
        
        assert len(result) == 1
        assert inventory["apple"] == 0
