<h1>Ion flux relabeling</h1>
<p>Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion! Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like following:</p>
<pre><code>      7
    /   \
  3      6
 /  \   / \
1   2  4   5
</code></pre>
<p>Write a function <code>answer(h, q)</code> - where <code>h</code> is the height of the perfect tree of converters and <code>q</code> is a list of positive integers representing different flux converters - which returns a <strong>list of integers</strong> <code>p</code> where each element in <code>p</code> is the label of the converter that sits on top of the respective converter in <code>q</code>, or <code>-1</code> if there is no such converter. For example, <code>answer(3, [1, 4, 7])</code> would return the converters above the converters at <strong>indexes 1, 4, and 7</strong> in a perfect binary tree of height 3, which is <code>[3, 6, -1]</code>.</p>
<p>The domain of the integer <code>h</code> is <code>1 &lt;= h &lt;= 30</code>, where <code>h = 1</code> represents a perfect binary tree containing only the root, <code>h = 2</code> represents a perfect binary tree with the root and two leaf nodes, <code>h = 3</code> represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists <code>q</code> and <code>p</code> contain at least one but no more than 10000 distinct integers, all of which will be between <code>1 and 2^h-1</code>, inclusive.</p>
<h1>Test cases</h1>
<p>Inputs:</p>
<pre><code>(int) h = 3
(int list) q = [7, 3, 5, 1]
</code></pre>
<p>Output:</p>
<pre><code>(int list) [-1, 7, 6, 3]
</code></pre>
<p>Inputs:</p>
<pre><code>(int) h = 5

(int list) q = [19, 14, 28]
</code></pre>
<p>Output:</p>
<pre><code>(int list) [21, 15, 29]
</code></pre>
