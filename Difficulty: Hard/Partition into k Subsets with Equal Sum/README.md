<h2><a href="https://www.geeksforgeeks.org/problems/partition-array-to-k-subsets/1">Partition into k Subsets with Equal Sum</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an integer array <strong>arr[ ]</strong>&nbsp;and an integer <strong>k</strong>, the task is to check if the array<strong> </strong>arr[ ]&nbsp;could be divided into k non-empty subsets with equal sum of elements.<br><strong>Note:</strong>&nbsp;All elements of this array should be part of exactly one partition.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [2, 1, 4, 5, 6], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> We can divide above array into 3 parts with equal sum as (2, 4), (1, 5), (6)</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [2, 1, 5, 5, 6], k = 3
<strong>Output:</strong> false
<strong>Explanation</strong>: It is not possible to divide above array into 3 parts with equal sum.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ k ≤ arr.size() ≤ 10<br>1 ≤ arr[i] ≤ 100</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Backtracking</code>&nbsp;