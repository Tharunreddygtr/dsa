class Binary_trees:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_binarytree(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print('L', root.left.data, end=",")
    if root.right != None:
        print('R', root.right.data)
    print_binarytree(root.left)
    print_binarytree(root.right)


def treeinput():  # root,left,right preorder  traversal
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = Binary_trees(rootdata)
    lefttree = treeinput()
    righttree = treeinput()
    root.left = lefttree
    root.right = righttree
    return root


def printnumberofnodes(root):
    if root == None:
        return 0
    return 1 + printnumberofnodes(root.left) + printnumberofnodes(root.right)


def sumofnodes(root):
    if root == None:
        return 0
    return root.data + sumofnodes(root.left) + sumofnodes(root.right)


def largestnode(root):
    if root == None:
        return 0
    max1 = root.data
    leftnode = largestnode(root.left)
    rightnode = largestnode(root.right)
    if leftnode > max1:
        max1 = leftnode
    if rightnode > max1:
        max1 = rightnode
    return max1


def fullbinarytree(root):  # 1
    if root == None:  # 2  #3
        return 0
    l = []
    l.append(root)
    count = 0
    while len(l) > 0:
        node = l.pop(0)
        if node.left is not None and node.right is not None:
            count += 1
        if node.left is not None:
            l.append(node.left)
        if node.right is not None:
            l.append(node.right)
        return count


def iternumberofnodes(root):
    if root == None:
        return 0
    l = []
    l.append(root)
    count = 1
    while len(l) > 0:
        node = l.pop(0)
        if node.left is not None:
            l.append(node.left)
            count += 1
        if node.right is not None:
            l.append(node.right)
            count += 1
        return count


def leafnodes(root):
    if root == None:
        return 0
    l = []
    l.append(root)
    while len(l) > 0:
        li = l.pop(0)
        if li.right == None and li.left == None:
            print(li.data)
        if li.right != None:
            l.append(li.right)
        if li.left != None:
            l.append(li.left)


def height_binarytree(root):
    if root == None:
        return 0
    else:
        lefttree = height_binarytree(root.left)
        righttree = height_binarytree(root.right)
        if lefttree > righttree:
            return lefttree + 1
        else:
            return righttree + 1


def maxnodedata(root):
    l = []
    l.append(root)
    max1 = root.data
    print(root.right.data)
    while len(l) > 0:
        l.pop(0)
        if root.left != None:
            l.append(root.left)
            if root.left.data > max1:
                max1 = root.left.data
        if root.right != None:
            l.append(root.right)
            if root.right.data > max1:
                max1 = root.right.data
    return max1


def nodegreaterthanx(root, x):
    if root == None:
        return -1
    if root.data > x:
        print(root.data)
    if root.left.data > x:
        print(root.left.data)
    if root.right.data > x:
        print(root.right.data)
    nodegreaterthanx(root.right, x)
    nodegreaterthanx(root.left, x)


def identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 != None and root2 != None:
        return (root1.data == root2.data) and identical(root1.left, root2.left) and identical(root1.right, root2.right)

    return False


def mirrortree(root):
    if root == None:
        return root
    root.left, root.right = root.right, root.left
    mirrortree(root.left)
    mirrortree(root.right)
    return root


def ismirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 != None and root2 != None:
        return root1.data == root2.data and ismirror(root1.left, root2.right) and ismirror(root1.right, root2.left)
    return False


def heightoftree(root):
    if root == None:
        return 0
    leftcount = heightoftree(root.left)
    rightcount = heightoftree(root.right)
    if leftcount >= rightcount:
        return leftcount + 1
    else:
        return rightcount + 1


def depthtree(root, k):
    if root != None:
        return 0
    root.data = k
    depthtree(root.left, k + 1)
    depthtree(root.right, k + 1)


def isnode(root, data):
    l = [root]
    while len(l) > 0:
        pop1 = l.pop(0)
        if pop1.data == data:
            return True
        if pop1.left != None:
            l.append(pop1.left)
            if pop1.left.data == data:
                return True
        if pop1.right != None:
            l.append(pop1.right)
            if pop1.right.data == data:
                return True
    else:
        return False


def nodeswithout_sibilings(root):
    if root == None:
        return
    if root.left != None and root.right != None:
        nodeswithout_sibilings(root.left)
        nodeswithout_sibilings(root.right)
    elif root.left != None:
        print(root.left.data)
        nodeswithout_sibilings(root.left)
    elif root.right != None:
        print(root.right.data)
        nodeswithout_sibilings(root.right)


def arrangebst(list1):  # unsolved
    if len(list1) > 0:
        root = Binary_trees(list1[len(list1) // 2])
        if len(list1[:len(list1) // 2]) > 0:
            root.left = arrangebst(list1[:len(list1) // 2])
        if len(list1[len(list1) // 2 + 1:]) > 0:
            root.right = arrangebst(list1[len(list1) // 2 + 1:])


def checkbst(root):
    if root == None:
        return True
    l = [root]
    while len(l) > 0:
        pop1 = l.pop(0)
        if pop1.left != None:
            l.append(pop1.left)
        if pop1.right != None:
            l.append(pop1.right)


def lowest_common_ancestor(root, a, b):
    if root == None:
        return
    if root.data == a or root.data == b:
        return root
    left1 = lowest_common_ancestor(root.left, a, b)
    right1 = lowest_common_ancestor(root.right, a, b)
    if left1 and right1:
        return root.data
    else:
        return left1.data if left1 is not None else right1


def mirror(root):
    if root == None:
        return
    else:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)
        return root


def check_bst(root):
    if root == None:
        return True
    if root.left and root.right:
        if root.left.data >= root.data and root.data >= root.right.data:
            return False
    check_bst(root.left)
    check_bst(root.right)


def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        if not valid(node.left, left, node.val):
            return False
        if not valid(node.right, node.val, right):
            return False
        return True

    return valid(root, float('-inf'), float('inf'))


def leftView(root):  # iterative way
    output = []
    if root is None:
        return
    list1 = []
    list1.append(root)
    while len(list1):
        length = len(list1)
        for i in range(1, length + 1):
            q = list1[0]
            list1.pop(0)
            if i == 1:
                output.append(q.data)
            if q.left is not None:
                list1.append(q.left)
            if q.right is not None:
                list1.append(q.right)
    return output


def rightView(root):  # iterative way
    output = []
    if root is None:
        return
    list1 = []
    list1.append(root)
    while len(list1):
        length = len(list1)
        for i in range(1, length + 1):
            q = list1[0]
            list1.pop(0)
            if i == 1:
                output.append(q.data)
            if q.right is not None:
                list1.append(q.right)
            if q.left is not None:
                list1.append(q.left)
    return output


def printLevelWise(root):
    if root == None:
        return
    list1 = [root]
    while len(list1):
        length = len(list1)
        output = []
        for i in range(1, length + 1):
            q = list1[0]
            list1.pop(0)
            output.append(q.data)
            if q.left != None:
                list1.append(q.left)
            if q.right != None:
                list1.append(q.right)
        print(output)


def isysmmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 and root2:
        if root1.data == root2.data:
            return isysmmetric(root1.left, root2.right) and isysmmetric(root1.right, root2.left)
    return False


def issymmteric1(root1, root2):  # iterative way
    if root1 is None and root2 is None:
        return True
    list1 = [root1, root2]
    while list1:
        left_node = list1.pop(0)
        right_node = list1.pop(0)
        if left_node.data != right_node.data:
            return False
        if left_node.right and right_node.left:
            list1.append(left_node.right)
            list1.append(right_node.left)
        if left_node.right or right_node.left:
            return False
        if left_node.left and right_node.right:
            list1.append(left_node.left)
            list1.append(right_node.right)
        if left_node.left or right_node.right:
            return False
    return True


def heightOfBinaryTree(root):
    if root is None:
        return 0
    leftside = 1 + heightoftree(root.left)
    rightside = 1 + heightoftree(root.right)
    if leftside > rightside:
        return leftside
    else:
        return rightside


def helperfunction(root, level, maxlevel):
    if root is None:
        return
    if maxlevel[0] < level:
        print(root.data, end=' ')
        maxlevel[0] = level

    helperfunction(root.right, level + 1, maxlevel)
    helperfunction(root.left, level + 1, maxlevel)


def leftviewOfBinaryTree(root):
    maxlevel = [0]
    helperfunction(root, 1, maxlevel)


root = Binary_trees(0)
root.left = Binary_trees(2)
root.right = Binary_trees(6)
root.right.left = Binary_trees(5)
root.right.right = Binary_trees(7)
root.left.left = Binary_trees(1)
root.left.right = Binary_trees(5)
root = mirror(root)
# print(lowest_common_ancestor(root,1,5))
root1 = Binary_trees(5)
root1.left = Binary_trees(2)
root1.left.left = Binary_trees(1)
root1.right = Binary_trees(9)
root1.right.left = Binary_trees(6)
root1.right.right = Binary_trees(10)
root1 = mirror(root)
# print(identical(root,root1))
# print(leftView(root))
# print(rightView(root))
# # print(printLevelWise(root))
# print(topView(root))
# print(bottomView(root))
node = Binary_trees(1)
node.right = Binary_trees(2)
node.left = Binary_trees(2)
node.left.left = Binary_trees(3)
node.left.right = Binary_trees(4)
node.right.left = Binary_trees(4)
node.right.right = Binary_trees(3)


# print(issymmteric1(node,node))
# print(heightOfBinaryTree(root))
# leftviewOfBinaryTree(root)

def get_total_cost(items, selected):
    # Lets create a variable named no_of_key_errors and no_of_value_errors assign zero for both the variables.
    no_of_key_errors = 0
    no_of_value_errors = 0
    # lets create the variable amount to count the total cost for the products.
    amount = 0
    # iterate over the selected items list to count the amount.
    for i in selected:
        # this try except is used to find the no of KeyErrors.
        try:
            value = items[i]
            # this try except is used to find the no of ValueErrors and to add the value  to the amount.
            try:
                amount += value
            except TypeError as te:
                no_of_value_errors += 1
        except KeyError as ke:
            no_of_key_errors += 1
    # returning the total cost (amount) and no of key errors and no of value errors.
    return (amount, no_of_key_errors, no_of_value_errors)


items = {'apple': 12, 'banana': 7, 'cherry': 10, 'dragonfruit': 35}
selected = ['apple', 'apple', 'cherry', 'eggplant', 'cherry']
cost = get_total_cost(items, selected)
print(cost)




def diagonalPrintUtil(root, d, diagonalPrintMap):
    # Base Case
    if root is None:
        return

    # Store all nodes of same line
    # together as a vector
    try:
        diagonalPrintMap[d].append(root.data)
    except KeyError:
        diagonalPrintMap[d] = [root.data]

    # Increase the vertical distance
    # if left child
    diagonalPrintUtil(root.left,
                      d + 1, diagonalPrintMap)

    # Vertical distance remains
    # same for right child
    diagonalPrintUtil(root.right,
                      d, diagonalPrintMap)


# Print diagonal traversal of given binary tree
def diagonalPrint(root):
    # Create a dict to store diagonal elements
    diagonalPrintMap = dict()

    # Find the diagonal traversal
    diagonalPrintUtil(root, 0, diagonalPrintMap)

    print("Diagonal Traversal of binary tree : ")
    for i in diagonalPrintMap:
        for j in diagonalPrintMap[i]:
            print(j, end=" ")
        print()


# Driver Program
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonalPrint(root)



def diameterOfBinaryTree(root):
    # Define a recursive function to calculate the diameter
    def diameter(node, res):
        # Base case: if the node is None, return 0
        if not node:
            return 0
        
        # Recursively calculate the diameter of left and right subtrees
        left = diameter(node.left, res)
        right = diameter(node.right, res)

        # Update the maximum diameter encountered so far
        res[0] = max(res[0], left + right)
        
        # Return the depth of the current node
        return max(left, right) + 1
    
    # Initialize a list to hold the maximum diameter encountered
    res = [0]
    # Call the diameter function starting from the root
    diameter(root, res)
    # Return the maximum diameter encountered
    return res[0]




















