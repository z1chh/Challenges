class BST(object):
    '''Class that represents a Binary Search Tree.'''
    class Node(object):
        '''A single node within a BST.'''
        def __init__(self, key, val = None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        '''Construct an empty binary search tree.'''
        self.root = None

    def __len__(self):
        '''Compute the size (number of key/value pairs) of the BST.'''
        return BST._size(self.root)

    def __bool__(self):
        '''Convert a BST into a Boolean value. Like most Python collections,
        the logic here is that any non-empty BST evaluates as True.'''
        return self.root != None

    def __repr__(self):
        list = []
        self.traverse(lambda x, y: list.append((x,y)))
        rep = '{'
        rep += "'{}':{}".format(list[0][0], list[0][1])
        list.pop(0)
        for pair in list:
            rep += ",'{}':{}".format(pair[0], pair[1])
        rep += '}'
        return rep
    
    @staticmethod
    def _size(node):
        '''Compute the size of the tree below this node.'''
        if node == None:
            return 0
        else:
            return 1 + BST._size(node.left) + BST._size(node.right)

    def put(self, key, val = None):
        '''Insert the key-value pair into the BST.'''
        def _put(node, key, val):
            '''Helper recursive function for the public put() method.'''
            if node == None:
                return BST.Node(key, val)
            elif key < node.key:
                node.left = _put(node.left, key, val)
            elif key > node.key:
                node.right = _put(node.right, key, val)
            else:
                node.val = val
            return node
        self.root = _put(self.root, key, val)

    @staticmethod
    def _get(node, key):
        '''Helper function for get() and contains(). This is not local
        so that it can be shared between the two public methods.

        Alternatively, this could be a method of the Node class.
        '''
        if node == None:
            return None
        elif key < node.key:
            return BST._get(node.left, key)
        elif key > node.key:
            return BST._get(node.right, key)
        else:
            return node

    def get(self, key):
        '''Get the value associated with the given 'key'.'''
        x = BST._get(self.root, key)
        if x == None:
            raise KeyError(key)
        else:
            return x.val

    def minKey(self):
        current = self.root
        while current.left:
            current = current.left
        return current.key

    def maxKey(self):
        current = self.root
        while current.right:
            current = current.right
        return current.key

    def traverse(self, func):
        def inorder(x, func):
            if x == None:
                return
            inorder(x.left, func)
            func(x.key, x.val)
            inorder(x.right, func)
        node = self.root
        inorder(node, func)


    def __contains__(self, key):
        '''Implements the 'in' operator.'''
        return BST._get(self.root, key) != None

    def depth(self):
        '''Return the maximum depth of the tree.'''
        def _depth(node):
            '''Compute the depth of the tree below this node.'''
            if node == None:
                return 0
            else:
                return 1 + max(_depth(node.left), _depth(node.right))
        return _depth(self.root)

"""
Java
    * TreeMap<KEY, VALUE>
* put(KEY, VALUE)
* containsKey
* containsValue
* get(KEY)
* firstKey
* lastKey
* remove(key)
* 
* clear()
* clone()
"""
