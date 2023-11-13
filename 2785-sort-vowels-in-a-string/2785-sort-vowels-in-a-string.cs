public class Solution {
    public string SortVowels(string s) {
        //Console.WriteLine(s[0].GetType());
        int n=s.Length;
        StringBuilder t = new StringBuilder(n);
        List<int> vowels = new List<int>();
        for(int i=0;i<n;i++)
        {
            switch(s[i])
            {
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    vowels.Add((int)s[i]);
                    break;
            }
        }
        vowels.Sort();
        int vindex=0;
        for(int i=0;i<n;i++)
        {
            switch(s[i])
            {
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    t.Append((char)vowels[vindex]);
                    vindex++;
                    break;
                default:
                    t.Append(s[i]);
                    break;
            }
        }
        return t.ToString();
    }
}