#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(3)
sll.sorted_insert(-5)
sll.sorted_insert(-5)
sll.sorted_insert("4")
print(sll)
