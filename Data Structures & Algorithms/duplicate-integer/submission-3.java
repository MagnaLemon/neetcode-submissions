class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> li = new HashSet<Integer>();
        for (int i: nums)
        {
            if (li.contains(i))
                return true;
            else
                li.add(i);
        }
        return false;
    }
}
