class Solution {
    HashMap<Integer, Integer> vals = new HashMap<>();
    int[] sum = new int[2];
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i<numbers.length;i++){
            Integer complement = target - numbers[i];
            if(vals.containsKey(complement)){
                sum[0] = (int) vals.get(complement) + 1;
                sum[1] = i+1;
                return sum;
            }
            vals.put((Integer) numbers[i], (Integer) i);
        }
        return sum;
    }
}
