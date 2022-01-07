public class Solution {
    public string ReverseWords(string s){
        string[] arr = s.Split(' ');
        s="";
        for(int i=0;i<arr.Length;i++)
        {
            s = s + Reverse(arr[i]);
            if(i !=arr.Length-1 ) s = s + " ";
        }  
        return s;
    }
    public string Reverse(string text)
    {
       if (text == null) return null;
        
       char[] array = text.ToCharArray();
       Array.Reverse(array);
       return new String(array);
    }
}