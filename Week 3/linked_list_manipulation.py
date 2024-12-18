class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def add_last(self, key):
        if self.contains(key):
            return
        new_node = Node(key)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def add_first(self, key):
        if self.contains(key):
            return
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, new_key, existing_key):
        if self.contains(new_key):
            return
        current = self.head
        while current:
            if current.data == existing_key:
                new_node = Node(new_key)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def add_before(self, new_key, existing_key):
        if self.contains(new_key) or not self.contains(existing_key):
            return
        new_node = Node(new_key)
        if self.head.data == existing_key:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.data == existing_key:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def remove(self, key):
        if not self.contains(key):
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" ".join(result))

# Đọc input
n = int(input())
keys = list(map(int, input().split()))

# Tạo danh sách liên kết với các khóa ban đầu
ll = LinkedList()
for key in keys:
    ll.add_last(key)

# Thực hiện các lệnh
while True:
    command = input().strip()
    if command == '#':
        break
    cmd = command.split()
    if cmd[0] == 'addlast':
        ll.add_last(int(cmd[1]))
    elif cmd[0] == 'addfirst':
        ll.add_first(int(cmd[1]))
    elif cmd[0] == 'addafter':
        ll.add_after(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'addbefore':
        ll.add_before(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'remove':
        ll.remove(int(cmd[1]))
    elif cmd[0] == 'reverse':
        ll.reverse()

# Xuất kết quả
ll.print_list()
