Heap sort
==========

Max/min heap을 이용하면 정렬할 수 있다.

Heap sort는 전체 자료를 정렬하는 것이 아니라 가장 큰 값 몇 개만 필요할 때이다.


======
Codes
======

Heap sort::

    void heap_sort(element a[], int n)
    {
        int i;
        HeapType h;

        init(&h);
        for(i = 0; i < n; i++)
            insert_max_heap(&h, a[i]);

        for (i = 0; i >= 0; i--)
            a[i] = delete_max_heap(&h);
    }


===============
Time complexity
===============

요소의 개수가 n개이므로 Heap에 삽입하거나 삭제할 때, Heap을 재정비하는 시간이 log2n 만큼 소요됨
→ O(nlog2n)


**References**
    * C언어로 쉽게 풀어쓴 자료 구조, 천인국 저