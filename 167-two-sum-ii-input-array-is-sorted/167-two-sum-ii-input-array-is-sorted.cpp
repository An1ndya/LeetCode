class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int maxvalue = 1000;
        int minvalue = -1000;
        int size = maxvalue - minvalue + 2;
        int aravalueindex[size]; //store index 
        for(int i=0;i<size;i++) aravalueindex[i] = -1;
        int probableValue;
        int index1, index2;
        for(int i=0;i<numbers.size();i++)
        {
            probableValue = target - numbers[i];
            if(aravalueindex[probableValue-minvalue] > -1){
                return {aravalueindex[probableValue-minvalue]+1, i+1};
                
            }
            aravalueindex[numbers[i]-minvalue] = i;
        }
        return {0,0};
    }
};