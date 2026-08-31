# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = head
        curr_node = head.next
        
        index = 2
        
        first = -1
        prev_critical = -1
        
        min_dist = float('inf')
        
        while curr_node.next:
            
            # Check if current node is a critical point
            is_max = (
                curr_node.val > prev_node.val and
                curr_node.val > curr_node.next.val
            )
            
            is_min = (
                curr_node.val < prev_node.val and
                curr_node.val < curr_node.next.val
            )
            
            if is_max or is_min:
                
                # First critical point
                if first == -1:
                    first = index
                
                # We already have a previous critical point
                else:
                    distance = index - prev_critical
                    min_dist = min(min_dist, distance)
                
                prev_critical = index
            
            prev_node = curr_node
            curr_node = curr_node.next
            index += 1
        
        # Fewer than 2 critical points
        if first == -1 or first == prev_critical:
            return [-1, -1]
        
        max_dist = prev_critical - first
        
        return [min_dist, max_dist]
        