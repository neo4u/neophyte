// Let m=nums1.size(), and n=nums2.size()

// Solution 1: hashtable (using unordered_map).

// time complexity: max(O(m), O(n))
// space complexity: choose one O(m) or O(n) <--- So choose the
// smaller one if you can

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    if(nums1.size() > nums2.size()) return intersect(nums2, nums1);
    vector<int> ret;
    unordered_map<int,int> map1;
    for(int num:nums1) map1[num]++;
    for(int num:nums2) {
        if(map1.find(num)!=map1.end() && map1[num]>0) {
            ret.push_back(num);
            map1[num]--;
        }
    }
    return ret;
}
// Solution 2: sort + binary search

// time complexity: max(O(mlgm), O(nlgn), O(mlgn)) or max(O(mlgm),
// O(nlgn), O(nlgm))
// O(mlgm) <-- sort first array
// O(nlgn) <--- sort second array
// O(mlgn) <--- for each element in nums1, do binary search in nums2
// O(nlgm) <--- for each element in nums2, do binary search in nums1
// space complexity: depends on the space complexity used in your
// sorting algorithm, bounded by max(O(m), O(n))

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ret;
    if(nums1.empty() || nums2.empty()) return ret;
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int j=0;
    for(int i=0; i<nums1.size(); ) {
        int index = lower_bound(nums2, nums1[i]);
        int count2 = 0;
        while(index<nums2.size() && nums2[index]==nums1[i]) {
            count2++; 
            index++;
        }
        int count1 = 0;
        while(nums1[j]==nums1[i]) {
            count1++;
            j++;
        }
        ret.insert(ret.end(),min(count1,count2),nums1[i]);
        i=j;
    } 
    return ret;
}

int lower_bound(const vector<int>& nums, int target) {
    int l=0, r=nums.size()-1;
    while(l<r) {
        int m=l+(r-l)/2;
        if(nums[m]<target) {l=m+1;}
        else {r=m;}
    }
    return r;
}
// So if two arrays are already sorted, and say m is much smaller than n,
// we should choose the algorithm that for each element
// in nums1, do binary search in nums2,
// so that the complexity is O(mlgn).
// In this case, if memory is limited and nums2 is stored
// in disk, partition it and send portions of nums2 piece
// by piece. keep a pointer for nums1 indicating the
// current position, and it should be working fine~