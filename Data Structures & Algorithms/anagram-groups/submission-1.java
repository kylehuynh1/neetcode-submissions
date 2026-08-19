class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            int[] alphaCount = new int[26]; // \fresh slate for each string
            
            for (int i = 0; i < str.length(); i++) { //letter frequency
                char current = str.charAt(i);
                int index = current - 'a';
                alphaCount[index]++;
            }

            String key = Arrays.toString(alphaCount); // Turn frequency array into a key

            //check [map] , if the anagram key isnt already in there,
            //init a new arraylist and put the current word in there
            if (map.containsKey(key) == false) {
                map.put(key, new ArrayList<>());
            }

            //pull the value connected to key, and add it to the hashmap
            map.get(key).add(str);
        }

        return new ArrayList<>(map.values()); //return list of lists
    }
}