class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:  # add to left subtree
            if self.left:  # if there is a left subtree, recurse it and add
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:  # add to right subtree
            if self.right:  # if there is a right subtree, recurse it and add
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

# ----------------------Traversals-----------------------------------------------

    def inorder_traversal(self):
        elements = []

        if self.left:  # traverse through the left wing
            elements += self.left.inorder_traversal()

        elements.append(self.data)  # take the middle root value

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def preorder_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

# ---------------------Methods--------------------------------------

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):

        if self.left:
            # minimum = self.left.data
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):

        if self.right:
            return self.right.find_max()
        else:
           return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

# Helper function to built tree
def built_tree(inp_elemets):
    print("Building Binary Search Tree with elements:", inp_elemets)

    root = BinarySearchTree(inp_elemets[0])
    for i in range(1, len(inp_elemets)):
        root.add_child(inp_elemets[i])

    return root


if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    number_tree = built_tree(numbers)
    #
    # print("Preorder Traversal: ", number_tree.preorder_traversal())
    # print("Inorder Traversal: ", number_tree.inorder_traversal())
    # print("Postorder Traversal: ", number_tree.postorder_traversal())

    # print(number_tree.search(20))
    # print(number_tree.find_min())
    # print(number_tree.find_max())
    # print(number_tree.calculate_sum())

    # number_tree.delete(20)
    # print("After deleting 20 ", number_tree.inorder_traversal())
    #
    # number_tree = built_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # number_tree.delete(9)
    # print("After deleting 9 ", number_tree.inorder_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    number_tree = built_tree([17, 4, 1, 20, 9, 23, 18, 34])
    number_tree.delete(17)
    print("After deleting 17 ", number_tree.inorder_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
# --------------------------------------------------------------------------------------------------

    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    # country_tree = built_tree(countries)
    # print('Preorder Traversal:',country_tree.preorder_traversal())
    # print('Inorder Traversal:',country_tree.inorder_traversal())
    # print('Postorder Traversal:',country_tree.postorder_traversal())
    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))
    # print(country_tree.find_min())
    # print(country_tree.find_max())


    pass
