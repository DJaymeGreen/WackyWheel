"""D Jayme Green
Many part of this files' code is attributed to other coders
"""


class EmptyNode():
    __slots__ = ()

class Node():
    __slots__ = ('previous', 'data','next')

def mkEmptyNode():
    return EmptyNode()

def mkNode(previous, data, next):
    node = Node()
    node.previous = previous
    node.next = next
    node.data = data
    return node

class myList():
    __slots__ = ('size','cursor')

def mkList():
    """Creates a new, epmty list instance, the cursor
    is pointing to the empty node"""
    lst = myList()
    lst.size = 0
    lst.cursor = mkEmptyNode()
    return lst

def printList(lst):
    """print the elements in the list instance, printing the cursor
    first, followed by every other item, moving forward"""
    for i in range (0, lst.size+5):
        print(lst.cursor.data)
        forward(lst)

def add(lst,element):
    """adds the element to the list, after the cursor(the new element
    should follow clockwise immediately after the cursor element). The
    cursor is not adjusted by the add function. Adding to an empty list
    results in a list with a single element and the cursor point to that
    single element"""
    if lst.size < 1:
        lst.cursor = mkNode(mkEmptyNode(), element, mkEmptyNode())
    else:
        lst.cursor.next = mkNode(lst.cursor, element, lst.cursor.next)
    lst.size += 1
    return lst

def addLast(lst,element):
    """Adds last element to make it ciruclar"""
    prevNode = lst.cursor
    for i in range(0, lst.size-1):
        lst.cursor = lst.cursor.previous
    lst.cursor.previous = mkNode(prevNode, element, lst.cursor)
    nextNode = lst.cursor.previous
    for i in range (0, lst.size-1):
        lst.cursor = lst.cursor.next
    lst.cursor.next = nextNode
    return lst

def forward(lst):
    """moves the cursor to the next item in the list"""
    lst.cursor = lst.cursor.next

def backward(lst):
    """moves the cursor to the previous item in the list"""
    lst.cursor = lst.cursor.previous

def getNext(lst):
    """returns the value of the item in front of the cursor node. Does
    NOT move the cursor"""
    return (lst.cursor.next)

def getPrev(lst):
    """returns the value of the item behind the cursor node. Does NOT
    move the cursor"""
    return (lst.cursor.previous)

def remove(lst):
    """removes the element at the cursor position, moves cursor position
    to previous position"""
    if lst.size == 0:
        print("Can't remove anything from an empty list")
    elif lst.size == 1:
        lst.cursor = mkEmptyNode()
    else:
        nextNode = lst.cursor.next
        prevNode = lst.cursor.previous
        lst.cursor = lst.cursor.previous
        prevNode.next = nextNode
        nextNode.previous = prevNode
    lst.size -= 1
        

def size(lst):
    """Returns the size of the list"""
    return lst.size
