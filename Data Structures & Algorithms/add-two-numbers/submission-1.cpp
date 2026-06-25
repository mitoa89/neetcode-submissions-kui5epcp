/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* c1 = l1;
        ListNode* c2 = l2;
        
        auto dummy = new ListNode();
        ListNode* curr = dummy;
        int carry = 0;
        while(c1 != nullptr  || c2 != nullptr || carry != 0){
            int v1 = c1 == nullptr ? 0 : c1->val;
            int v2 = c2 == nullptr ? 0 : c2->val;
            
            int sum = v1 + v2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            curr->next = new ListNode(sum);

            
            c1 = c1 == nullptr ? nullptr : c1->next;
            c2 = c2 == nullptr ? nullptr : c2->next;
            curr = curr->next;
        }

        auto ans = dummy->next;
        delete dummy;
        return ans;
    }
};
