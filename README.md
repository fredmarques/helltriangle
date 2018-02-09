# Hell Triangle

Python lang had been adopted due it's simplicity. 

Also, for unit testing, the doc module testing was choosen to document and test the code at the same time and eliminate dependecies.

___
## Run
Running this code is straight forward, assuming you have python 3.X installed
```shell
python hell_triangle.py
```

> If nothing is logged on console means that doctest tests the module and everything works.
Look at the tests and the code comments to understand it's logic.

---
## Assumptions:

* The lists inside input arg must have a triangular shape.
* The first element (triangle's top) is not an exception case: 
I could assume it will always be in the path and then appending it in the beginning and eliminate the ternary check for right child index. **That would improve execution time.**

---
## Complexity

The algorithm runs for each row and check the childs from the row above.
Thus for a N sized input array the complexity is `O(N)` or so called *linear*, in which execution 
time increases with a constant ratio.