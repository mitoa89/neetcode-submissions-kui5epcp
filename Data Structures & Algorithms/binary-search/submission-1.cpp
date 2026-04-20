#include <print>
#include <numeric>
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int begin = 0;
        int end = nums.size() - 1;

        while(begin <= end)
        {
            int mid = begin + (end - begin)/2;
           // std::print("mid: {}", mid);
            auto value = nums[mid];

            if (value == target){
                return mid;
            }
            else if(value < target){
                begin = mid+1;
            }
            else{
                end = mid -1;
            }
        }

        return -1;
    }
};
