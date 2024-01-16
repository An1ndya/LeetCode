public class RandomizedSet {
    Dictionary<int, int> hashMap;
    List<int> list;
    public RandomizedSet(){
        hashMap = new Dictionary<int, int>();
        list=new List<int>(); 
    }
    
    public bool Insert(int val) {
        if(hashMap.ContainsKey(val))
            return false;
        else
            hashMap[val] = list.Count;
            list.Add(val);
            return true;
    }
    
    public bool Remove(int val) {
        if(hashMap.ContainsKey(val)){
            int index = hashMap[val];
            //int lastindex= list.Count-1;
            list[index] = list[list.Count-1];
            hashMap[list[index]]=index;
            list.RemoveAt(list.Count - 1);
            hashMap.Remove(val);
            return true;
        }
        else
            return false;
    }
    
    public int GetRandom() {
        return list[new Random().Next(list.Count)];

    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */