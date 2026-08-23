class Solution {
    HashSet<Integer> comp = new HashSet<>();
    public int missingNumber(int[] nums) {
        for(int i =0; i<nums.length;i++){
            comp.add((Integer) nums[i]);
        }
        for(int i =0; i<nums.length; i++){
            if(comp.contains((Integer) i)==false){
                return i;
            }
        }
        return nums.length;
    }
}
