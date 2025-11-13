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

def counting_sort_by_pages(self) -> None:
        if self.head is None:
            return
        
        # Находим диапазон страниц
        min_node = self.find_min_pages()
        max_node = self.find_max_pages()
        min_pages = min_node.data.pages
        max_pages = max_node.data.pages
        
        range_size = max_pages - min_pages + 1
        count = [0] * range_size
        
        # Подсчет частот
        current = self.head
        while current:
            count[current.data.pages - min_pages] += 1
            current = current.next
        
        # Для сортировки по убыванию накапливаем с конца
        for i in range(range_size - 2, -1, -1):
            count[i] += count[i + 1]
        
        # Создаем массив для результата
        result = [None] * self.get_depth()
        
        # Заполняем результат в убывающем порядке
        current = self.head
        while current:
            pages = current.data.pages
            position = count[pages - min_pages] - 1
            result[position] = current.data
            count[pages - min_pages] -= 1
            current = current.next
        
        # Обновляем список
        current = self.head
        for book in result:
            current.data = book
            current = current.next