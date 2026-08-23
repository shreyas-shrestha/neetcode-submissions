class MinStack {
    LinkedList<Integer> myList;
    int minVal;

    public MinStack() {
        myList = new LinkedList();
        minVal = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        myList.addFirst(val);
        if (val < minVal) {
            minVal = val;
        }
    }
    
    public void pop() {
        int removed = myList.removeFirst();
        if (removed == minVal) {
            minVal = Integer.MAX_VALUE;
            for (int i : myList) {
                if (i < minVal) {
                    minVal = i;
                }
            }
        }
    }
    
    public int top() {
        return myList.get(0);
    }
    
    public int getMin() {
        return minVal;
    }
}
