#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
#
#     def print_tree(self):
#         space = " " * self.get_level() * 3
#         prefix = space + "|__" if self.parent else ""
#         print(prefix + self.data)
#         for child in self.children:
#             child.print_tree()
#
#
# def bulit_tree():
#     root = TreeNode("Electronics")
#
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))
#
#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))
#
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))
#
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#
#     root.print_tree()
#
#
# if __name__ == '__main__':
#     bulit_tree()
#
#
# -----------------Problem 1------------------

# class TreeNode:
#     def __init__(self, n, d):
#         self.data = {
#             "name": n,
#             "designation": d
#         }
#         self.children = []
#         self.parent = None
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
#
#     def print_tree(self,type):
#         space = " " * self.get_level() * 3
#         prefix = space + "|__" if self.parent else ""
#         if type == "both":
#             print(f'{prefix} {self.data['name']} ({self.data["designation"]})')
#         else:
#             print(prefix + str(self.data[type]))
#         for child in self.children:
#             child.print_tree(type)
#
#
# def built_management_tree():
#     root = TreeNode('Nilpul', 'CEO')
#
#     ih = TreeNode('Viswa', "Infrastructure Head")
#     ih.add_child(TreeNode('Dhaval', 'Cloud Manager'))
#     ih.add_child(TreeNode('Abhijith', 'App Manager'))
#
#     cto = TreeNode('Chinmay','CTO')
#     cto.add_child(ih)
#     cto.add_child(TreeNode('Aamir','Application Head'))
#
#     hr = TreeNode("Gels","HR Head")
#     hr.add_child(TreeNode('Peter','Recruitment Manager'))
#     hr.add_child(TreeNode('Waqas','Policy Manager'))
#
#     root.add_child(cto)
#     root.add_child(hr)
#
#     return root
#
#
# if __name__ == '__main__':
#     root_node = built_management_tree()
#     root_node.print_tree("name")
#     root_node.print_tree("designation")
#     root_node.print_tree("both")

# ------------------------Problem 2-------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,lev):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        if self.get_level() <= lev:
            print(prefix + self.data)
            for child in self.children:
                child.print_tree(lev)
        else:
            return
def built_location_tree():
    root = TreeNode('Global')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))

    newjersey = TreeNode('New Jersey')
    newjersey.add_child(TreeNode('Princeton'))
    newjersey.add_child(TreeNode('Trenton'))

    california = TreeNode('California')
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))

    india = TreeNode('India')
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode('USA')
    usa.add_child(newjersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root_node = built_location_tree()
    root_node.print_tree(0)