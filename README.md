# algorithms
Algorithms hodgepodge repository

## Common
### FizzBuzz algorithm:

```
$ python3 fizzbuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
...
```

### Fibonacci
```
$ python3 fibonacci.py
0
1
1
2
3
5
8
13
21
34
```

### Object Oriented Programming
```
$ python3 oop.py 
My name is Aitor
My name is James Bond
...And I am 007
```

## Sorting
### Insertion Sort
```
$ javac InsertionSortAlgorithm.java
$ java InsertionSortAlgorithm 
Length: 6
vector: {22, 18, 7, 23, 2, 15}
Sorted vector: {2, 7, 15, 18, 22, 23}
``` 

## Trees
### AVL
AVL (Adelson-Velsky and Landis) Tree: A balanced binary search tree where the height of the two subtrees (children) of a node differs by at most one.
Look-up, insertion, and deletion are O(log n), where n is the number of nodes in the tree.
(Definition from [http://xlinux.nist.gov/dads//HTML/avltree.html](http://xlinux.nist.gov/dads//HTML/avltree.html) )

In big O notation terms: ([http://en.wikipedia.org/wiki/AVL_tree](http://en.wikipedia.org/wiki/AVL_tree) )

<table>
<tr>
<td>Operation</td>       <td>Average</td>        <td>Worst Case</td>
</tr>
<tr>
<td>Space</td>       <td>O(n)</td>        <td>O(n)</td>
</tr>
<tr>
<td>Search</td>       <td>O(log n)</td>        <td>O(log n)</td>
</tr>
<tr>
<td>Insert</td>       <td>O(log n)</td>        <td>O(log n)</td>
</tr>
<tr>
<td>Delete</td>       <td>O(log n)</td>        <td>O(log n)</td>
</tr>
</table>

```
$ cd trees/avl

$ ./test_avl.py words.txt meanings.txt 2 2 1
-:=Test AVL trees=:-
Words file: words.txt
Meanings file: meanings.txt
Inserts: 2	Searchs: 2	Deletes: 1
words:  ['aa']
Insert node in tree and rebalance = True
words:  ['aa', 'aah']
key  aah  > self.__root.key  aa
-------------paiting Root right subtree
----
k:  aah
v:  aah
Balanced
-------------end Root right subtree
Rebalance status:  True
key > self.__root.key => rebalance
key > self.__root.key => Balances.balanced
words:  ['aa', 'aah']
Insertion process ends successfully! -> time  0.000312089920044

...
```
