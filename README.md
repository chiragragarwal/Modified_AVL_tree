Author	:	Chirag R. Agarwal
Email	:	chirag.agarwalr@gmail.com
Problem	:	Implemeting a modified AVL tree in python
Site	:	http://agarwalchirag.wordpress.com

Idea :- To implement insert and delete operations for a modified AVL tree.

Statement :- You will be given 2 sequences of numbers. You have to insert the first sequence into a BST such that for every node, the difference between the left and right height is atmost 2. You have to use the second sequence to delete nodes from the BST. After each operation you must print the preorder traversal of the BST.

Input format :-
NI <Number of nodes to be inserted>
NI integers
ND <Number of nodes to be deleted>
ND integers

Sample Input :-
10
10 20 30 40 25 23 22 50 60 70
5
25 23 10 20 22

Sample Output :-
10
10 20
10 20 30
20 10 30 40
20 10 30 25 40
20 10 30 25 23 40
25 20 10 23 22 30 40
25 20 10 23 22 30 40 50
25 20 10 23 22 40 30 50 60
25 20 10 23 22 40 30 50 60 70
30 20 10 23 22 50 40 60 70
30 20 10 22 50 40 60 70
30 20 22 50 40 60 70
30 22 50 40 60 70
50 30 40 60 70

--- NOTE :

I print the tree after inserting all the nodes. Next, after every deletion, I print the tree in a formatted manner rather than the pre-order traversal for better understanding. The output is formatted as follows :

All the nodes at the same level in the tree are equidistant from the starting line i.e. same number of tabs from the start.
The root is at the start (0 tabs). The nodes at level 1 are at 1 tab space from the start.

For the above sample input, the inserted tree would be :

25
  20
    10
    23
      22
  40
    30
    50
      60
        70

At the end I print the preorder traversal of the final tree too.
