class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        ArrayList<int[]> ans = new ArrayList<int[]>();
        int m = firstList.length;
        int n = secondList.length;
        int i=0 ,j =0; 
        if (m ==0 || n==0) return new int[][]{}; 
        while(i<m && j < n){
            int[] a = firstList[i];
            int[] b = secondList[j];
            
            if (a[1] < b[1]){
                int[] intervel = intersection(a,b);
                if (intervel.length!=0) ans.add(intervel);
                i++;
            }else{
                int[] intervel = intersection(b,a);
                if (intervel.length!=0) ans.add(intervel);
                j++;
            }
            
        }

        return arrayList2darray(ans);
    }
    public int[] intersection(int[] first, int[] second){
    
            //second bigger
            if (first[1] >= second[0]){
                //overlap
                int a = Math.max( first[0], second[0]);
                int b = Math.min( first[1], second[1]);
                return new int[]{a,b};
            }
            else{
                return new int[]{};
            }  
    }
    public int[][] arrayList2darray(ArrayList<int[]> list){
        int size = list.size();
        int col = list.get(0).length;
        int[][] result = new int[size][col];
                   
        for(int i=0;i<size;i++){
            result[i] = list.get(i);
        } 
        return result;
    }
}