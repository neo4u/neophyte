using System;
using System.Collections.Generic;
using System.Linq;

public class MinStack
{
    private Stack<int> stack;
    private Stack<int> minStack;

    /** initialize your data structure here. */
    public MinStack()
    {
        stack = new Stack<int>();
        minStack = new Stack<int>();
    }

    public void Push(int x)
    {
        int currentMin = minStack.Any() ? minStack.Peek() : int.MaxValue;

        stack.Push(x);
        minStack.Push(Math.Min(currentMin, x));
    }

    public void Pop()
    {
        minStack.Pop();
        stack.Pop();
    }

    public int Top()
    {
        return stack.Peek();
    }

    public int GetMin()
    {
        return minStack.Peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
