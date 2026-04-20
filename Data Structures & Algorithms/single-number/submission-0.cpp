class Solution {
public:
    int singleNumber(vector<int>& nums) {

        int r = 0;
        for(auto num : nums){
            r = r ^ num;
        }
        return r;
    }
};
