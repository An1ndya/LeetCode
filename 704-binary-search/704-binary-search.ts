function search(nums: number[], target: number): number {
  let low = 0;
  let high = nums.length - 1;
  while (low <= high) 
  {
    let mid = Math.floor((low + high) / 2);
    
    if (nums[mid] === target) {
      return mid;
    }
    if (target > nums[mid])
    {
      low = mid + 1;
    } 
    else 
    {
      high = mid - 1;
    }
  }
  return -1;

};