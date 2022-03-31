function groupAnagrams(strs: string[]): string[][] 
{
    let ans:string[][]  = [];
    let hash  = {};
    let n =  strs.length;
    for(let i =0;i<n;i++)
    {
        let key = anagramKey(strs[i]);
        if(key in hash)
        {
            hash[key].push(strs[i]);
        }else
        {
            hash[key]=[strs[i]];
        }
    }
    for( let key in hash)
    {
        ans.push(hash[key]);
    }
    return ans;
};
function anagramKey(str1: string): string
{
    let charcount = new Array(26).fill(0);
    for(let i =0;i <str1.length; i++)
    {
        charcount[str1[i].charCodeAt(0)-'a'.charCodeAt(0)]++;
    } 
    let key = "";
    for(let i =0;i <26; i++)
    {
        key+= String.fromCharCode(97 + i) + charcount[i];
    } 
    return key;
};
