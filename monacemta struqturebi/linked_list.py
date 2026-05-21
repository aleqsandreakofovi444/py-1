class Node:
    """ხის კვანძი"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """დაკავშირებული სია (LinkedList)"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """ელემენტის დამატება ბოლოში"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        """სიის ელემენტების ჩვენება"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")
    
    def search(self, element):
        """
        ელემენტის ძებნა და წაშლა
        
        Args:
            element: ძებნის ელემენტი
        
        Returns:
            True თუ ელემენტი იპოვა და წაიშალა, False თუ ელემენტი არ იპოვა
        """
        # თუ სიის დასაწყისი ცარიელია
        if not self.head:
            return False
        
        # თუ პირველი ელემენტი ემთხვევა
        if self.head.data == element:
            self.head = self.head.next
            return True
        
        # დანარჩენი ელემენტების ძებნა
        current = self.head
        while current.next:
            if current.next.data == element:
                current.next = current.next.next
                return True
            current = current.next
        
        # ელემენტი არ იპოვა
        return False


# ტესტირება
if __name__ == "__main__":
    # LinkedList-ის შექმნა
    linked_list = LinkedList()
    
    # ელემენტების დამატება
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)
    
    print("თავდაპირველი სია:")
    linked_list.display()
    
    # ელემენტის წაშლა (search მეთოდით)
    print("\n20-ის ძებნა და წაშლა:")
    result = linked_list.search(20)
    print(f"შედეგი: {result}")
    linked_list.display()
    
    # ელემენტის წაშლა (search მეთოდით)
    print("\n10-ის ძებნა და წაშლა:")
    result = linked_list.search(10)
    print(f"შედეგი: {result}")
    linked_list.display()
    
    # ელემენტის წაშლა (search მეთოდით)
    print("\n50-ის ძებნა და წაშლა:")
    result = linked_list.search(50)
    print(f"შედეგი: {result}")
    linked_list.display()
    
    # არაარსებული ელემენტის ძებნა
    print("\n100-ის ძებნა (ელემენტი არ არსებობს):")
    result = linked_list.search(100)
    print(f"შედეგი: {result}")
    linked_list.display()
