class Solution {
    HashMap<Character, Integer> sChars = new HashMap<>();
    HashMap<Character, Integer> tChars = new HashMap<>();
    public boolean isAnagram(String s, String t) {
        for(int i = 0; i<s.length(); i++){
            if(sChars.containsKey((Character) s.charAt(i))){
                Integer count = sChars.get((Character) s.charAt(i)) + (Integer) 1;
                sChars.replace((Character) s.charAt(i), count);
            }
            else{
                sChars.put((Character) s.charAt(i), (Integer) (1));
            }
        }
        for(int j = 0; j<t.length(); j++){
            if(tChars.containsKey((Character) t.charAt(j))){
                Integer count = tChars.get((Character) t.charAt(j)) + (Integer) 1;
                tChars.replace((Character) t.charAt(j), count);
            }
            else{
                tChars.put((Character) t.charAt(j), (Integer) (1));
            }
        }
    return tChars.equals(sChars);
    }
}

