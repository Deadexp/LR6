class Book:
    def __init__(self, author: str, publisher: str, pages: int, price: int | float, isbn: str) -> None:
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.isbn = isbn

    def __repr__(self) -> str:
        return f"Book(author='{self.author}', publisher='{self.publisher}', pages={self.pages}, price={self.price}, isbn='{self.isbn}')"

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data: Book) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def get_depth(self) -> int:
        depth = 0
        current = self.head
        while current:
            depth += 1
            current = current.next
        return depth

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def find_max_pages(self) -> None | Node:
        if self.head is None:
            return None

        max_node = self.head
        current = self.head
        while current:
            if current.data.pages > max_node.data.pages:
                max_node = current
            current = current.next
        return max_node

    def find_min_pages(self) -> None | Node:
        if self.head is None:
            return None

        min_node = self.head
        current = self.head
        while current:
            if current.data.pages < min_node.data.pages:
                min_node = current
            current = current.next
        return min_node

