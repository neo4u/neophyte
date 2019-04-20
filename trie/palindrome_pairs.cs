using System;
using System.Collections.Generic;

public class Solution
{
    public IList<IList<int>> PalindromePairs(string[] words)
    {
        TrieNode root = new TrieNode();

        var result = new List<IList<int>>();

        for (int i = 0; i < words.Length; i++)
        {
            AddWord(words[i], i, root);
        }

        for (int i = 0; i < words.Length; i++)
        {
            Search(words[i], i, root, result);
        }

        return result;
    }

    /** Adds a word into the data structure. */
    private void AddWord(string word, int wordIndex, TrieNode root)
    {
        TrieNode current = root;

        for (int i = word.Length - 1; i >= 0; i--)
        {
            int index = word[i] - 'a';
            if (current.Children[index] == null)
            {
                current.Children[index] = new TrieNode();
            }

            bool isPrefixPalindrome = IsPalindrome(word, 0, i);
            if (isPrefixPalindrome)
            {
                current.WordIndices.Add(wordIndex);
            }

            current = current.Children[index];
        }

        // When you reach the first char in the word, it's prefix is an empty string and so we add word index to the the list
        current.WordIndices.Add(wordIndex);
        current.WordIndexThatEndsHere = wordIndex;
    }


    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    private void Search(string word, int wordIndex, TrieNode root, List<IList<int>> result)
    {
        TrieNode current = root;

        for (int i = 0; i < word.Length; i++)
        {
            // Check if another word ended here and matched reverse of current word so far
            if (current.WordIndexThatEndsHere >= 0 && current.WordIndexThatEndsHere != wordIndex)
            {
                bool isSuffixPalindrome = IsPalindrome(word, i, word.Length - 1);
                if (isSuffixPalindrome)
                {
                    result.Add(new List<int>() { wordIndex, current.WordIndexThatEndsHere });
                }
            }

            int index = word[i] - 'a';
            if (current.Children[index] == null)
            {
                return;
            }

            current = current.Children[index];
        }

        foreach (int wi in current.WordIndices)
        {
            if (wi == wordIndex) continue;
            result.Add(new List<int>() { wordIndex, wi });
        }
    }

    private bool IsPalindrome(string word, int start, int end)
    {
        while (start < end)
        {
            if (word[start] != word[end]) return false;

            start++;
            end--;
        }

        return true;
    }

    private class TrieNode
    {
        public TrieNode[] Children { get; }

        public int WordIndexThatEndsHere { get; set; }

        public List<int> WordIndices { get; }

        public TrieNode()
        {
            WordIndexThatEndsHere = -1;
            Children = new TrieNode[26];
            WordIndices = new List<int>();
        }
    }
}