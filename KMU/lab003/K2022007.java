import java.util.*;

// Name :
// Student ID :


class Chain <T> {
	
	class ChainNode <U> {
		private U data;	// storage for data
		private ChainNode<U> link;	// link to the next node

		// constructors come here
		ChainNode() {
			this.link = null;
			// the link field is null 
		}
		ChainNode(U data) {
			// set the data field only 
			this.data = data;
		}
		ChainNode(U data, ChainNode<U> link) {
			// set the data field and link field
			this.data = data;
			this.link = link;
		}
	};

	private ChainNode<T> first; // reference to the fist node

	Chain() { 
		first = null;
	}

	boolean IsEmpty() {
		return first == null;
	}

	/**
	 * Show all the elements in the Chain in sequence
	 */
	public String toString() { 
		ChainNode<T> p = first;

		String str = new String();
		str = String.format("List (%d) : ", Size());

		// show all the nodes
		while (p != null) {
			str += p.data + " ";
			p = p.link;
		}
		return str;
	}

	/**
	 * insert theElement in theIndex
	 */

	boolean Insert(int theIndex, T theElement) {

		if (theIndex > Size()) return false;

		ChainNode<T> newNode = new ChainNode<T>(theElement);
		ChainNode<T> currentNode = first;

		if (IsEmpty()) {
			first = newNode;
		} else {
			if (theIndex == 0) {
				ChainNode<T> nextNode = first;
				newNode.link = nextNode;
				first = newNode;
			} else {
				for (int i = 0; i < theIndex - 1; i++) {
					currentNode = currentNode.link;
				}
				ChainNode<T> nextNode = currentNode.link;
				currentNode.link = newNode;
				newNode.link = nextNode;
			}
		}
		return true;
	}

	/**
	 * delete an element from the first 
	 */
	T DeleteFront() {
		if (IsEmpty()) {
			return null;
		} else {
			T data = first.data;
			first = first.link;
			return data;
		}
	}

	/**
	 * return the number of elements in Chain
	 */
	final int  Size() {
		ChainNode<T> p = first;
		int cnt = 0;
		while (p != null) {
			cnt++;
			p = p.link;
		}
		return cnt;
	}
}
