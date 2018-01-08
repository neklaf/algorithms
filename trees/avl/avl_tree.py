#!/usr/bin/python
# -*- coding: ascii -*-

import sys

sys.setrecursionlimit(4000)

left_heavy = 0
balanced = 1
right_heavy = 2

class Rebalancing:
    def __init__(self, status):
        self.__status = status

    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status

class AVLNode:
    """This class represents as much as a node as a subtree"""
    #key = ""
    #value = ""
    #left = None
    #right = None
    #balance = balanced
    
    def __init__(self):
        global balancing_factor, balanced
        print "entering __init__(key, value, balance) AVLNode method"
        self.key = ""
        self.value = ""
        self.left = None
        self.right = None
        self.balance = balanced

    def is_empty(self):
        return self == None or self.key == None or self.key == ""

    def draw(self, margin):
        if self != None:
            """print "key: " + margin , self.key"""
            print margin , self.key
            """print "value: " + margin , self.value"""
            if self.left != None:
                self.left.draw(margin + "  ")
                
            if self.right != None:
                self.right.draw(margin + "  ")

    def remove(self, key, rebalance):
        print "entering remove AVL method"
        if self != None:
            if key < self.key:
                self.left.remove(key, rebalance)
            if rebalance:
                left_rebalance(self, rebalance)
            elif self.key < key:
                self.right.remove(key, rebalance)
            else:
                if self.left == None:
                    aux = self
                    self = self.right
                    aux = None
                    rebalance = True
                elif self.right == None:
                    aux = self
                    self = self.left
                    aux = None
                    rebalance = True
                else:
                    self.left.delete_maximum_key(self.key, self.value, rebalance)
                    if rebalance:
                        self.left_balance(rebalance)
    
    def delete_maximum_key(self, key, value, rebalance):
        print "entering delete maximum key AVLNode method"
        """ Be careful with my implementation of the dispose method : obj = None"""
        if self.right == None:
            key = self.key
            value = self.value
            aux = self
            self = self.left
            aux = None
            rebalance = True
        else:
            self.right.delete_maximum_key(key, value, rebalance)
            if rebalance:
                self.right_balance(rebalance)

    def search(self, key, success, value):
        print "entering search AVLNode method"
        if self == None:
            success = False
        else:
            if self.key == key:
                success = True
                value = self.value
            elif key < self.key:
                self.left.search(key, success, value)
            else:
                self.right.search(key, success, value)
    
    def test_balancing_factors(self):
        global balancing_factor, left_balance, balanced, right_balance
        print "entering test_balancing_factors AVLNode method"
        if self == None:
            return True
        elif self.left == None and self.right == None:
            return self.balance == balanced
        elif self.left == None and self.right != None:
            return self.balance == (right_heavy and self.right.test_balancing_factors())
        else:
            hi = self.left.height()
            hr = self.right.height()
            if hi == hr:
                ok = self.balance == balanced
            elif hi > hr:
                ok = self.balance == left_heavy
            else:
                ok = self.balance == right_heavy

    def balancing(self):
        print "entering balancing AVLNode method"
        if self == None:
            return True
        elif self.left == None and self.right == None:
            return true
        elif self.left == None and self.right != None:
            return self.right.height() == 0
        elif self.left != None and self.right == None:
            return self.left.height() == 0
        else:
            hi = self.left.height()
            hr = self.right.height()
            return abs(hi - hr) <= 1 and self.left.balancing() and self.right.balancing()
    
    def height(self):
        print "entering height AVLNode method"
        def max(left, right):
            if left >= right:
                return left
            else:
                return right
        if self.left == None and self.right != None:
            return 1 + self.right.height()
        elif self.left != None and self.right == None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def left_balance(self, rebalance):
        global balancing_factor, left_balance, balanced, right_balance
        print "entering left_balance AVLNode method"
        if self.balance == left_heavy:
            self.balance = balanced
        elif self.balance == balanced:
            self.balance = right_heavy
            rebalance = False
        elif self.balance == right_heavy:
            right_subtree = self.right
            balance_subtree = right_subtree.balance
            if balance_subtree != left_heavy:
                self.right = right_subtree.left
                rigth_subtree.left = self
                if right_subtree == balanced:
                    self.balance = right_heavy
                    right_subtree.balance = left_heavy
                    rebalance = False
                else:
                    self.balance = balanced
                    rigth_subtree.balance = balanced
                self = right_subtree
            else:
                left_subtree = right_subtree.left
                balance_subtree = left_subtree.balance
                right_subtree.left = left_subtree.right
                left_subtree.right = right_subtree
                self.right = left_subtree.left
                left_subtree.left = self
                if balance_subtree == right_heavy:
                    self.balance = left_heavy
                    right_subtree.balance = balanced
                elif balance_subtree == balanced:
                    self.balance = balanced
                    right_subtree.balance = balanced
                else:
                    self.balance = balanced
                    right_subtree.balance = right_heavy
                self = self.left
                left_subtree.balance = balanced
    
    def right_balance(self, rebalance):
        global balancing_factor, left_balance, balanced, right_balance
        print "entering right_balance AVLNode method"
        if self.balance == right_heavy:
            self.balance = balanced
        elif self.balance == balanced:
            self.balance = left_heavy
            rebalance = False
        elif self.balance == left_heavy:
            left_subtree = self.left
            balance_subtree = left_subtree.balance
            if balance_subtree != right_heavy:
                self.left = left_subtree.right
                left_subtree.right = selft
                if balance_subtree == balanced:
                    self.balance = right_heavy
                    left_subtree.balance = right_heavy
                    rebalance = False
                else:
                    self.balance = balanced
                    left_subtree.balance = balanced    
                self = left_subtree
            else:
                right_subtree = left_subtree.right
                balance_subtree = right_subtree.balance
                left_subtree.right = right_subtree.left
                right_subtree.left = left_subtree
                self.left = right_subtree.right
                right_subtree.right = self
                if balance_subtree == left_heavy:
                    self.balance = right_heavy
                    left_subtree.balance = balanced
                elif balance_subtree == balanced:
                    self.balance = balanced
                    left_subtree.balance = balanced
                else:
                    self.balance = balanced
                    left_subtree.balance = left_heavy
                self = right_subtree
                right_subtree.balance = balanced


class AVLTree:
    """ 
    AVL Trees: 
    http://en.wikipedia.org/wiki/AVL_tree
    http://xlinux.nist.gov/dads//HTML/avltree.html
    
    This Dictorionary ADT implementation is based on Javier Campos's Ada95 AVL implementation:
    http://webdiis.unizar.es/asignaturas/EDA/gnat/ejemplos_TADs/arboles_AVL/campos/
    
    There are many examples of a Python AVL tree implementation
    out there using Object Oriented Programming techniques, for instance:
    http://www.brpreiss.com/books/opus7/
    
    And in other programming language:
    (C++) http://cis.stvincent.edu/html/tutorials/swd/avltrees/avltrees.html
    """    
    def __init__(self, **dargs):
        """Order to option parameters: node, key, value"""
        global balanced
        #dargs -- dictionary of named arguments
        print "AVLTree::__init__(root)"
        self.__root = AVLNode()
        #self.__root = None
        for key in dargs:
            if key == "node":
                self.__root = dargs['node']
            elif key == "key":
                if self.__root is None:
                    self.__root = AVLNode()
                self.__root.key = dargs[key]
            elif key == "value":
                if self.__root is None:
                    self.__root = AVLNode()
                self.__root.value = dargs[value]

    def empty(self):        
        print "AVLTree::empty()"
        self.__root = None
        self = None

    def __modify(self, key, value, rebalance):
        global balancing_factor, left_balance, balanced, right_balance
        print "AVLTree::__modify(key, value, rebalance)"
        if self.is_empty():
            print "\tinsert node in tree and rebalance = True"
            self.__root = AVLNode()
            self.__root.key = key
            self.__root.value = value
            rebalance.setStatus(True)
        elif key < self.__root.key:
            print "\tkey " + key + "< self.__root.key " + self.__root.key
            if self.__root.left == None:
                self.__root.left = AVLNode()
            left_subtree = AVLTree(node = self.__root.left)
            #self.__root.left.__modify(key, value, rebalance)
            left_subtree.__modify(key, value, rebalance)
            if rebalance.getStatus(): 
                print "key < self.__root.key -> rebalance"
                if self.__root.balance == left_heavy:
                    print "key < self.__root.key -> left_heavy"
                    if self.__root.left.balance == left_heavy:
                        print "left_rotation()"
                        self.left_rotation()
                    else:
                        print "left_right_rotation()"
                        self.left_right_rotation()
                    #rebalance.setStatus(False)
                    rebalance.status = False
                elif self.__root.balance == balanced:
                    print "key < self.__root.key -> balanced"
                    self.__root.balance = right_heavy
                elif self.__root.balance == right_heavy:
                    print "key < self.__root.key -> right_heavy"
                    self.__root.balance = balanced
                    #rebalance.setStatus(False)
                    rebalance.status = False
        elif self.__root.key < key:
            print "self.__root.key ", self.__root.key , " < key " , key
            if self.__root.right == None:
                self.__root.right = AVLNode()
            right_subtree = AVLTree(node = self.__root.right)
            #self.__root.right.__modify(key, value, rebalance)
            right_subtree.__modify(key, value, rebalance)
            if rebalance.getStatus():
                print "self.__root.key < key -> rebalance"
                if self.__root.balance == left_heavy:
                    print "self.__root.key < key -> left_heavy"
                    self.__root.balance = balanced
                    #rebalance.setStatus(False)
                    rebalance.status = False
                elif self.__root.balance == balanced:
                    print "self.__root.key < key -> balanced"
                    self.__root.balance = right_heavy
                elif self.__root.balance == right_heavy:
                    print "self.__root.key < key -> right_heavy"
                    if self.__root.right.balance == right_heavy:
                        print "right_rotation()"
                        self.right_rotation()
                    else:
                        print "right_left_rotation()"
                        subtree.right_left_rotation()
                    #rebalance.setStatus(False)
                    rebalance.status = False
        else:
            self.__root.value = value

    def modify(self, key, value):
        print "AVLTree::modify(key, value, rebalance)"
        rebalance = Rebalancing(False)
        self.__modify(key, value, rebalance)
    

    def is_empty(self):
        print "AVLTree::is_empty()"
        return self is None or self._root is None

    def left_rotation(self):
        global balancing_factor, balanced
        print "AVLTree::left_rotation"
        aux = self.__root.left
        self.__root.right = aux.left
        self.__root.balance = balanced
        self.__root = aux
        self.__root.balance = balanced
        self.__root.left, self.__root.right = self.__root.right, self.__root.left

    def right_rotation(self):
        global balancing_factor, balanced
        print "AVLTree::right_rotation"
        aux = self.__root.right
        self.__root.right = aux.left
        self.__root.balance = balanced
        aux.left = self.__root
        self.__root = aux
        self.__root.balance = balanced

    def left_right_rotation(self):
        global balancing_factor, left_balance, balanced, right_balance
        print "AVLTree::left_right_rotation"
        aux1 = self.__root.left
        aux2 = self.__root.left.right
        aux1.right = aux2.left
        aux2.left = aux1
        if aux2.balance == left_heavy:
            aux1.balance = balanced
        elif aux2.balance == balanced:
            aux1.balance = balanced
            self.__root.balance = balanced
        else:
            aux1.balance = left_heavy
            self.__root.balance = balanced
        self.__root.left = aux2.right
        aux2.right = self.__root
        aux2.balance = balanced
        self.__root = aux2

    def right_left_rotation(self):
        global balancing_factor, left_balance, balanced, right_balance
        print "AVLTree::right_left_rotation"
        root = self.__root
        aux1 = self.__root.right
        aux2 = self.__root.right.left
        aux1.left = aux2.right
        self.__root.right = aux2
        if aux2.balance == right_heavy:
            aux1.balance = balanced
        elif aux2.balance == balanced:
            aux1.balance = balanced
            self.__root.balance = balanced
        else:
            aux1.balance = left_heavy
            self.__root.balance = balanced
        self.__root.right = aux2.left
        aux2.left = self.__root
        aux2.balance = balanced
        self.__root = aux2

    def delete(self, key):
        print "entering delete AVLTree method"
        rebalance = False
        self.__root.remove(key, rebalance)
    
    def search(self, key, success, value):
        print "entering search AVLTree method"
        if self == None:
            success = False
        else:
            self.__root.search(key, success, value)

    def is_empty(self):
        print "entering is_empty AVLTree method"
        return self == None or self.__root == None

    def dump_in_order(self):
        print "entering dump_in_order AVLTree method"
        if self != None and self.__root != None:
            self.__root.left.dump_in_order()
            print self.__root.key, ":", self.__root.value
            print "\n"
            self._root.right.dump_in_order()

    def height(self):
        print "entering height AVLTree method"
        return self.__root.height()

    def draw_tree(self):
        print "entering draw_tree AVL method"
        self.__root.draw("")

    def balancing(self):
        print "entering balancing AVLTree method"
        if self != None and self.__root != None:
            self.__root.balancing()

    def test_balancing_factors(self):
        print "entering test_balancing_factors AVLTree method"
        if self == None:
            return True
        else:
            return self.__root.test_balancing_factors()



""" 
Commented AVLNode methods??   
    def __init__(self, root):
        global balancing_factor
        print "entering __init__(root) AVLTree method"
        if root == None:
            __root = AVLNode("","")
        else:
            __root = root
        __balance = balanced

    def __init__(self, root, balance):
        global balancing_factor
        print "entering __init__(root, balance) AVLTree method"
        if root == None:
            __root = AVLNode("","")
        else:
            __root = root
        if balance == None:
            __balance = balanced
        else:
            __balance = balance
""" 
"""
    def __init__(self, key, value, balance):
        global balancing_factor
        print "entering __init__(key, value, balance) AVLNode method"
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.balance = balance
"""
"""
def __init__(self, key, value, balance):
        global balancing_factor, balanced
        print "entering __init__(key, value, balance) AVLNode method"
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.balance = balance
"""
"""
    def modify(self, key, value, rebalance):
        global balancing_factor, left_balance, balanced, right_balance
        print "entering modify(key, value, rebalance) AVLNode method"
        print "\tself.key: ", self.key, " key: ", key, " value: ",value, " rebalance: ", rebalance
        if self.is_empty():
            print "\tinsert node in tree and rebalance = True"
            self.key = key
            self.value = value
            rebalance.setStatus(True)
        elif key < self.key:
            print "\tkey " + key + "< self.key " + self.key
            if self.left == None:
                self.left = AVLNode()
            self.left.modify(key, value, rebalance)
            if rebalance.getStatus(): 
                print "key < self.key -> rebalance"
                if self.balance == left_heavy:
                    print "key < self.key -> left_heavy"
                    subtree = AVLTree(node = self)
                    if self.left.balance == left_heavy:
                        #self.left_rotation()
                        subtree.left_rotation()
                    else:
                        #self.left_right_rotation()
                        subtree.left_right_rotation()
                    rebalance.setStatus(False)
                elif self.balance == balanced:
                    print "key < self.key -> balanced"
                    self.balance = right_heavy
                elif self.balance == right_heavy:
                    print "key < self.key -> right_heavy"
                    self.balance = balanced
                    rebalance.setStatus(False)
        elif self.key < key:
            print "self.key ", self.key , " < key " , key
            if self.right == None:
                self.right = AVLNode()
            self.right.modify(key, value, rebalance)
            if rebalance.getStatus():
                print "self.key < key -> rebalance"
                if self.balance == left_heavy:
                    print "self.key < key -> left_heavy"
                    self.balance = balanced
                    rebalance.setStatus(False)
                elif self.balance == balanced:
                    print "self.key < key -> balanced"
                    self.balance = right_heavy
                elif self.balance == right_heavy:
                    print "self.key < key -> right_heavy"
                    subtree = AVLTree(node = self)
                    if self.right.balance == right_heavy:
                        print "invoking right_rotation()"
                        #self.right_rotation()
                        subtree.right_rotation()
                        subtree.draw_tree()
                    else:
                        print "invoking right_left_rotation()"
                        #self.right_left_rotation()
                        subtree.right_left_rotation()
                    rebalance.setStatus(False)
        else:
            self.value = value
"""