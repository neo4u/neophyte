Status: Software Engineer, 5 Years Experience
Position: Software Engineer, Security
Location: Mountain View, CA
Date: June, 2019

Direct onsite due to interviewing before with Google.


### ***Round 1: Coding***
We're given a list of intervals and the corresponding speed for that interval. This list represents ranges within an infinite road and the speed of vehicles in those ranges. We are supposed to return the final list of smallest ranges and the average speed of vehicles in each of those ranges.

Used for road color coding as per traffic prediction used in google maps or lately uber.

```python
input = [(5, 15, 20), (10, 20, 30)]
output = [(5, 10, 20), (10, 15, (20 + 30)//2), (15, 20, 30)]
output = [(5, 10, 20), (10, 15, 25), (15, 20, 30)]

input = [(5, 15, 20), (10, 20, 30), (7, 25, 10)]
output = [(5, 10, 20), (10, 15, 25), (15, 20, 30)] merged with (7, 25, 10)
output = [(5, 7, 20), (7, 10, (20 + 10)//2), (10, 15, (25 + 10)//2), (15, 20, (30 + 10)//2), (20, 25, 10)
output = [(5, 7, 20), (7, 10, 15), (10, 15, 17.5), (15, 20, 20), (20, 25, 10)
maybe a little wrong on the speeds but you get the idea. It should be the average speed for that interval.
```

<details>
    <summary>Solved using the below solution!</summary>


```python
class Node:
    def __init__(self, s, e, sp):
        self.s, self.e, self.sp = s, e, sp
        self.left, self.right = None, None

class Events:
    def __init__(self):
        self.root = None

    def insert(self, s, e, sp):
        if not self.root:
            root = Node(s, e, sp)
            return

        self._insert(s, e, sp, root)

    def _insert(self, s, e, sp, i_root):
        if s == e: return

        if e <= i_root.s:
            self._insert(s, e, sp, i_root.left)
        elif s >= i_root.e:
            self._insert(s, e, sp, i_root.right)
        else:
            a = min(i_root.s, s)
            b = max(i_root.s, s)
            c = min(i_root.e, e)
            d = max(i_root.e, e)

            if i_root.s != s and i_root.s == b:
                left_sp = sp
            else:
                left_sp = i_root.sp

            if i_root.e != e and i_root.e == c:
                right_sp = sp
            else:
                right_sp = i_root.sp

            self._insert(a, b, left_sp, i_root.left)
            self._insert(c, d, right_sp, i_root.right)
            i_root.sp = (i_root.sp + sp) / 2

return in order traversal
```

</details>


#### Points to ponder:
- I used a solution similar to My Calendar II, III. https://leetcode.com/problems/my-calendar-ii/
- Here, where we'll have unlimited bookings.
- I use an approximate average. However, it is better to keep a total of how many interval merged into a node (number of bookings for that interval) and the total speed for that interval

Didn't have time to complete. Didn't see any exact match on LC before.


### ***Round 2: More Coding***
Interviewer gave me a story regarding how I wanted to cut a chocolate by sweetness such a way that the sweetest piece was least sweet so that the one who gets the least sweet piece get the maximum sweetness and some nonsense. I was thoroughly confused and didn't solve it.

The main problem was: 
Split array into `m` sub-arrays that the max piece is minimized. Important bit was that the problem was [this one](https://leetcode.com/problems/split-array-largest-sum/description/), the story was pretty stupid. Wth do you mean by chocolate with variable sweetness. :( 
https://leetcode.com/problems/split-array-largest-sum/description/

#### Points to ponder
Its supposed to be solved using:
- DP (Very weird solution)
- Binary Search with some analysis of the mid at every stage of the search (Easier to understand but quite intricate in terms of how to evaluate if a mid is a valid mid to consider towards the solution)


### ***Round 3: More Coding Wowie***
The problem was to implement a monarchy. Where we're to implement a class that has the general idea like so:

```python
class Monarchy:
    def __init__(self):
        pass

    def birth(self, name, parent):
        pass

    def death(self, name):
        pass

    def get_order_of_succession(self):
        pass
```

<details>
    <summary>Solved using the below solution!</summary>


```python
# I used an nary-tree and did this like so:
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

class Monarchy:
    def __init__(self, king_name):
        self.root = king_name
        self.names_map = {king_name: Node(king_name)}

    def birth(self, name, parent):
        node = self.names_map[parent]
        child = Node(name)
        node.children.append(child)
        self.names_map[name] = node

    def death(self, name):
        node = self.names_map[name]
        if node == self.root:
            first_c = self.root.children.pop(0)
            self.root = first_c
            first_c.children.extend(self.root.children)

        for n in self.root.children:
            if self._delete(node, n, self.root):
                break

    def _delete(self, delete_node, node, parent):
        if node == delete_node:
            i = parent.children.index(node)
            for c in node.children:
                parent.children.insert(i, c)
                i += 1
            return True

        for c in node.children:
            if self._delete(delete_node, c, node):
                return True

        return False

    def get_order_of_succession(self):
        self._dfs(self.root)

    def _dfs(self, node):
        print(node.name)
        for c in node.children:
            self._dfs(c)
```
</details>


#### Points to ponder
Never saw such a problem on LC before. Anyone know any similar problems?

I didn't get to complete the code in the interview as it took forever to clarify and understand how the interviewer expected the death of a person to be handled. It was a little non-intuitive.  A point to note is that a if a person dies high children, grandchildren and so on take his place in line of succession.

### ***Lunch: Fajitas! Yes, Please.***

Interviewer was very curious about my work and interests and I was constantly engaged during the whole lunch.


### ***Round 4: Behavior***

Tell me a time when you were:
- good guy
- bad guy
- conflict guy
- yada, yada
- the ush



### ***Round 5: Security Domain***

Attack Google users, go ahead do your worst, you have unlimited budget! :)

I answered with lots of good stuff namely:
phising using fake login pages, password stealing, brute-force, ARP spoofing, DNS rebinding, HSTS downgrade, near domain name hijacking, IP spoofing, Fake OAuth and password stealing.


Need your collective knowledge to figure out what I did wrong during the interview. It was as good as I could do. :( It still wasn't enough. The chocolate problem was patirularly brutal! :( :(


***Interview Level***: Hard
***Overall Experience***: Very Positive with some bitterness :(
