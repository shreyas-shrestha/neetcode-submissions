class Solution {
    public int getSum(int a, int b) {
        int count = 0;
        if (a>0){
            for(int i = 0; i<a; i++){
                count++;
            }   
        } else {
            for(int i = 0; i<Math.abs(a); i++){
                count--;
            }
        }
        if (b>0){
            for(int i = 0; i<b; i++){
                count++;
            }   
        } else {
            for(int i = 0; i<Math.abs(b); i++){
                count--;
            }
        }
        return count;
    }
}
