class Solution {
    public boolean isPalindrome(String s) {
        String last = "";
        for(int i=0; i<s.length(); i++){
            Character current = s.charAt(i);
            if(Character.isLetter(current)){
                last+=Character.toLowerCase(s.charAt(i));
            }
            if(Character.isDigit(current)){
                last+=s.charAt(i);
            }
        }
        System.out.println(last);
        int k = last.length()-1;
        for(int j=0; j<=k;j++){
            Character beg = last.charAt(j);
            Character end = last.charAt(k);
            if(beg.equals(end)==false){
                return false;
            }
            k--;
        }
        return true;
    }
}
