class node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

    def add_left(self,ptr):
        self.left = ptr

    def add_right(self,ptr):
        self.right = ptr

    def insert_node_in_bst(self,head,val):
        temp = head
        while not temp.left == None and temp.right == None:
            while(temp.value>val):
                if not temp.left == None:
                    temp = temp.left
                else:
                    break
            while(temp.value<val):
                if not temp.right == None:
                    temp = temp.right
                else:
                    break
        try:
            if temp.value == val:
                raise ValueError("This element already exists")
            elif temp.value>val:
                temp.left == node(val)
                return True
            elif temp.value<val:
                temp.right == node(val)
                return True
        except ValueError as error:
            print(str(error))
            pass
    def in_order(head):
        temp = head
        if temp == None:
            return 
        else 
            print(in_order(temp.left))
            print(temp.value)
            print(in_order(temp.right))

    
            
