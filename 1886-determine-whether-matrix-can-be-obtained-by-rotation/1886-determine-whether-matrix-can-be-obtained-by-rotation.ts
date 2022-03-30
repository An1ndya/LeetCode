function findRotation(mat: number[][], target: number[][]): boolean 
{
    if(isEqual(mat,target)) return true;
    
    for(let i=0;i<3;i++)
    {
        mat = Rotate90(mat);
        if(isEqual(mat,target)) return true;
    }
    return false;
};
function Rotate90(mat: number[][]): number[][] 
{
    //transpose+mirror
    return mirror(transpose(mat));
};
function transpose(mat: number[][]):number[][]
{
    let n = mat.length;
    for(let i =0;i<n;i++)
    {
        for(let j=0;j<i;j++)
        {
            let temp = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = temp;
        }
    }
    return mat;
};
function mirror(mat: number[][]): number[][]
{
    let n = mat.length;
    for(let i =0;i<n;i++)
    {
        for(let j=0;j<n/2;j++)
        {
            let temp = mat[i][j];
            mat[i][j] = mat[i][n-1-j];
            mat[i][n-1-j] = temp;
        }
    }
    return mat;
};
function isEqual(mat: number[][], target: number[][]): boolean 
{
    if(mat.length!=target.length) return false;
    if(mat[0].length!=target[0].length) return false;
    
    let n = mat.length; 
    let m = mat[0].length; 
    for(let i=0;i<n;i++)
    {
        for(let j=0;j<m;j++)
        {
            if(mat[i][j]!=target[i][j]) return false;
        }
    }
    return true;
};