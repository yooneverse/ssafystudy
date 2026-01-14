import java.io.*;

class Main
{
    static class Node{
        int value;
        Node left, right;
        
        Node(int value) {
            this.value = value;
        }
        Node(int value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
        }
        
        void insert(int v) {
            if (v < this.value) {
                if (this.left == null){
                    this.left = new Node(v);
                }else {
                    this.left.insert(v);
                }
            }else {
                if(this.right == null){
                    this.right = new Node(v);
                }else {
                    this.right.insert(v);
                }
            }
        }
    }
    
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Node root = new Node(Integer.parseInt(br.readLine()));
		
		String num;
		
		while(true){
		    num = br.readLine();
		    if (num == null || num.equals("")) {
		        break;
		    }
		    root.insert(Integer.parseInt(num));
		}
		
		postOrder(root);
	}
	
	static void postOrder(Node node) {
	    if (node == null){
	        return;
	    }
	    
	    postOrder(node.left);
	    postOrder(node.right);
	    System.out.println(node.value);
	}
}
