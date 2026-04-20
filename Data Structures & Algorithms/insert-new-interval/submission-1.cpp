class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
   
        auto newstart = newInterval[0];
        auto newend = newInterval[1];
        bool inserted = false;
        vector<vector<int>> output;
        for(int i = 0; i< intervals.size(); ++i){
            auto start = intervals[i][0];
            auto end =  intervals[i][1];
            if (end < newstart){
                output.push_back(intervals[i]);
                continue;
            }

            if(newend < start)
            {
                //std::cout << i << inserted << std::endl;
                if (inserted){
                    output.push_back(intervals[i]);
                    continue;
                }

                newInterval[0] = newstart;
                newInterval[1] = newend;
                output.push_back(newInterval);
                inserted = true;
                
                    output.push_back(intervals[i]);
                continue;
            }

            if (start <= newstart && newstart <= end){
                newstart = start;
            }
            if (start <= newend && newend <= end){
                newend = end;
            }
        }

        if(!inserted)
        {
             newInterval[0] = newstart;
                newInterval[1] = newend;
                output.push_back(newInterval);
        }
        //std::cout << newstart <<","<< newend;
        return output;
    }
};
