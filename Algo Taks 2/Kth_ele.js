/* 
7- K-th Element of Two Sorted Arrays Given two sorted
arrays of size m and n respectively, you are tasked 
with finding the element that would be at the k’th position
of the final sorted array.
_____________
|psuedo code|
|___________| 
find_Kth_Ele(arr1,arr2,k)
m=len of arr1
n=len of arr2
if m>n
 return find_Kth_Ele(arr2,arr1,k)
else 
low =0
high =m
while low<=high
i=(low+high)/2 -> round to floor
j=k-i
if L1>R2
high =i-1
else if L2>R1
low=i+1
else return max(L1,L2)
*/

function find_Kth_Ele(arr1, arr2, k){
  let m = arr1.length, n = arr2.length;
  if (m > n) {
    return find_Kth_Ele(arr2, arr1, k)
  }
  else {
    let low = 0, high = m;
    while (low <= high) {
      let i=Math.floor((low + high) / 2), j = k - i;
      let L1 = (i === 0) ? -Infinity : arr1[i - 1];
      let R1 = (i === m) ? Infinity : arr1[i];
      let L2 = (j === 0) ? -Infinity : arr2[j - 1];
      let R2 = (j === n) ? Infinity : arr2[j];
      if (L1> R2) {
        high=i-1;
      }
      else if (L2 > R1){
        low=i+1
      }
      else {return `The ${k}th element is : ${Math.max(L1,L2)}`;}
    }
  }
}
let arr1 = [2 ,3, 6, 7, 9] , arr2 =[1, 4, 8, 10] , k = 5;
document.writeln(find_Kth_Ele(arr1, arr2, k));