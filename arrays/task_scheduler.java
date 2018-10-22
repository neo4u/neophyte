// The idea used here is similar to - https://leetcode.com/problems/rearrange-string-k-distance-apart
// We need to arrange the characters in string such that each same character is K distance apart, where distance in this problems is time b/w two similar task execution.

// Idea is to add them to a priority Q and sort based on the highest frequency.
// And pick the task in each round of ‘n’ with highest frequency. As you pick the task, decrease the frequency, and put them back after the round.

public int leastInterval(char[] tasks, int n) {
	Map<Character, Integer> map = new HashMap<>();

	for (int i = 0; i < tasks.length; i++) {
		map.put(tasks[i], map.getOrDefault(tasks[i], 0) + 1); // map key is TaskName, and value is number of times to be executed.
	}

	PriorityQueue<Map.Entry<Character, Integer>> q = new PriorityQueue<>( //frequency sort
			(a,b) -> a.getValue() != b.getValue() ? b.getValue() - a.getValue() : a.getKey() - b.getKey());

	q.addAll(map.entrySet());

	int count = 0;

	while (!q.isEmpty()) {
		int k = n + 1;
		List<Map.Entry> tempList = new ArrayList<>();

		while (k > 0 && !q.isEmpty()) {
			Map.Entry<Character, Integer> top = q.poll(); // most frequency task
			top.setValue(top.getValue() - 1); // decrease frequency, meaning it got executed
			tempList.add(top); // collect task to add back to queue
			k--;
			count++; //successfully executed task
		}

		for (Map.Entry<Character, Integer> e : tempList) {
			if (e.getValue() > 0) q.add(e); // add valid tasks 
		}

		if (q.isEmpty()) break;
		count = count + k; // if k > 0, then it means we need to be idle
	}

	return count;
}