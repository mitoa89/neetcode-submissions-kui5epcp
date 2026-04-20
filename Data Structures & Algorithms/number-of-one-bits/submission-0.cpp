#include <iostream>
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int num = 0;
        for(int i = 0; i<= 32; ++i){
            long test =  std::pow(2, i);
            bool is = n & test;
            if(is){
                num++;
            }

        }
        return num;

    }
};
