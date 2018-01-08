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

import sys, time, random, avl_tree

sys.setrecursionlimit(4000)

def main():
    print "Advanced Data Structures: AVL vs RED BLACK TREE"
    if(len(sys.argv) < 3):
        print "Use: ./test_avl.py <words_file_name> <meanings_file_name> <number_of_insertions> <number_of_search> <number of delete>"
        sys.exit(0)
    else:
        words_file_name = sys.argv[1]
        meanings_file_name = sys.argv[2]
        print "Words file: " + words_file_name + " Meanings file: " + meanings_file_name
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
    """
    f3 = open("results_avlVSredBlack.txt","w")
    f3.write("TEST AVL | Size: \n")
    f3.write("\tInserts: ")
    f3.write(str(inserts) + "\n")
    f3.write("\tSearchs: ")
    f3.write(str(searchs) + "\n")
    f3.write("\tDelete operations: ")
    f3.write(str(deletes) + "\n")
    f3.write("")
    """
    """ INSERTS PART """
    avl = avl_tree.AVLTree()
    avl_tree.__init__()
    t0_1 = time.time()
    t0 = time.strftime('%s')
    words = []
    sys.exit(0)
    for i in range(0, inserts):
        word = f.readline()
        print "word read: " , word.strip()
        definition = f2.readline()
        print "meaning read: ", definition.strip()
        if not word: break
        if not definition: break
        words.append(word.strip())
        avl.modify(word.strip(), definition.strip())
    t1 = time.strftime('%s')
    t1_1 = time.time()
    print "words: ", words
    t_insert = int(t1) - int(t0)
    t_insert_1 = t1_1 - t0_1
    print "Insertion process ends successfully! -> time ", t_insert , " time_1 " , t_insert_1
    print ""
    """
    f3.write("Inserts | Time: ")
    f3.write(str(t_insert))
    f3.write("")
    """
    f.close()
    f2.close()
    avl.draw_tree()
    #f3.close()
""" SEARCH PART """
"""    t0 = time.time()
    for s in range(0, searchs):
        word = words[random.randint(0, len(words))]
        avl.search(word, success, value)
    t1 = time.time()
    t_search = t1 - t0
    print "Search operations done! -> time ", t_search
    print ""
    f3.write("Search | Time: ")
    f3.write(str(t_search))
    f3.write("")
"""
""" DELETE PART """
"""
    t0 = time.time()
    for s in range(0, deletes):
        word = words[random.randint(0, len(words))]
        avl.delete(word)
    t1 = time.time()
    t_delete = t1 - t0
    print "Delete operations done! -> time ", t_delete
    print ""
    f3.write("Delete | Time: ")
    f3.write(str(t_delete))
    f3.write("")
"""
main()