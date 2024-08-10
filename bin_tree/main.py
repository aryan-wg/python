from node import node

head = None
while(True):
    op = int(input("""
          Enter 1 to add a new node - 
          Enter 2 to print in order -
          Enter 3 to print pre order -
          Enter 4 to print post order -
          Enter 5 to delete a node -
          Enter 0 to quit - 
          """))
    if op == 1:
        val = int(input("Enter the value you want to put in this node"))
        if head == None:
            head = node(val)
        else:
            if head.insert_node_in_bst(head,val):
                print("Node created")
            else:
                print("Node could not be created")

    elif op == 2:
        print("In order traversal of the tree is ")
        head.in_order()

