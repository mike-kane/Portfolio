# Sorting Algorithms

## Selection Sort
Time Complexity: O(n<sup>2</sup>)      
Space Complexity: O(1)

*Description:*
Selection Sort works by 'selecting' the largest element in the list and moving it to the end of the list--in a list of length n, the index would be n-1.  Next, it iterates through the list and selects the second largest element in the list, and places it at index (n-2). This process is repeated until the list is fully sorted.  

Since the sort can be done in-place, the space complexity of Selection Sort is O(1).  The space complexity is bounded at O(n<sup>2</sup>).  This is because Selection Sort contains an outer loop (starting at the end of the list and iterating backwards) and an inner loop (iterating from the start of the list up to the current position of the outer loop).  

It is worth noting that as selection sort progresses, the range of the inner loop gets smaller and smaller.  This means that the time complexity of selection sort is actually better than O(n<sup>2</sup>), although according to the rules of Big O, we ignore this and still classify the time complexity of this sort as 0(n<sup>2</sup>).

## Bucket Sort
Time Complexity:                     
Space Complexity: O(n)             

## Gnome Sort  
Time Complexity:                
Space Complexity:  

*Description:*                

## Heap Sort
Time Complexity:                
Space Complexity: O(1)         

## Insertion Sort
Time Complexity:                              
Space Complexity: O(1)                            

*Description:*  

## Intro Sort
Time Complexity:                
Space Complexity:               

## Merge Sort
Time Complexity:                
Space Complexity: O(n)

*Description:*   Merge sort is a classic "divide-and-conquer" algorithm.  The algorithm starts by dividing the list in half, and then cutting each of those section half, again and again until each list is a single item.  Once the list is divided into a bunch of sublists each containing one item, the "conquer" part begins.  This is where Merge Sort gets its name--the algorithm then combines individual items into lists of two items, putting the smaller item first.  To be specific, the algorithm uses 3 pointers--1 for each sub list (we'll call them _left_ and _right_), and one to keep track of the main list and where the items go within it.  The algorithm compares the data _left_ and _right_ are pointing at, and selects the smaller value to be added to the main list.  The _left_ or _right_ pointer that was pointing at the smaller data is then incremented, moving onto the next item in its list.  This process is repeated until both sub lists have been merged into the main list, and then repeated on the next set of sub lists.  This process repeats until all sub lists have been merged back into 1 main list, but now in sorted order!

## Quick Sort
Time Complexity:                
Space Complexity: O(log(n))         

## Radix Sort
Time Complexity:                
Space Complexity: O(n+k)          

## Tim Sort
Time Complexity:                
Space Complexity: O(n)             
