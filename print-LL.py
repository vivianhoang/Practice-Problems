# Sample Input

# This example uses the following two linked lists:

# NULL  
# 1->2->3->NULL

# NULL and Node 1 are the two head nodes passed as arguments to Print(Node* head).

# Note: In linked list diagrams, -> describes a pointer to the next node in the list.

# Sample Output

# 1
# 2
# 3

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""

def print_list(head):
    if not head:
        return
        
    current = head
    
    while current is not None:
        print current.data
        current = current.next
    