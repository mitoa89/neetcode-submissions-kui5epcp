class Solution {
public:
    vector<int> countBits(int n) {
        auto getCount = [](int num){
            int cnt = 0;
            while(num > 0){
                if(num & 1) ++cnt;
                
                num = num >> 1;
            }
            return cnt;
        };

        vector<int> v;
        for(int i =0; i<=n; ++i){
            v.push_back(getCount(i));
        }
        return v;
    }
};
