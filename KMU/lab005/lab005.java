import java.util.*;

// Name :
// Student ID :


class HeapSort {
	int [] heap;	// Heap Array
	int heapSize;	// number of elements in the Heap

	HeapSort(int cap) {
		heap = new int[cap + 1];
		heapSize = 0;
	}

	public String toString() { 
		// Convert heap array into a string
		String str;
		str = "Heap : - ";

		for(int i = 1; i <= heapSize; i++)
			str +=  heap[i] + "  ";

		return str;
	}

	void  Init(int [] es, int n) {	
		// fill the heap array by the input
		// we need to create heap structure when we call Sort()
		heapSize = n;
		for(int i = 1; i <= n; i++)
			heap[i] = es[i];
	}


	void  Adjust(int root, int n) {	
		// adjust binary tree with root "root" to satisfy heap property.
		// The left and right subtrees of "root" already satisfy the heap
		// property. No node index is > n.

		//	"NEED TO IMPLEMENT" 






	}

	void  Sort() {	
		// sort heap[1:n] into nondecreasing order
		//	"NEED TO IMPLEMENT" 





	}
}

