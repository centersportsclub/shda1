class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, arr: list[int] | None) -> None:
        self.head = None
        if arr:
            for elem in arr:
                self.append(elem)

    def append(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def prepend(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert(self, val: int, index: int) -> None:
        if index == 0:
            self.prepend(val)
            return

        curr = self.head
        for _ in range(index - 1):
            if not curr:
                return
            curr = curr.next

        node = Node(val)
        node.next = curr.next
        curr.next = node

    def search(self, val: int) -> Node | None:
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None

    def pop_head(self) -> Node | None:
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def pop_tail(self) -> Node | None:
        if not self.head:
            return None

        if not self.head.next:
            temp = self.head
            self.head = None
            return temp

        curr = self.head
        while curr.next.next:
            curr = curr.next

        temp = curr.next
        curr.next = None
        return temp

    def delete_node(self, node: Node) -> Node | None:
        if not self.head:
            return None

        if self.head == node:
            return self.pop_head()

        curr = self.head
        while curr.next and curr.next != node:
            curr = curr.next

        if curr.next == node:
            temp = curr.next
            curr.next = curr.next.next
            return temp

        return None

    def sort_llist(self) -> None:
        # Simple bubble sort (for learning)
        if not self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            curr = self.head

            while curr.next:
                if curr.val > curr.next.val:
                    curr.val, curr.next.val = curr.next.val, curr.val
                    swapped = True
                curr = curr.next

    def __reversed__(self):
        prev = None
        curr = self.head

        while curr:
            new_node = Node(curr.val)
            new_node.next = prev
            prev = new_node
            curr = curr.next

        reversed_list = LinkedList(None)
        reversed_list.head = prev
        return reversed_list

    def __len__(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def __str__(self):
        curr = self.head
        list_str = ""
        while curr:
            list_str += f"{curr.val} -> "
            curr = curr.next
        return list_str


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list = LinkedList(arr)

    print("Original:", linked_list)
    print("Length:", len(linked_list))

    # Reverse using magic method
    rev_list = reversed(linked_list)
    print("Reversed:", rev_list)

    # Sorting (just to test)
    linked_list.sort_llist()
    print("Sorted:", linked_list)