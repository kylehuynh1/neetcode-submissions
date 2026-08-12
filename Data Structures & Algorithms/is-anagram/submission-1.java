class Solution {
    public boolean isAnagram(String s, String t) {
        int[] countsS = new int[26];
        int[] countsT = new int[26];

        //counter letter freq. for string s
        for(int i = 0; i < s.length(); i++){
            char current = s.charAt(i);
            int index = current - 'a';
            countsS[index]++;
        }

        //count letter freq. for string t
        for(int j = 0; j < t.length(); j++){
            char current = t.charAt(j);
            int index = current - 'a';
            countsT[index]++;
        }

        //utilize arrays.equals fcn to compare letter contents for both strings
        if(Arrays.equals(countsS, countsT))
            return true;
        
        return false;
    }
}
