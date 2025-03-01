from collections import deque
import heapq

class Solution:

    # Time: O(N)
    # Space: O(1) as the input contains only A-Z.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get the frequency of each task
        count = Counter(tasks)
        # At any point, we should pick the task that has max frequency in order to minimize the total cycle time
        # Python supports only min heap, so we negate the counts to get the max count first
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # Pairs of [-cnt, time when this task will be available again]
        queue = deque() 
        time = 0

        # Continue till we have tasks left in heap or queue
        while maxHeap or queue:
            # Process current task and increment time
            time += 1
            if maxHeap:
                # As the counts are negative, we add 1 eg. if task frequency is -3, one unit is processed so only 2 are left. As we store -3 instead of 3, we add 1 instead of subtracting to reach -2 which actually means 2 units are left now.
                cnt = 1 + heapq.heappop(maxHeap)
                # If the count is non-zero i.e. this task still needs to processed once the cooldown time is over, add it to the queue.
                if cnt:
                    # IMP step: Add the remaining units of this task in the queue along with the time when this can be processed next i.e. if current time is t, then this task cannot be processed again until t + n.
                    queue.append([cnt, time + n])
            # If that current time there is any task which becomes available again after the cooldown, add it back to the heap.
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
              
        # Total time taken to do all the above steps
        return time   
