class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> pq = new PriorityQueue();
        int ans = 0, cost = 0;
        for(int s:sticks){
            pq.add(s);
        }
        while(pq.size() > 1){
            cost = pq.poll() + pq.poll();
            ans += cost;
            pq.add(cost);
        }
        return ans;
    }
}