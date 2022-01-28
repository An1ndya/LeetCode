public class WordDictionary {

    node head;
    
    public WordDictionary() {
        head=null;
    }
    
    public void AddWord(string word) {
        node element = new node();
        element.s=word;
        element.next=head;
        head=element;
    }
    
    public bool Search(string word) {
        node temp = head;
        while(temp!=null)
        {
            if (word.Length==temp.s.Length)
            {
                for(int i=0;i<word.Length;i++)
                {
                    if(word[i]!= temp.s[i] && word[i]!='.' ) break;
                    if(i==word.Length-1) return true;
                }
            }
            temp=temp.next;
        }
        return false;
    }
}
public class node 
{
    public string s;
    public node next;
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.AddWord(word);
 * bool param_2 = obj.Search(word);
 */