class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int minBuy = 100;
        for(int i = 0; i<prices.length;i++){
            if(prices[i]<minBuy){
                minBuy = prices[i];
            }
            if(prices[i]-minBuy>max){
                max=prices[i]-minBuy;
            }
        }
        return max;
    }
}
