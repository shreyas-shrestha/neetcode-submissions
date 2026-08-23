class Solution {
    HashMap<Integer, Integer> comp = new HashMap<>();
    public boolean hasDuplicate(int[] nums) {
    for(int i = 0; i<nums.length; i++){
        if (comp.containsKey((Integer) nums[i])){
            return true;
        }
        comp.put((Integer) nums[i], (Integer) nums[i]);
    }
    return false;   
    }
}