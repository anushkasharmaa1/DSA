class Solution {
    public int countCharacters(String[] words, String chars) {

        int[] base = new int[26];

        for(char c : chars.toCharArray())
            base[c - 'a']++;

        int sum = 0;

        for(String word : words){

            int[] count = base.clone();
            boolean valid = true;

            for(char c : word.toCharArray()){

                if(count[c - 'a'] == 0){
                    valid = false;
                    break;
                }

                count[c - 'a']--;
            }

            if(valid)
                sum += word.length();
        }

        return sum;
    }
}