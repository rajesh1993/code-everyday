'''
Problem 911.

In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
'''


class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # Map time to topvotedCandidate
        self.timeSlots = dict()
        self.time_length = len(times)
        self.times = times
        # Map candidate to votes
        votes = collections.Counter()
        topPerson = persons[0]
        for idx, time in enumerate(times):
            votes[persons[idx]] += 1
            if votes[persons[idx]] >= votes[topPerson]:
                self.timeSlots[time] = persons[idx]
                topPerson = persons[idx]
            else:
                self.timeSlots[time] = topPerson
            

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # find the closest number in times less than the given t (logn search)
        high = self.time_length - 1
        low = 0
        if t >= self.times[high]:
            return self.timeSlots[self.times[high]]
        while low < high:
            mid = int((low + high) / 2)
            if t == self.times[mid]:
                return self.timeSlots[self.times[mid]]
            elif high - low == 1:
                return self.timeSlots[self.times[low]]
            elif t > self.times[mid]:
                low = mid
            else:
                high = mid
        # Return topvotedCandidate from map


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)