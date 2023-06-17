class Node{
    int data;
    Node next;

    Node(int d){
        this.data = d;
        this.next = null;
    }

    //insertion at LAST
    static void insertAtLast(Node head, int d){
        Node temp = head;
        Node newnode = new Node(d);
        while (temp.next != null){

            temp = temp.next;
        }

        temp.next = newnode;

    }

    void solve(int[] arr, Node head)
    {
        for(int i=0;i<arr.length; i++){
            insertAtLast(head, arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in):
    }
}