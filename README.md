### Types of LinkedLists

- Doubly Linked Lists
- Singly Linked Lists
- Circular Linked Lists

### Structure

- Every linked list consists of nodes, Every node has two components:

1. Data
2. Next

- The data component allows the linked list to store an element of data that can be of type string, character, number or any type of object.
- The next node in every node is a pointer that points from one node to another.
- The start of the linked list is reffered to as the **head** which is pointer that points to the beginning of the linked list, if you want to traverse the linked to obtain or access an element of the linked list, you'll have to start from head and move along.
- The last component of a singly linked list is a notion of null, null terminates the linked list,the last node in a singly linked list points to a null object, and that is the end of the linked list.

## Arrays vs Linked Lists

| Endpoint                                                  | Array  | Linked Lists |
| --------------------------------------------------------- | ------ | ------------ |
| Insertion/Deletion at begging of the array or linked list | O(_n_) | O(1)         |
| Access element                                            | O(1)   | O(n)         |
| Contagious Memory                                         | Yes    | No           |

### Insertion/Deletion

- The insertion/deletion operation is in O(n) operations for insertion/deletion of a value at the beginning of an array, if we insert a value at the beginning of any array, we have to move the others others one position to the right, due to the shifting, the time complexity is O(_n_), same case with deletion, we have to move back by one index, this operation has a time complexity of O(_n_).

- Inserting a node at the head of a linked list given the head node is a constant time operation since we just need to change the orientation of a few pointers, if we are given the exact pointer after which we have to insert another node, it will be constant time operation.

## Accessing Elements

- Accessing elements given an index in arrays is better than accesing elements i.e nth element in a linked list, in array this is a constant time operation, in a linked list, you have to access the head node of a linked list, if we want to access an element, we have to start from the head pointer and traverse the entire linked list.

# Contiguous Memory

Arrays are contiguous in memory which allows the access time to be constant, whereas, in linked lists, you do not have the luxury of contiguous memory.

# Implementation

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

We create a class called Node. In the constructor of this class, we give the argument of self and data on line 2. Every node is going to consist of data and next. We define self.data equal to data that is passed into the constructor of the object of class Node (line 3). We set self.next equal to None on line 4. This is something that we’ll set again as we make use of the node, but for now, we just set it to None. That’s pretty much all we need for the Node class right now.

On line 6, we define a LinkedList class, and in the constructor, we again pass self. On line 8, we define the head pointer, which will point to the first node in the linked list. Initially, we just set it equal to None.

## Append

- The append method will insert an element at the end of the linked list.
