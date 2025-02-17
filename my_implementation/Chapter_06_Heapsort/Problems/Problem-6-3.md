> An $m \times n$ Young tableau is an $m \times n$ matrix such that the entries of each row are in sorted order from left to right and the entries of each column are in sorted order from top to bottom. Some of the entries of a Young tableau may be $\infty$, which we treat as nonexistent elements. Thus, a Young tableau can be used to hold $r \le mn$ finite numbers.
>
> **a.** Draw $4 \times 4$ tableau containing the elements $\\{9, 16, 3, 2, 4, 8, 5, 14, 12\\}$.
>
> **b.** Argue that an $m \times n$ Young tableau $Y$ is empty if $Y[1, 1] = \infty$. Argue that $Y$ is full (contains $mn$ elements) if $Y[m, n] < \infty$.
>
> **c.** Give an algorithm to implement $\text{EXTRACT-MIN}$ on a nonempty $m \times n$ Young tableau that runs in $O(m + n)$ time. Your algorithm should use a recursive subroutine that solves an $m \times n$ problem by recursively solving either an $(m - 1) \times n$ or an $m \times (n - 1)$ subproblem. ($\textit{Hint:}$ Think about $\text{MAX-HEAPIFY}$.) Define $T(p)$ where $p = m + n$, to be the maximum running time of $\text{EXTRACT-MIN}$ on any $m \times n$ Young tableau. Give and solve a recurrence relation for $T(p)$ that yields the $O(m + n)$ time bound.
>
> **d.** Show how to insert a new element into a nonfull $m \times n$ Young tableau in $O(m + n)$ time.
>
> **e.** Using no other sorting method as a subroutine, show how to use an $n \times n$ Young tableau to sort $n^2$ numbers in $O(n^3)$ time.
>
> **f.** Give an $O(m + n)$-time algorithm to determine whether a given number is stored in a given $m \times n$ Young tableau.

**a.**

$$
\begin{matrix}
     2 &      3 &     12 & 14     \\\\
     4 &      8 &     16 & \infty \\\\
     5 &      9 & \infty & \infty \\\\
\infty & \infty & \infty & \infty
\end{matrix}
$$

**b.** If the top left element is $\infty$, then all the elements on the first row need to be $\infty$. But if this is the case, all other elements need to be $\infty$ because they are larger than the first element on their column.

If the bottom right element is smaller than $\infty$, all the elements on the bottom row need to be smaller than $\infty$. But so are the other elements in the tableau, because each is smaller than the bottom element of its column.

**c.** The $A[1, 1]$ is the smallest element. We store it, so we can return it later and then replace it with $\infty$. This breaks the Young tableau property and we need to perform a procedure, similar to $\text{MAX-HEAPIFY}$, to restore it.

We compare $A[i, j]$ with each of its neighbours and exchange it with the smallest. This restores the property for $A[i, j]$ but reduces the problem to either $A[i, j + 1]$ or $A[i + 1, j]$. We terminate when $A[i, j]$ is smaller than its neighbours.

The relation in question is

$$T(p) = T(p - 1) + O(1) = T(p - 2) + O(1) + O(1) = \cdots = O(p).$$

**d.** The algorithm is very similar to the previous, except that we start with the bottom right element of the tableau and move it upwards and leftwards to the correct position. The asymptotic analysis is the same.

**e.** We can sort by starting with an empty tableau and inserting all the $n^2$ elements in it. Each insertion is $O(n + n) = O(n)$. The complexity is $n^2O(n) = O(n^3)$. Afterwards we can take them one by one and put them back in the original array which has the same complexity. In total, its $O(n^3)$.

We can insert elements in place. We imagine the array that stores $n^2$ numbers as a n x n matrix. We insert A[1, 2] into the 1 x 2 Young tableau. We insert A[1, 3] into the 1 x 3 Young tableau. We insert A[1, n] into the 1 x n Young tableau. We insert A[2, 1] into the 2 x 1 Young tableau. We insert A[2, 2] into the 2 x 2 Young tableau. ... Finally we insert A[n, n] into the n x n Young tableau. The time complexity of this in-place insertion algorithm is as follows, which is faster by a constant factor than the previous algorithm.

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} (i+j) = n^2(n+1)
$$

**f.** We start from the bottom-left corner. We check the current element $current$ with the one we're looking for $key$ and move up if $current > key$ and right if $current < key$. We declare success if $current = key$ and otherwise terminate if we walk off the tableau.


my first wrong answer was: start from the top-left corner.
The key is whenever you move right/left one column, you can make sure the previous column doesn't have the key. Whenever you move up/down one row, you can make sure the previous row doesn't have the key.