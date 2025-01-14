> We can build a heap by repeatedly calling $\text{MAX-HEAP-INSERT}$ to insert the elements into the heap. Consider the following variation of the $\text{BUILD-MAX-HEAP}$ procedure:
>
> ```cpp
> BUILD-MAX-HEAP'(A)
>     A.heap-size = 1
>     for i = 2 to A.length
>         MAX-HEAP-INSERT(A, A[i])
> ```
>
> **a.** Do the procedures $\text{BUILD-MAX-HEAP}$ and $\text{BUILD-MAX-HEAP}'$ always create the same heap when run on the same input array? Prove that they do, or provide a counterexample.
>
> **b.** Show that in the worst case, $\text{BUILD-MAX-HEAP}'$ requires $\Theta(n\lg n)$ time to build a $n$-element heap.

**a.** Consider the following counterexample.

- Input array $A = \langle 1, 2, 3 \rangle$:
- $\text{BUILD-MAX-HEAP}(A)$: $A = \langle 3, 2, 1 \rangle$.
- $\text{BUILD-MAX-HEAP}'(A)$: $A = \langle 3, 1, 2 \rangle$.

**b.** If the array A has been sorted and all elements in A are distinct. Each inserted node has to travel all the way up to the root, which takes $\Theta(\log (heapsize))$ time.

$$
\sum_{i=1}^{n} \log_2(i) = \Theta(n\lg n)
$$
