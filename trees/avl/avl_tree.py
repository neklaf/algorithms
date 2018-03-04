#!/usr/bin/python
# -*- coding: ascii -*-

import sys

# https://docs.python.org/2/library/sys.html
sys.setrecursionlimit(4000)

def enum(**enums):
    return type('Enum', (), enums)

Balances = enum(left_heavy=0, balanced=1, right_heavy=2)

log = False

class Rebalancing:
    __status = None

    def __init__(self, status):
        self.__status = status

    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status

class AVLNode:
    """This class represents a node as a subtree"""
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

    def is_empty(self):
        if log:
            print "AVLNode::is_empty(self) ini"
        return self == None or self.key == None or self.key == ""

    '''Draw AVLNode fields'''
    def draw(self, margin):
        if log:
            print "AVLNode::draw(self, margin) ini"
        if self != None:
            print margin + "key: ", self.key
            print margin + "value: ", self.value
            print margin + "balance: ", self.balance
            if self.left != None:
                self.left.draw(margin + " (L)")
            if self.right != None:
                self.right.draw(margin + " (R)")

    def remove(self, key, rebalance):
        if log:
            print "AVLNode::remove(self, key, rebalance) ini"
        if self != None:
            if key < self.key:
                self.left.remove(key, rebalance)
            if rebalance:
                self.left_balance(rebalance)
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

    def search(self, key, success, value):
        if log:    
            print "AVLNode::search(self) ini"
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

    def left_balance(self, rebalance):
        if log:
            print "AVLNode::left_balance(self, rebalance) ini"
        if self.balance == Balances.left_heavy:
            self.balance = Balances.balanced
        elif self.balance == Balances.balanced:
            self.balance = Balances.right_heavy
            rebalance = False
        elif self.balance == Balances.right_heavy:
            right_subtree = self.right
            balance_subtree = right_subtree.balance
            if balance_subtree != left_heavy:
                self.right = right_subtree.left
                rigth_subtree.left = self
                if right_subtree == Balances.balanced:
                    self.balance = Balances.right_heavy
                    right_subtree.balance = Balances.left_heavy
                    rebalance = False
                else:
                    self.balance = balanced
                    rigth_subtree.balance = Balances.balanced
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

    def __modify(self, key, value, rebalance):
        if log:
            print "AVLTree::__modify(key, value, rebalance) ini"
        if self.is_empty():
            print "\tInsert node in tree and rebalance = True"
            self.__root = AVLNode()
            self.__root.key = key
            self.__root.value = value
            rebalance.setStatus(True)
        elif key < self.__root.key:
            print "\tkey " + key + "< self.__root.key " + self.__root.key
            if self.__root.left == None:
                self.__root.left = AVLNode()
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
            print "\tkey ", key, " > self.__root.key ", self.__root.key
            if self.__root.right == None:
                self.__root.right = AVLNode()
            right_subtree = AVLTree(node = self.__root.right)
            right_subtree.__modify(key, value, rebalance)
            if rebalance.getStatus():
                print "self.__root.key < key -> rebalance"
                if self.__root.balance == Balances.left_heavy:
                    print "self.__root.key < key -> Balances.left_heavy"
                    self.__root.balance = Balances.balanced
                    rebalance.setStatus(False)
                elif self.__root.balance == Balances.balanced:
                    print "self.__root.key < key -> Balances.balanced"
                    self.__root.balance = Balances.right_heavy
                elif self.__root.balance == Balances.right_heavy:
                    print "self.__root.key < key -> Balances.right_heavy"
                    if self.__root.right.balance == Balances.right_heavy:
                        print "right_rotation()"
                        self.right_rotation()
                    else:
                        print "right_left_rotation()"
                        self.right_left_rotation()
                    rebalance.setStatus(False)
        else:
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
    
    def search(self, key, success, value):
        if log:
            print "AVLTree::delete(self, key, success, value) ini"
        if self == None:
            success = False
        else:
            self.__root.search(key, success, value)

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
        return self.__root.height()

    def draw_tree(self):
        if log:
            print "AVLTree::draw_tree(self) ini"
        if self.is_empty():
            print None
        #else:
        #    self.__root.draw('\t')

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