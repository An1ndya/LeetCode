function groupAnagrams(strs: string[]): string[][] 
{
    let ans:string[][]  = [];
    let hash  = {};
    let n =  strs.length;
    for(let i =0;i<n;i++)
    {
        //using a key like a2b3c1 to hashing different anagram
        let key = anagramKey(strs[i]);
        if(key in hash)
        {
            //if key exist just push in that array
            hash[key].push(strs[i]);
        }else
        {
            //create a new array with a inital anagram
            hash[key]=[strs[i]];
        }
    }
    for( let key in hash)
    {
        //transfer all anagram array from hash to a array
        ans.push(hash[key]);
    }
    return ans;
};
function anagramKey(str1: string): string
{
    let charcount = new Array(26).fill(0);
    for(let i =0;i <str1.length; i++)
    {
        //store all character count of a word
        charcount[str1[i].charCodeAt(0)-'a'.charCodeAt(0)]++;
    } 
    let key = "";
    for(let i =0;i <26; i++)
    {
        //using a key like a2b3c1 to hashing different anagram
        key+= String.fromCharCode(97 + i) + charcount[i];
    } 
    return key;
};