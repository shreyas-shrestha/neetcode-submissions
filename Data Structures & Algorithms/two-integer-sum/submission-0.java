class Solution {
    HashMap<Integer,Integer> tracker = new HashMap<>();
    int[] val = new int[2];
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length; i++){
            int complement = target -nums[i];
            if(tracker.containsKey((Integer) complement)){
                val[1] = i;
                val[0] = (int) tracker.get((Integer) complement);
            }
            tracker.put((Integer) nums[i], (Integer) i);
        }
        return val;
    }
}
