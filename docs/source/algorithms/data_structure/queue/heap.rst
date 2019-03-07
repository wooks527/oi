Heap
=====

완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조


=======
Types
=======

.. figure:: img/heap_types.png
    :align: center
    :scale: 40%


* Max heap (최대 히프)
    * key (부모 노드) >= key (자식 노드)
* Min heap (최소 히프)
    * key (부모 노드) <= key (자식 노드)


===============
Implementation
===============

.. figure:: img/heap_implementation.png
    :align: center
    :scale: 40%


Heap::

    #define MAX_ELEMENT 200
    typedef struct {
        int key;
    } element;
    typedef struct {
        element heap[MAX_ELEMENT];
        int heap_size;
    }


============
Insertion
============

.. figure:: img/heap_insertion.png
    :align: center
    :scale: 40%


Insertion::

    void insert_max_heap(HeapType *h, element item)
    {
        int i;
        i = ++(h->heap_size);

        while((i != 1) && (item.key > h->heap[i/2].key)) {
            h->heap[i] = h->heap[i/2];
            i /= 2;
        }
        h->heap[i] = item;
    }


**Time complexity**

Worse case
* 루트 노드까지 올라가야 하므로 트리의 높이에 해당하는 비교/이동 연산이 필요
* O(log2n)


===========
Deletion
===========

.. figure:: img/heap_deletion.png
    :align: center
    :scale: 40%


**Codes**

Deletion::

    element delete_max_heap(HeapType *h)
    {
        int parent, child;
        element item, temp;

        item = h->heap[1];
        temp = h->heap[(h->heap_size)--];
        parent = 1;
        child = 2;
        while(child <= h->heap_size) {
            if ((child < h->heap_size) && (h->heap[child].key) < h->heap[child+1].key)) child++;
            if(temp.key >= h->heap[child].key) break;
            h->heap[parent] = h->heap[child];
            parent = child;
            child *= 2;
        }
        h->heap[parent] = temp;

        return item;
    }


**Time complexity**

Worse case
* 가장 아래 레벨까지 내려가야 하므로 트리의 높이 만큼의 시간이 걸림
* O(log2n)


===============
Utilization
===============

* `Heap sort <https://oi.readthedocs.io/en/latest/algorithms/sort/heap_sort.html>`_
* Simulation


**References**
    * C언어로 쉽게 풀어쓴 자료 구조, 천인국 저
    * https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html