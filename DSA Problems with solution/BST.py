# Class user which help you to build the object of the user
class User():
    def __init__(self, name, email, phone_num):
        self.name= name
        self.email= email
        self.phone_no= phone_num

    def __repr__(self):                      # __repr__ function is used to represent the object as a string
        return "Name: {}, Email_ID: {}, Phone_number: {}".format(self.name, self.email, self.phone_no)

    def __str__(self):                       # __str__ function is used to represent the object as a string
        return "User(Name: {}, Email_ID: {}, Phone_number: {})".format(self.name, self.email, self.phone_no)


# Class of the node structure of the BST in which we have keys and values pair
class bst():
    def __init__(self, key, value):
        self.key= key
        self.value= value
        self.left= None
        self.right= None


# Function to remove the None values from the list
    def none_remover(keys):
        return [x for x in keys if x is not None]

# Function to check that tree in binary or not
    def is_bst(node):
        if node is None:
            return True, None, None

        is_bst_l, min_l, max_l = bst.is_bst(node.left)
        is_bst_r, min_r, max_r = bst.is_bst(node.right)

        is_node_bst = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (
                min_r is None or node.key < min_r))

        min_key = min(bst.none_remover([min_l, min_r, node.key]))
        max_key = max(bst.none_remover([max_l, max_r, node.key]))

        return is_node_bst, min_key, max_key

    def tree_height(node):
        left_height, right_height = 0, 0
        if node is None:
            return 0
        else:
            return 1 + max(bst.tree_height(node.left), bst.tree_height(node.right))

# Function to display the tree
    def display_keys(node, space='\t', level=0):
        # print(node.key if node else None, level)

        # If the node is empty
        if node is None:
            print(space * level + '∅')
            return

            # If the node is a leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return

        # If the node has children
        bst.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        bst.display_keys(node.left, space, level + 1)

    # Function to insert the node in the tree
    def insert(tree, key, value):
            if tree is None:
                tree= bst(key, value)
            elif tree.key < key:
                tree.right= bst.insert(tree.right, key, value)
                tree.right.parent= tree
            elif tree.key > key:
                tree.left= bst.insert(tree.left, key, value)
                tree.left.parent= tree
            return tree

    # Function to serach the particular node
    def find_key(tree, key):
        if tree is None:
            return None
        elif tree.key == key:
            return tree
        elif tree.key < key:
            return bst.find_key(tree.right, key)
        else:
            return bst.find_key(tree.left, key)

    # Function to update the value of the object
    def update_key(tree, key, value):
        target= bst.find_key(tree, key)
        if target is None:
            return None
        target.value = value

    # Function to list all the object of the class
    def list_all(tree):
        if tree is None:
            return []
        return bst.list_all(tree.left) + [(tree.key, tree.value)] + bst.list_all(tree.right)

    # Function to check weather tree is balance or not
    def is_balance_tree(tree):
        if tree is None:
            return True, 0
        balance_l, height_l= bst.is_balance_tree(tree.left)
        balance_r, height_r= bst.is_balance_tree(tree.right)
        balance= (balance_l and balance_r) and abs(height_l - height_r) <= 1
        height= bst.tree_height(tree)
        return  balance, height

    # Function to  make balance binary search tree
    def make_balance_bst(data, lo= 0, hi= None, parent= None):
        if hi is None:
            hi= len(data)-1
        if lo > hi:
            return None

        mid= (lo+hi) // 2
        key, value= data[mid]
        node= bst(key, value)
        node.parent= parent
        node.left= bst.make_balance_bst(data, lo, mid-1, node)
        node.right= bst.make_balance_bst(data, mid+1, hi,node)

        return node

# Object of the user class
vishal = User('vishal',  'vishal@example.com', 9874563)
hemanth = User('hemanth', 'hemanth@example.com', 78965)
jadhesh = User('jadhesh', 'jadhesh@example.com',741258)
siddhant = User('siddhant', 'siddhant@example.com',8564123)
biraj = User('biraj', 'biraj@abc.com',84123)
aakash= User('aakash', 'aakash@123.in', 32105)
nikil= User('nikil', 'rockstar@night.com', 5687)
users= [vishal, hemanth, jadhesh, siddhant, biraj, aakash, nikil]


# Creating the tree for the object of the class user
print('\nTree 0\n')
tree0= bst(jadhesh.name, jadhesh)
tree0.left= bst(siddhant.name, siddhant)
tree0.right= bst(vishal.name, vishal)
tree0.display_keys()

print('\nTree 1 BST\n')
tree1= bst.insert(None, jadhesh.name, jadhesh)
bst.insert(tree1, siddhant.name, siddhant)
bst.insert(tree1, hemanth.name, hemanth)
bst.insert(tree1, vishal.name, vishal)
bst.insert(tree1, biraj.name, biraj)
bst.insert(tree1, aakash.name, aakash)
bst.insert(tree1, nikil.name, nikil)
tree1.display_keys()

new_obj= bst.update_key(tree1, 'biraj', User('biraj', 'biraj@wtf.in', 7840315))
tree1.display_keys()

obj= bst.find_key(tree1, 'biraj')
print('\n', obj.key, obj.value)

obj_list= tree1.list_all()
print(obj_list)

result= tree1.is_balance_tree()
print('Is this tree1 is balance or not: ', result[0], '\nHeight of the Tree: ', result[1])


data= [(x.name, x) for x in users]
print(data)
btree= bst.make_balance_bst(data)
print('\nBalance Binary Tree\n')
btree.display_keys()
print('\n')
print(btree.is_balance_tree())



