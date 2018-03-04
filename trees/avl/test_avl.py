#!/usr/bin/python
# -*- coding: utf-8 -*-

# How to debug Python code!
#
#Python: http://docs.python.org/2/library/pdb.html :

# python -m pdb debugfile.py

#Once in:
#b (line #) – sets breakpoint
#s – step into
#n – next
#c – continue
#r – run til return

from avl_tree import AVLTree, AVLNode

import sys, time, random

sys.setrecursionlimit(4000)

def main():
    print "-:=Test AVL trees=:-"
    if(len(sys.argv) != 6):
        print "Use: ./test_avl.py <words_file_name> <meanings_file_name> <number_of_insertions> <number_of_search> <number of delete>"
        sys.exit(0)
    else:
        words_file_name = sys.argv[1]
        meanings_file_name = sys.argv[2]
        print "Words file: " + words_file_name + "\nMeanings file: " + meanings_file_name
        inserts = int(sys.argv[3])
        searchs = int(sys.argv[4])
        deletes = int(sys.argv[5])
        
        sys.stdout.write("Inserts: %s" % inserts)
        print ""
        sys.stdout.write("Searchs: %s" % searchs)
        print ""
        sys.stdout.write("Deletes: %s" % deletes)
        print ""

        f = open(words_file_name, "r")
        f2 = open(meanings_file_name, "r")

        """ INSERTS PART """
        avl = AVLTree(node = AVLNode())
        print "Is an empty tree: ", avl.is_empty()
        print "Draw a tree: ", avl.draw_tree()
        print "Tree height: ", avl.height()
        t0_1 = time.time()
        t0 = time.strftime('%s')
        words = []
        for i in range(0, inserts):
            word = f.readline()
            print "word read: " , word.strip()
            definition = f2.readline()
            print "meaning read: ", definition.strip()
            if not word: break
            if not definition: break
            words.append(word.strip())
            print "words: ", words
            avl.modify(word.strip(), definition.strip())

        t1 = time.strftime('%s')
        print "words: ", words
        if inserts > 0:
            t1_1 = time.time()
            t_insert = t1_1 - t0_1
            print "Insertion process ends successfully! -> time ", t_insert
            print ""
        
        """ SEARCH PART """
        if searchs > 0:
            t0 = time.time()
            for s in range(0, searchs):
                word = words[random.randint(0, len(words))]
                avl.search(word, success, value)
            t1 = time.time()
            t_search = t1 - t0
            print "Search operations done! -> time ", t_search
            print ""

        """ DELETE PART """
        if deletes > 0:
            t0 = time.time()
            for s in range(0, deletes):
                word = words[random.randint(0, len(words))]
                avl.delete(word)
            t1 = time.time()
            t_delete = t1 - t0
            print "Delete operations done! -> time ", t_delete
            print ""

        # Closing file descriptors
        f.close()
        f2.close()
        print "Resultant tree:"
        avl.draw_tree()

main()