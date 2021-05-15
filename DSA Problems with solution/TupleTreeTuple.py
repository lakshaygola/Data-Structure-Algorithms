# Class to define the single node of the tree
class tree_node():
    def __init__(self, key, left= None, right= None):
        self.key= key
        self.left= left
        self.right= right

    # Function to change the tuple into binary tree
    def tuple_tree(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = tree_node(data[1])
            node.left = tree_node.tuple_tree(data[0])
            node.right = tree_node.tuple_tree(data[2])
        elif data is None:
            node = None
        else:
            node = tree_node(data)
        return node

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
        tree_node.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        tree_node.display_keys(node.left, space, level + 1)

    # Function to find out the height of the tree
    def tree_height(node):
        left_height, right_height = 0, 0
        if node is None:
            return 0
        else:
            return 1 + max(tree_node.tree_height(node.left), tree_node.tree_height(node.right))

    # Function to remove the None values from the list
    def none_remover(keys):
        return [x for x in keys if x is not None]

    # Function to check that tree in binary or not
    def is_bst(node):
        if node is None:
            return True, None, None

        is_bst_l, min_l, max_l = tree_node.is_bst(node.left)
        is_bst_r, min_r, max_r = tree_node.is_bst(node.right)

        is_node_bst = (is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (
                    min_r is None or node.key < min_r))

        min_key = min(tree_node.none_remover([min_l, min_r, node.key]))
        max_key = max(tree_node.none_remover([max_l, max_r, node.key]))

        return is_node_bst, min_key, max_key

    # Function for inplace-order traversal of the tree
    def inplace(node):
        if node is None:
            return []
        return (tree_node.inplace(node.left) + [node.key] + tree_node.inplace(node.right))

    # Function for pre-order traversal of the tree
    def preorder(node):
        if node is None:
            return []
        return ([node.key] + tree_node.preorder(node.left) + tree_node.preorder(node.right))

    # Function for the post-order traversal of the tree
    def postorder(node):
        if node is None:
            return []
        return (tree_node.postorder(node.left) + tree_node.postorder(node.right) + [node.key])



if __name__ == '__main__':
    
    # This is a tuple which we will convert into the binary tree
    keys = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    # Lets convert the tree_tuple tuple into tree
    Btree = tree_node.tuple_tree(keys)

    print('Right key of the tree: ',Btree.right.right.right.key)
    # Calling function to display the binary tree
    tree_node.display_keys(Btree, ' ')
    # Height of the Binary Tree
    print('Height of the Binary Tree: ', tree_node.tree_height(Btree))
    # Converting tree back into tuple
    print('Elements of the tree (inorder Traversal): ', tree_node.inplace(Btree))
    print('Elements of the tree (preorder Traversal): ', tree_node.preorder(Btree))
    print('Elements of the tree (postorder Traversal): ', tree_node.postorder(Btree))




