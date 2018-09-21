import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter()
        for task in tasks:
            task_counts.update(task)
        
        M = task_counts[task_counts.most_common(1)[0][0]]
        maxCount = sum([1 for i in task_counts if task_counts[i] == M])
        return max(len(tasks), (M-1) * (n+1) + maxCount)
            
        