import java.util.*;

// Name :
// Student ID :

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

	TreeNode <T> root;// the reference to the root node

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

	boolean  Insert(T item)  {
		// first search the key
		if(root == null) {


			return true;
		}

		TreeNode<T> ptr, parent;



		return true;
	}

	T Get(T item)  {
		// use the key field of item and find the node
		// do not use val field of item
		TreeNode<T> ptr;
		ptr = root;



		return ptr.data;
	} 


	boolean Delete(T item)  {
		if(root == null)
			return false;	// non existing key

	




		return true;
	}

	void  PreOrder(TreeNode<T> t)  {



	}

	void  InOrder(TreeNode<T> t)  {



	}

	void  PostOrder(TreeNode<T> t)  {



	}

	int  Count(TreeNode<T> t)  {


		return 0;
	}

	int  Height(TreeNode<T> t)  {



		return 0;
	}
}


