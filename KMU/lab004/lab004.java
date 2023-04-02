import java.util.*;

import javax.swing.tree.TreeNode;

import org.w3c.dom.Node;

// Name : 송도영
// Student ID : K2022007

@SuppressWarnings("unchecked")
class BST <T extends KeyValue> {

	class TreeNode <U extends KeyValue> {
		U data;	// storage for data : in HW 3, T will be Item
		TreeNode<U> leftChild;	// link to the left Child
		TreeNode<U> rightChild;	// link to the right Child

		// constructors come here
		TreeNode() {
			leftChild = rightChild = null;
		}
		TreeNode(U d) {
			// data is given
			data = d;
			// the leftChild and rightChild field are null
			leftChild = rightChild = null;
		}
	};

	TreeNode<T> root;// the reference to the root node

	BST() { 
		// BST constructor. 
		root = null;
	}

	void Show() {
		System.out.print( "Pre  Order : ");
		PreOrder(root);
		System.out.println("");
		System.out.print("In   Order : ");
		InOrder(root);
		System.out.println("");
		System.out.print("Post Order : ");
		PostOrder(root);
		System.out.println("");
		System.out.print("Number of Nodes : ");
		System.out.println( Count(root));
		System.out.print("Height : ");
		System.out.println( Height(root));
		System.out.println("");
	}

	// IMPLEMENT THE FOLLOWING FUNCTIONS

	boolean Insert(T item)  {
		// first search the key
		TreeNode<T> newNode = new TreeNode<T>(item);
		
		if(root == null) {
			root = newNode;
			return true;
		}
		TreeNode<T> currentNode = root;
		int newKey = item.GetKey();

		while(true) {
			int key = currentNode.data.GetKey();
			if (newKey == key) {
				return false;
			} else if (newKey < key) {
				if (currentNode.leftChild == null) {
					currentNode.leftChild = newNode;
					return true;
				} else {
					currentNode = currentNode.leftChild;
					continue;
				}
			} else {
				if (currentNode.rightChild == null) {
					currentNode.rightChild = newNode;
					return true;
				} else {
					currentNode = currentNode.rightChild;
					continue;
				}
			}
		}
	}

	private TreeNode<T> Find(T item) {

		TreeNode<T> currentNode = root;
		int key = item.GetKey();

		while (currentNode != null) {
			int currentKey = currentNode.data.GetKey();
			if (key == currentKey) {
				return currentNode;
			} else if (key < currentKey) {
				currentNode = currentNode.leftChild;
			} else {
				currentNode = currentNode.rightChild;
			}
		}
		return null;
	}

	private void remove(T item, TreeNode<T> predecessor) {
		TreeNode<T> currentNode = root;
		TreeNode<T> parentNode = null;
		TreeNode<T> deletingNode = Find(item);

		if (predecessor == null) {
			int itemKey = item.GetKey();

			while (currentNode != null) {
				int currentKey = currentNode.data.GetKey();
	
				if (itemKey == currentKey) {
					if (parentNode == null) {
						root = null;
						return;
					}
					else {
						if (currentNode == parentNode.leftChild) {
							parentNode.leftChild = null;
						}
						if (currentNode == parentNode.rightChild) {
							parentNode.rightChild = currentNode.rightChild;
						}
						return;
					}
				} else if (itemKey < currentKey) {
					parentNode = currentNode;
					currentNode = currentNode.leftChild;
				} else {
					parentNode = currentNode;
					currentNode = currentNode.rightChild;
				}
			}
		} else {
			int predecessorKey = predecessor.data.GetKey();
	
			while (currentNode != null) {
				int currentKey = currentNode.data.GetKey();
	
				if (predecessorKey == currentKey) {
					if (parentNode == null) {
						root = null;
						return;
					}
					else {
						deletingNode.rightChild = predecessor.rightChild;
						deletingNode.data = predecessor.data;
						// parentNode.leftChild = predecessor.leftChild;
						parentNode.rightChild = null;
						return;
					}
				} else if (predecessorKey < currentKey) {
					parentNode = currentNode;
					currentNode = currentNode.leftChild;
				} else {
					parentNode = currentNode;
					currentNode = currentNode.rightChild;
				}
			}
		}
	}

	T Get(T item)  {
		return (Find(item) == null) ? null : Find(item).data;
	} 

    private TreeNode<T> Predecessor(TreeNode<T> root) {
        TreeNode<T> node = root.leftChild;
		if (node == null) return node;

		while(node.rightChild != null) {
			node = node.rightChild;
		}
        return node;
    }

	boolean Delete(T item)  {
		TreeNode<T> node = Find(item);
		if(node == null) return false;
		TreeNode<T> predecessor = Predecessor(node);
		remove(item, predecessor);
		return true;
	}

	void PreOrder(TreeNode<T> t) {
		if (root == null) return;
		int key = t.data.GetKey();
		int value = t.data.GetValue();
		System.out.print(String.format("[%s(%s)]", key, value));
		if (t.leftChild != null) PreOrder(t.leftChild);
		if (t.rightChild != null) PreOrder(t.rightChild);
	}

	void InOrder(TreeNode<T> t) {
		if (root == null) return;
		if (t.leftChild != null) InOrder(t.leftChild);
		int key = t.data.GetKey();
		int value = t.data.GetValue();
		System.out.print(String.format("[%s(%s)]", key, value));
		if (t.rightChild != null) InOrder(t.rightChild);
	}

	void PostOrder(TreeNode<T> t) {
		if (root == null) return;
		if (t.leftChild != null) PostOrder(t.leftChild);
		if (t.rightChild != null) PostOrder(t.rightChild);
		int key = t.data.GetKey();
		int value = t.data.GetValue();
		System.out.print(String.format("[%s(%s)]", key, value));
	}

	int Count(TreeNode<T> t)  {
		return (t == null) ? 0 : 1 + Count(t.leftChild) + Count(t.rightChild);
	}

	int Height(TreeNode<T> t)  {
		if (root == null) return 0;
		int left = (t.leftChild != null) ? Height(t.leftChild) : 0;
		int right = (t.rightChild != null) ? Height(t.rightChild) : 0;
		return Math.max(left, right) + 1;
	}
}
