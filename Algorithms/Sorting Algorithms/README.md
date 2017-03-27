# Sorting Algorithms

## Selection Sort
Time Complexity: O(n<sup>2</sup>)      
Space Complexity: O(1)

*Description:*
Selection Sort works by 'selecting' the largest element in the list and moving it to the end of the list--in a list of length n, the index would be n-1.  Next, it iterates through the list and selects the second largest element in the list, and places it at index (n-2). This process is repeated until the list is fully sorted.  

Since the sort can be done in-place, the space complexity of Selection Sort is O(1).  The space complexity is bounded at O(n<sup>2</sup>).  This is because Selection Sort contains an outer loop (starting at the end of the list and iterating backwards) and an inner loop (iterating from the start of the list up to the current position of the outer loop).  

It is worth noting that as selection sort progresses, the range of the inner loop gets smaller and smaller.  This means that the time complexity of selection sort is actually better than O(n<sup>2</sup>), although according to the rules of Big O, we ignore this and still classify the time complexity of this sort as 0(n<sup>2</sup>).            

## Gnome Sort  
Time Complexity: O(n<sup>2</sup>)             
Space Complexity: O(1)

*Description:*  Gnome Sort was originally called "Stupid Sort", and with good reason.  Gnome sort is an iterative sort that accomplishes sorting through a series of swaps for each item.  In this way, it is similar to bubble sort.  The sheer number of swaps this algorithm makes pretty much ensures that the algorithm will have a bounded runtime of 0(n<sup>2</sup>).    

## Heap Sort
Time Complexity:  O(n log(n))              
Space Complexity: O(1)   

*Description:*      

## Insertion Sort
Time Complexity:  O(n<sup>2</sup>)                           
Space Complexity: O(1)                            

*Description:*  Insertion sort is a simple but reliable iterative sorting algorithm.  It works by treating the first item in the array as a sorted sequence (that contains only that single item).  Then, the algorithm iterates through the rest of the array, grabs the next item, and iterates through the sequence until it finds the correct sorted position for that item.  Once the algorithm has iterated all the way through the original list, all items will have been sorted into the sequence, meaning that the list will have been sorted in-place.

## Intro Sort
Time Complexity:                
Space Complexity:

*Description:*              

## Merge Sort
Time Complexity:  O(n log(n))              
Space Complexity: O(n)

*Description:*   Merge sort is a classic "divide-and-conquer" algorithm.  The algorithm starts by dividing the list in half, and then cutting each of those section half, again and again until each list is a single item.  Once the list is divided into a bunch of sublists each containing one item, the "conquer" part begins.  This is where Merge Sort gets its name--the algorithm then combines individual items into lists of two items, putting the smaller item first.  To be specific, the algorithm uses 3 pointers--1 for each sub list (we'll call them _left_ and _right_), and one to keep track of the main list and where the items go within it.  The algorithm compares the data _left_ and _right_ are pointing at, and selects the smaller value to be added to the main list.  The _left_ or _right_ pointer that was pointing at the smaller data is then incremented, moving onto the next item in its list.  This process is repeated until both sub lists have been merged into the main list, and then repeated on the next set of sub lists.  This process repeats until all sub lists have been merged back into 1 main list, but now in sorted order!

## Quick Sort
Time Complexity:  O(n log(n))*              
Space Complexity: O(log(n))

*Description*:  Quick Sort is another classic "divide-and-conquer" algorithm.  The algorithm starts by selecting an index in the array that will act as a "pivot".  This can effectively be randomly chosen, since no position in the array provides a performance advantage in all situations.  Put another way, each pivot position has a weakness depending on the type of data--for instance, choosing the last item in the list as a pivot would give us a O(n**2) run time if the list was already nearly sorted.  

Once the pivot is chosen, the list then sorts all values smaller than the pivot to the left, and all values larger to the pivot to the right.  Now, the recursion comes in--the algorithm then calls itself on the left and right halves.  This will eventually result in a base case of a list with 1 item in it.  By definition, a list with one item in sorted, so it is returned.  As the recursive calls return, the items are concatenated with the smaller values first, the pivot (and any values that were equal to the pivot) in the middle, and the larger values on the right.      

## Radix Sort
Time Complexity:                
Space Complexity: O(n+k)

*Description:*         

## Tim Sort
Time Complexity:                
Space Complexity: O(n)             

*Description:*
