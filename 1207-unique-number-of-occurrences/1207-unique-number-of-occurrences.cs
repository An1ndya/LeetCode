public class Solution {
    public bool UniqueOccurrences(int[] arr) 
    {
        Dictionary<int, int> hashMapOccurances = new Dictionary<int, int>();
        Dictionary<int, bool> hashMapUnique = new Dictionary<int, bool>();
        for(int i=0; i<arr.Length; i++)
        {
            if(hashMapOccurances.ContainsKey(arr[i]))
                hashMapOccurances[arr[i]]+=1;
            else
                hashMapOccurances[arr[i]]= 1;
        }
        foreach(int occurance in hashMapOccurances.Values)
        {
            if(hashMapUnique.ContainsKey(occurance))
                return false;
            
            hashMapUnique[occurance]=true;
        }
        return true;
    }
}