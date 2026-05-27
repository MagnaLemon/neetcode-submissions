class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> li = new ArrayList<Integer>();
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
