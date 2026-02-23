class Solution {
    public boolean isPalindrome(int x) {
       if (x < 0) return false;   // ✅ fix

        int originalnum = x;
        int ans = 0;

        while (x != 0) {
            int digit = x % 10;
            ans = ans * 10 + digit;
            x = x / 10;
        }

        return originalnum == ans;
    }
}