class node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def append_node(val,tail):
    new_node = node(val)
    if not tail == None :
        tail.next = new_node
    tail = new_node
    return tail

def read_entire_list(head):
    while head.next!=None:
        print(head.val)
        head = head.next

def main():
    while True:
        op = input("""Enter a to append a node
            Enter A to insert node at a position
            Enter d to delete a node from front
            Enter D to delete a node from a position rear
            Enter r to read entire list\n""")
        if op == 'x':
            break
        elif op == 'a':
            val = input("Enter the value of the node\n")
            tail = append_node(val,tail)
        elif op == 'd':
            
