
// Definition for a Node.
/* using System.Collections.Generic;

public class Node
{
    public int val;
    public Node next;
    public Node random;

    public Node() { }
    public Node(int _val, Node _next, Node _random)
    {
        val = _val;
        next = _next;
        random = _random;
    } */

public class Solution
{
    public Node CopyRandomList(Node head)
    {
        if (head == null)
        {
            return null;
        }

        var map = new Dictionary<Node, Node>(); // Original Node -> Cloned Node mapping

        DeepCopy(head, map);

        return map[head];
    }

    private Node DeepCopy(Node original, Dictionary<Node, Node> map)
    {
        if (original == null)
        {
            return null;
        }

        if (map.ContainsKey(original))
        {
            return map[original];
        }

        var newNode = new Node(original.val, null, null);
        map.Add(original, newNode);

        newNode.next = DeepCopy(original.next, map);
        newNode.random = DeepCopy(original.random, map);

        return map[original];
    }
}