#!/usr/bin/python
# -*- coding: ascii -*-

'''
AVL (Adelson-Velsky and Landis) Tree: A balanced binary search tree where the height of the two subtrees (children) of a node differs by at most one. 
Look-up, insertion, and deletion are O(log n), where n is the number of nodes in the tree. 
(Definition from http://xlinux.nist.gov/dads//HTML/avltree.html)

In big O notation terms: (http://en.wikipedia.org/wiki/AVL_tree)
Algorithm   Average     Worst Case
Space       O(n)        O(n)
Search      O(log n)    O(log n)
Insert      O(log n)    O(log n)
Delete      O(log n)    O(log n)
'''

import sys

# https://docs.python.org/2/library/sys.html
sys.setrecursionlimit(4000)

# Just a way to implement an enumeration
def enum(**enums):
    return type('Enum', (), enums)
Balances = enum(left_heavy=0, balanced=1, right_heavy=2)

log = False
debug = True

class Rebalancing:
    __status = None

    def __init__(self, status):
        self.__status = status

    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status

class AVLNode:
    """Class to represent a AVL tree node"""
    key = ""
    value = ""
    left = None
    right = None
    balance = Balances.balanced
    
    def __init__(self):
        if log: 
            print "AVLNode::__init__(self) ini"
        self.key = ""
        self.value = ""
        self.left = None
        self.right = None
        self.balance = Balances.balanced

    '''def __init__(self, key, value, letf, right, balance):
        print "AVLNode::__init__(self, key, value, letf, right, balance) ini"
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.balance = balance'''

    '''Method to know if a node is empty'''
    def is_empty(self):
        if log:
            print "AVLNode::is_empty(self) ini"
        return self == None or self.key == None or self.key == ""

    '''Draw AVLNode fields'''
    def draw(self, margin):
        if log:
            print "AVLNode::draw(self, margin) ini"
        if self != None:
            print margin + "k: ", self.key
            print margin + "v: ", self.value
            if self.balance == Balances.right_heavy:
                print margin + "Right Balanced"
            elif self.balance == Balances.left_heavy:
                print margin + "Left Balanced"
            else:
                print margin + "Balanced" 

            if self.left != None:
                margin = "\t" + margin
                if '(R)' in margin:
                    margin = margin.replace("(R)","(L)")
                if '(L)' not in margin:
                    margin = margin + "(L)"
                #    self.left.draw("\t" + margin + "--(L) ")
                #else:
                #    self.left.draw("\t" + margin)
                self.left.draw(margin)
            if self.right != None:
                margin = "\t" + margin
                if '(L)' in margin:
                    margin = margin.replace("(L)", "(R)")
                if '(R)' not in margin:
                    margin = margin + "(R)"
                    #self.right.draw("\t" + margin + "--(R) ")
                #else:
                #    self.right.draw("\t" + margin)
                self.right.draw(margin)    

    '''Remove a node from a tree'''
    def remove(self, key, rebalance):
        if log:
            print "AVLNode::remove(self, key, rebalance) ini"
        if self != None:
            if debug:
                print 'self != None'
            if key < self.key:
                if debug:
                    print 'key ' + key + '< self.key ' +  self.key
                self.left.remove(key, rebalance)
            if rebalance:
                if debug:
                    print 'left rebalance'
                self.left_balance(rebalance)
            elif key > self.key:
                if debug:
                    print 'key ' + key + ' > self.key ' + self.key 
                self.right.remove(key, rebalance)
            else:
                if self.left == None:
                    if debug:
                        print 'self.left == None'
                    aux = self
                    self = self.right
                    aux = None
                    rebalance = True
                elif self.right == None:
                    if debug:
                        print 'self.right == None'
                    aux = self
                    self = self.left
                    aux = None
                    rebalance = True
                else:
                    if debug:
                        print 'invoking delete_maximum_key'
                    self.left.delete_maximum_key(self.key, self.value, rebalance)
                    if rebalance:
                        self.left_balance(rebalance)
    
    def delete_maximum_key(self, key, value, rebalance):
        if log:
            print "AVLNode::delete_maximum_key(self, key, value, rebalance) ini"
        """ It has been implemented dispose method : obj = None """
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

    def search(self, key):
        if log:    
            print "AVLNode::search(self, key) ini"
        success = False
        if self == None:
            return False
        else:
            if self.key == key:
                success = True
            elif key < self.key:
                self.left.search(key, success, value)
            else:
                self.right.search(key, success, value)
        return success

    def test_balancing_factors(self):
        if log:
            print "AVLNode::test_balancing_factors(self) ini"
        if self == None:
            return True
        elif self.left == None and self.right == None:
            return self.balance == Balances.balanced
        elif self.left == None and self.right != None:
            return self.balance == (Balances.right_heavy and self.right.test_balancing_factors())
        else:
            hi = self.left.height()
            hr = self.right.height()
            if hi == hr:
                ok = self.balance == Balances.balanced
            elif hi > hr:
                ok = self.balance == Balances.left_heavy
            else:
                ok = self.balance == Balances.right_heavy

    def balancing(self):
        if log:
            print "AVLNode::balancing(self) ini"
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
        if log:
            print "AVLNode::height(self) ini"
        def max(left, right):
            if left >= right:
                return left
            else:
                return right
        if self.left == None and self.right != None:
            return 1 + self.right.height()
        elif self.left != None and self.right == None:
            return 1 + self.left.height()
        elif self.left != None and self.right != None:
            return 1 + max(self.left.height(), self.right.height())
        else:
            return 1

    '''Method to balance a letf balanced tree'''
    def left_balance(self, rebalance):
        if log:
            print "AVLNode::left_balance(self, rebalance) ini"
        if self.balance == Balances.left_heavy:
            if debug:
                print 'self.balance ', self.balance, ' == Balances.left_heavy ', Balances.left_heavy
            self.balance = Balances.balanced
        elif self.balance == Balances.balanced:
            if debug:
                print 'self.balance ', self.balance, ' == Balances.balanced ', Balances.balanced
            self.balance = Balances.right_heavy
            rebalance = False
        elif self.balance == Balances.right_heavy:
            if debug:
                print 'self.balance ', self.balance, ' == Balances.right_heavy ', Balances.right_heavy
            right_subtree = self.right
            balance_subtree = right_subtree.balance
            if balance_subtree != left_heavy:
                if debug:
                    print 'balance_subtree != left_heavy'
                self.right = right_subtree.left
                right_subtree.left = self
                if right_subtree == Balances.balanced:
                    if debug:
                        print 'right_subtree == Balances.balanced'
                    self.balance = Balances.right_heavy
                    right_subtree.balance = Balances.left_heavy
                    rebalance = False
                else:
                    self.balance = balanced
                    right_subtree.balance = Balances.balanced
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
                    right_subtree.balance = Balances.balanced
                elif balance_subtree == Balances.balanced:
                    self.balance = Balances.balanced
                    right_subtree.balance = Balances.balanced
                else:
                    self.balance = Balances.balanced
                    right_subtree.balance = Balances.right_heavy
                self = self.left
                left_subtree.balance = Balances.balanced
    
    '''Method to balance a right balanced tree'''
    def right_balance(self, rebalance):
        if log:
            print "AVLNode::right_balance(self, rebalance) ini"
        if self.balance == Balances.right_heavy:
            self.balance = Balances.balanced
        elif self.balance == Balances.balanced:
            self.balance = Balances.left_heavy
            rebalance = False
        elif self.balance == Balances.left_heavy:
            left_subtree = self.left
            balance_subtree = left_subtree.balance
            if balance_subtree != Balances.right_heavy:
                self.left = left_subtree.right
                left_subtree.right = self
                if balance_subtree == Balances.balanced:
                    self.balance = Balances.right_heavy
                    left_subtree.balance = Balances.right_heavy
                    rebalance = False
                else:
                    self.balance = Balances.balanced
                    left_subtree.balance = Balances.balanced    
                self = left_subtree
            else:
                right_subtree = left_subtree.right
                balance_subtree = right_subtree.balance
                left_subtree.right = right_subtree.left
                right_subtree.left = left_subtree
                self.left = right_subtree.right
                right_subtree.right = self
                if balance_subtree == left_heavy:
                    self.balance = Balances.right_heavy
                    left_subtree.balance = Balances.balanced
                elif balance_subtree == Balances.balanced:
                    self.balance = Balances.balanced
                    left_subtree.balance = Balances.balanced
                else:
                    self.balance = Balances.balanced
                    left_subtree.balance = Balances.left_heavy
                self = right_subtree
                right_subtree.balance = Balances.balanced


class AVLTree:
    """ 
    AVL Tree class

    This Dictorionary ADT implementation is based on Javier Campos's Ada95 AVL implementation (@javifields):
    http://webdiis.unizar.es/asignaturas/EDA/gnat/ejemplos_TADs/arboles_AVL/campos/

    There are many examples of a Python AVL tree implementation
    out there using Object Oriented Programming techniques, for instance:
    http://www.brpreiss.com/books/opus7/
    
    And in other programming language:
    (C++)
    http://cis.stvincent.edu/html/tutorials/swd/avltrees/avltrees.html
    https://www.auto.tuwien.ac.at/~blieb/woop/avl.html
    """
    __root = None

    def __init__(self, **dargs):
        #Order to option parameters: node, key, value
        if log:
            print "AVLTree::__init__(self, **dargs)"
        #dargs -- dictionary of named arguments
        self.__root = AVLNode()
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
        if log:
            print "AVLTree::empty() ini"
        self.__root = None
        self = None

    def get_root(self):
        if log:
            print "AVLTree::get_root() ini"
        return self.__root

    '''
    Internal method to add a node in AVL tree
    '''
    def __modify(self, key, value, rebalance):
        if log:
            print "AVLTree::__modify(key, value, rebalance) ini"
        if self.is_empty():
            if debug:
                print "Insert node in tree and rebalance = True"
            self.__root = AVLNode()
            self.__root.key = key
            self.__root.value = value
            # Rebalance marked as true to the next??
            rebalance.setStatus(True)
        elif key < self.__root.key:
            if debug:
                print "key " + key + "< self.__root.key " + self.__root.key
            if self.__root.left == None:
                self.__root.left = AVLNode()
                self.__root.left.key = key
                self.__root.left.value = value
                rebalance.setStatus(True)

            left_subtree = AVLTree(node = self.__root.left)
            left_subtree.__modify(key, value, rebalance)
            if rebalance.getStatus():
                print "key < self.__root.key -> rebalance"
                if self.__root.balance == Balances.left_heavy:
                    print "key < self.__root.key -> Balances.left_heavy"
                    if self.__root.left.balance == Balances.left_heavy:
                        print "left_rotation()"
                        self.left_rotation()
                    else:
                        print "left_right_rotation()"
                        self.left_right_rotation()
                    rebalance.setStatus(False)
                    #rebalance.__status = False
                elif self.__root.balance == Balances.balanced:
                    print "key < self.__root.key -> Balances.balanced"
                    self.__root.balance = Balances.right_heavy
                elif self.__root.balance == Balances.right_heavy:
                    print "key < self.__root.key -> Balances.right_heavy"
                    self.__root.balance = Balances.balanced
                    rebalance.setStatus(False)
                    #rebalance.__status = False
        elif key > self.__root.key:
            if debug:
                print "key ", key, " > self.__root.key ", self.__root.key
            if self.__root.right == None:
                self.__root.right = AVLNode()
                self.__root.right.key = key
                self.__root.right.value = value
                rebalance.setStatus(True)
            
            right_subtree = AVLTree(node = self.__root.right)
            right_subtree.__modify(key, value, rebalance)
            if debug:
                print "-------------paiting Root right subtree"
                right_subtree.draw_tree()
                print "-------------end Root right subtree"
            if rebalance.getStatus():
                if debug:
                    print "Rebalance status: ", rebalance.getStatus()
                    print "key > self.__root.key => rebalance"
                if self.__root.balance == Balances.left_heavy:
                    if debug:
                        print "key > self.__root.key => Balances.left_heavy"
                    self.__root.balance = Balances.balanced
                    rebalance.setStatus(False)
                elif self.__root.balance == Balances.balanced:
                    if debug:
                        print "key > self.__root.key => Balances.balanced"
                    self.__root.balance = Balances.right_heavy
                elif self.__root.balance == Balances.right_heavy:
                    if debug:
                        print "key > self.__root.key => Balances.right_heavy"
                    if self.__root.right.balance == Balances.right_heavy:
                        if debug:
                            print "Invoking right_rotation()"
                        self.right_rotation()
                    else:
                        if debug:
                            print "right_left_rotation()"
                        self.right_left_rotation()
                    rebalance.setStatus(False)
        else:
            # Unchanged balance
            self.__root.value = value

    def modify(self, key, value):
        if log:
            print "AVLTree::modify(self, key, value) ini"
        rebalance = Rebalancing(False)
        self.__modify(key, value, rebalance)

    def is_empty(self):
        if log:
            print "AVLTree::is_empty(self) ini"
        return self is None and self._root is None and self._root.key == "" and self._root.value == ""

    def left_rotation(self):
        if log:
            print "AVLTree::left_rotation(self) ini"
        aux = self.__root.left
        self.__root.right = aux.left
        self.__root.balance = Balances.balanced
        self.__root = aux
        self.__root.balance = Balances.balanced
        self.__root.left, self.__root.right = self.__root.right, self.__root.left

    def right_rotation(self):
        if log:
            print "AVLTree::right_rotation(self) ini"
        aux = self.__root.right
        self.__root.right = aux.left
        self.__root.balance = Balances.balanced
        aux.left = self.__root
        self.__root = aux
        self.__root.balance = Balances.balanced

    def left_right_rotation(self):
        if log:
            print "AVLTree::left_right_rotation(self) ini"
        aux1 = self.__root.left
        aux2 = self.__root.left.right
        aux1.right = aux2.left
        aux2.left = aux1
        if aux2.balance == Balances.left_heavy:
            aux1.balance = Balances.balanced
        elif aux2.balance == Balances.balanced:
            aux1.balance = Balances.balanced
            self.__root.balance = Balances.balanced
        else:
            aux1.balance = Balances.left_heavy
            self.__root.balance = Balances.balanced
        self.__root.left = aux2.right
        aux2.right = self.__root
        aux2.balance = Balances.balanced
        self.__root = aux2

    def right_left_rotation(self):
        if log:
            print "AVLTree::right_left_rotation(self) ini"
        root = self.__root
        aux1 = self.__root.right
        aux2 = aux1.left
        if aux2 != None:
            aux1.left = aux2.right
        else:
            aux1.left = None
        self.__root.right = aux2
        if aux2.balance == Balances.right_heavy:
            aux1.balance = Balances.balanced
        elif aux2.balance == Balances.balanced:
            aux1.balance = Balances.balanced
            self.__root.balance = Balances.balanced
        else:
            aux1.balance = Balances.left_heavy
            self.__root.balance = Balances.balanced
        self.__root.right = aux2.left
        aux2.left = self.__root
        aux2.balance = Balances.balanced
        self.__root = aux2

    def delete(self, key):
        if log:
            print "AVLTree::delete(self, key) ini"
        rebalance = False
        self.__root.remove(key, rebalance)
    
    '''Method to search a key in tree'''
    def search(self, key):
        if log:
            print "AVLTree::delete(self, key) ini"
        if self == None:
            return False
        else:
            return self.__root.search(key)

    def is_empty(self):
        if log:
            print "AVLTree::is_empty(self) ini"
        return self == None or self.__root == None or self.__root.key == ""

    def dump_in_order(self):
        if log:
            print "AVLTree::dump_in_order(self) ini"
        if self != None and self.__root != None:
            self.__root.left.dump_in_order()
            print self.__root.key, ":", self.__root.value
            print "\n"
            self._root.right.dump_in_order()

    def height(self):
        if log:
            print "AVLTree::height(self) ini"
        if self.is_empty:
            return 0
        return self.__root.height()

    '''
    Method to draw a tree
    '''
    def draw_tree(self, margin=''):
        if log:
            print "AVLTree::draw_tree(self) ini"
        if self.is_empty():
            print '----EMPTY----'
        else:
            print margin + '----'
            self.__root.draw(margin)

    def balancing(self):
        if log:
            print "AVLTree::balancing(self) ini"
        if self != None and self.__root != None:
            self.__root.balancing()

    def test_balancing_factors(self):
        if log:
            print "AVLTree::test_balancing_factors(self) ini"
        if self == None:
            return True
        else:
            return self.__root.test_balancing_factors()