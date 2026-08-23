class Solution {
    LinkedList<Character> chars = new LinkedList<>();
    int maxCount = 0;
    int current = 0;
    public int lengthOfLongestSubstring(String s) {
        for(int i = 0; i<s.length();i++){
            if(chars.contains(s.charAt(i))==false){
                chars.add((Character) s.charAt(i));
                current++;
            } else {
                chars.subList(0,chars.indexOf(s.charAt(i))+1).clear();
                chars.add((Character) s.charAt(i));
                current = chars.size();
            }
            if(current>maxCount){
                maxCount = current;
            }
        }
        return maxCount;
    }
}
