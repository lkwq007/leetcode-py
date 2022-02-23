class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt=[0]*(len(nums2)+1)
        def update(pos,val):
            while pos<len(nums1):
                cnt[pos]+=val
                pos=pos|(pos+1)
        def get(pos):
            x=0
            while pos>=0:
                x+=cnt[pos]
                pos=(pos&(pos+1))-1
            return x
        def get_cnt(lst1,lst2):
            idx=[0]*len(lst1)
            for i in range(len(lst1)):
                idx[lst1[i]]=i
            ret=[0]*len(lst2)
            for i in range(1,len(lst2)-1):
                left=lst2[i-1]
                cur=lst2[i]
                left_idx=idx[left]
                cur_idx=idx[cur]
                update(left_idx,1)
                ret[i]=get(cur_idx)
            return ret
        left_lst=get_cnt(nums1,nums2)
        for i in range(len(nums1)):
            cnt[i]=0
        right_lst=get_cnt(nums1[::-1],nums2[::-1])[::-1]
        acc=0
        for i in range(1,len(nums2)-1):
            acc+=left_lst[i]*right_lst[i]
        return acc