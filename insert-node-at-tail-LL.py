# You are given the pointer to the head node of a linked list and an integer to add to the list.
# Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node.
# The given head pointer may be null, meaning that the initial list is empty.

# Input Format 
# You have to complete the Node* Insert(Node* head, int data) method. It takes two arguments:
# the head of the linked list and the integer to insert. You should not read any input from the stdin/console.

# Output Format 
# Insert the new node at the tail and just return the head of the updated linked list. Do not print anything to stdout/console.

# Sample Input

# NULL, data = 2
# 2 --> NULL, data = 3

# Sample Output

# 2 -->NULL
# 2 --> 3 --> NULL

"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    new_node = Node(data)
    
    if not head:
        head = new_node
        return head
    
    current = head
    
    while current is not None:
        if current.next == None:
            current.next = new_node
            return head
        else:
            current = current.next
            