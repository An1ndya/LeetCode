public class Solution {
    public string CapitalizeTitle(string title) {
        string[] arr = title.Split(" ");
        title = "";
        for(int i=0;i<arr.Length;i++){
            if(arr[i].Length > 2)
            {
                title = title + TitleCaseString(arr[i]);
            }
            else{
                title = title + arr[i].ToLower();
            }
            if(i!=arr.Length-1)  title = title + " ";
        }
        return title;
    }
    public static String TitleCaseString(String s)
    {
        if (s == null) return s;

        String[] words = s.Split(' ');
        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].Length == 0) continue;

            Char firstChar = Char.ToUpper(words[i][0]); 
            String rest = "";
            if (words[i].Length > 1)
            {
                rest = words[i].Substring(1).ToLower();
            }
            words[i] = firstChar + rest;
        }
        return String.Join(" ", words);
    } 
}