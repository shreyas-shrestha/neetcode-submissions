class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet <Integer> mySet = new HashSet<>();
        for (int i : nums) {
            if (mySet.contains(i)) {
                return true;
            }
            mySet.add(i);
        }
        return false;
    }
}