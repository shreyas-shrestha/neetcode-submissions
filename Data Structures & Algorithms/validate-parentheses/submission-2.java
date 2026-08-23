class Solution {
    public boolean isValid(String s) {
        Stack<Character> myStack = new Stack<>();
        for(int i = 0; i<s.length();i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '{'||
                s.charAt(i) =='['){
                myStack.push((Character) s.charAt(i));
            }
            if(myStack.size()==0){
                return false;
            }
           if(s.charAt(i) == ')'){
                char current = myStack.pop();
                if(!(current == '(')){
                    return false;
                }
            }
            if(s.charAt(i) == '}'){
                char current = myStack.pop();
                if(!(current == '{')){
                    return false;
                }
            }
            if(s.charAt(i) == ']'){
                char current = myStack.pop();
                if(!(current == '[')){
                    return false;
                }
            }
        }
        if(myStack.size() != 0){
            return false;
        }
        return true;
    }
}
