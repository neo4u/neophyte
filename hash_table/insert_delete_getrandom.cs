// 380. Insert Delete GetRandom O(1)
public class RandomizedSet
{
    List<int> list;
    Dictionary<int, int> map;
    Random random;

    /** Initialize your data structure here. */
    public RandomizedSet()
    {
        list = new List<int>();
        map = new Dictionary<int, int>();
        random = new Random();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public bool Insert(int val)
    {
        if (map.ContainsKey(val)) return false;

        map.Add(val, list.Count);
        list.Add(val);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public bool Remove(int val)
    {
        if (!map.ContainsKey(val)) return false;

        int indexToDelete = map[val];
        
        if (indexToDelete != list.Count - 1)
        {
            int lastItem = list[list.Count - 1];
            list[indexToDelete] = lastItem;
            map[lastItem] = indexToDelete;
        }

        map.Remove(val);
        list.RemoveAt(list.Count - 1);
        return true;
    }

    /** Get a random element from the set. */
    public int GetRandom()
    {
        int index = random.Next(0, list.Count);
        return list[index];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
