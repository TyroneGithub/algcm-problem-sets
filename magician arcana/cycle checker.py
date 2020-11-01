# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    hasCycle = False
    
    tortoise = hare = head
    
    while hare.next is not None and hare.next.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        
        if tortoise == hare:
            hasCycle = True
            break
            
    return 1 if hasCycle else 0
    
    