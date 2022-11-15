/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int n=lists.length;
        if(lists==null||n==0)
            return null;
        return merge(lists,0,n-1);
    }
    public ListNode merge(ListNode[] lists,int l, int h){
        if(l==h)
            return lists[l];
        int mid=l+(h-l)/2;
        ListNode l1=merge(lists,l,mid);
        ListNode l2=merge(lists,mid+1,h);
        return mergeTwoLists(l1,l2);
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null)
             return l2;
        if(l2==null)
            return l1;
        if(l1==null && l2==null)
            return null;
        ListNode res=new ListNode(0);
        ListNode r=res;
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                res.next=l1;
                l1=l1.next;
            }
            else{
                res.next=l2;
                l2=l2.next;
            }
            res=res.next;
        }
        if(l1==null){
            res.next=l2;
        }
        else{
            res.next=l1;
        }
        return r.next;
    }
}