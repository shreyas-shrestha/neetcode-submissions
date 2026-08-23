class LRUCache {
    private int capacity;
    HashMap<Integer, Integer> comp = new HashMap<>();
    LinkedList<Integer> order = new LinkedList<>();
    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if(comp.get(key)!=null){
            order.remove((Integer) key);
            order.add((Integer) key);
            return comp.get(key);
        }
        return -1;
    }
    
    public void put(int key, int value) {
        comp.put((Integer) key, (Integer) value);
        order.remove((Integer) key);
        order.add((Integer) key);
        if(comp.size()>capacity){
            comp.remove(order.get(0));
            order.remove(0);
        }
    }
}
