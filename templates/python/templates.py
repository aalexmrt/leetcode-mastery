"""
LeetCode Common Templates - Python
====================================
Reusable code patterns for common problem types.
"""

# =============================================================================
# ARRAYS & HASHING
# =============================================================================

def two_sum_template(nums, target):
    """Find two numbers that add up to target. Returns indices."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def frequency_count_template(nums):
    """Count frequency of each element."""
    from collections import Counter
    return Counter(nums)
    # Manual: freq = {}; for n in nums: freq[n] = freq.get(n, 0) + 1


def group_by_key_template(items, key_func):
    """Group items by a computed key."""
    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)
    return dict(groups)


# =============================================================================
# TWO POINTERS
# =============================================================================

def two_pointer_converging_template(nums):
    """Two pointers moving toward each other."""
    left, right = 0, len(nums) - 1
    
    while left < right:
        # Process current pair
        current = nums[left] + nums[right]
        
        if condition_met(current):
            # Found answer or update result
            pass
        elif need_larger(current):
            left += 1
        else:
            right -= 1
    
    return result


def two_pointer_same_direction_template(nums):
    """Fast/slow pointers for in-place modification."""
    slow = 0
    for fast in range(len(nums)):
        if should_keep(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1
    return slow  # New length


# =============================================================================
# SLIDING WINDOW
# =============================================================================

def sliding_window_variable_template(s):
    """Variable size sliding window."""
    left = 0
    result = 0
    window = {}  # or other state
    
    for right in range(len(s)):
        # Expand: add s[right]
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Contract: while invalid
        while window_invalid(window):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result


def sliding_window_fixed_template(nums, k):
    """Fixed size sliding window."""
    window_sum = sum(nums[:k])
    result = window_sum
    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result = max(result, window_sum)
    
    return result


# =============================================================================
# BINARY SEARCH
# =============================================================================

def binary_search_template(nums, target):
    """Standard binary search."""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_leftmost_template(nums, target):
    """Find leftmost position where target could be inserted."""
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_on_answer_template(low, high, is_valid):
    """Binary search on answer space (e.g., Koko eating bananas)."""
    while low < high:
        mid = low + (high - low) // 2
        
        if is_valid(mid):
            high = mid  # Can do it with mid, try smaller
        else:
            low = mid + 1  # Can't do it, need larger
    
    return low


# =============================================================================
# LINKED LIST
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list_template(head):
    """Reverse a linked list iteratively."""
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev


def fast_slow_pointer_template(head):
    """Detect cycle or find middle."""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Cycle detected
            return True
    
    return slow  # Middle node (no cycle)


def dummy_node_template(head):
    """Use dummy node for easier edge case handling."""
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    # Process list...
    
    return dummy.next


# =============================================================================
# TREES
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_recursive_template(root):
    """DFS traversal (preorder example)."""
    result = []
    
    def dfs(node):
        if not node:
            return
        
        result.append(node.val)  # Preorder: process before children
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result


def dfs_iterative_template(root):
    """DFS using stack."""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


def bfs_level_order_template(root):
    """BFS level order traversal."""
    from collections import deque
    
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def tree_max_depth_template(root):
    """Calculate max depth recursively."""
    if not root:
        return 0
    
    return 1 + max(
        tree_max_depth_template(root.left),
        tree_max_depth_template(root.right)
    )


# =============================================================================
# GRAPHS
# =============================================================================

def graph_bfs_template(graph, start):
    """BFS traversal from a starting node."""
    from collections import deque
    
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited


def graph_dfs_template(graph, start):
    """DFS traversal from a starting node."""
    visited = set()
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start)
    return visited


def number_of_islands_template(grid):
    """Count connected components in a grid."""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        
        grid[r][c] = '0'  # Mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    
    return count


# =============================================================================
# DYNAMIC PROGRAMMING
# =============================================================================

def dp_1d_template(n):
    """1D DP (e.g., Fibonacci, climbing stairs)."""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def dp_1d_space_optimized(n):
    """Space-optimized 1D DP."""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1


def dp_2d_template(m, n):
    """2D DP (e.g., unique paths)."""
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


def dp_knapsack_template(weights, values, capacity):
    """0/1 Knapsack."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Take
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


# =============================================================================
# BACKTRACKING
# =============================================================================

def backtrack_subsets_template(nums):
    """Generate all subsets."""
    result = []
    
    def backtrack(start, path):
        result.append(path[:])  # Add current subset
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result


def backtrack_permutations_template(nums):
    """Generate all permutations."""
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result


def backtrack_combination_sum_template(candidates, target):
    """Find combinations that sum to target (can reuse elements)."""
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse)
            path.pop()
    
    backtrack(0, [], target)
    return result


# =============================================================================
# HEAP / PRIORITY QUEUE
# =============================================================================

def top_k_elements_template(nums, k):
    """Find top k largest elements."""
    import heapq
    return heapq.nlargest(k, nums)
    
    # Or using min heap of size k:
    # heap = []
    # for num in nums:
    #     heapq.heappush(heap, num)
    #     if len(heap) > k:
    #         heapq.heappop(heap)
    # return heap


def merge_k_sorted_lists_template(lists):
    """Merge k sorted lists using heap."""
    import heapq
    
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)
    
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result


# =============================================================================
# INTERVALS
# =============================================================================

def merge_intervals_template(intervals):
    """Merge overlapping intervals."""
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= result[-1][1]:  # Overlapping
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    
    return result


def interval_intersection_template(list1, list2):
    """Find intersection of two interval lists."""
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        start = max(list1[i][0], list2[j][0])
        end = min(list1[i][1], list2[j][1])
        
        if start <= end:
            result.append([start, end])
        
        # Move pointer with earlier end
        if list1[i][1] < list2[j][1]:
            i += 1
        else:
            j += 1
    
    return result
