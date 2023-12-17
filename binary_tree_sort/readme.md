Binary Tree Level Order Traversal

This Python function performs a level-order traversal of a binary tree and returns a list containing the elements of the tree sorted by levels.

Input:
The root node of the binary tree. Each node has a left child (left), a right child (right), and a value (value).

Output:
Returns a list of integers representing the elements of the binary tree sorted by levels.
Example:

Input:
            2
       8         9
     1   3     4   5

Output: [2, 8, 9, 1, 3, 4, 5]

Note:

The function returns an empty list if the root is None.
The order of elements in the output list follows the level-order traversal, where the root comes first, followed by its children from left to right on each level.