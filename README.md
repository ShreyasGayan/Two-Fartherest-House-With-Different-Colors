2078. Two Furthest Houses With Different Colors
Problem Statement

There are n houses lined up on a street, where colors[i] represents the color of the i-th house.

Your task is to find the maximum distance between two houses that have different colors.

The distance between house i and house j is:

abs(i - j)

Return the maximum possible distance.

Examples
Example 1
Input: colors = [1,1,1,6,1,1,1]
Output: 3

Explanation:

House 0 has color 1
House 3 has color 6

Distance:

|0 - 3| = 3

This is the maximum possible distance between two houses of different colors.

Example 2
Input: colors = [1,8,3,8,3]
Output: 4

Explanation:

House 0 has color 1
House 4 has color 3

Distance:

|0 - 4| = 4
Approach
Key Observation

The furthest valid pair must include either:

The first house, or
The last house

Why?

If two houses have different colors and produce the maximum distance, moving one endpoint closer to the edge can only increase or maintain the distance.

Therefore:

Find the furthest house from the left whose color differs from the first house.
Find the furthest house from the right whose color differs from the last house.
The maximum of these two distances is the answer.

Complexity Analysis
Complexity	Value
Time	O(n)
Space	O(n)
Time Complexity

The array is traversed twice.

O(n) + O(n) = O(n)
Space Complexity

Only a few variables are used regardless of input size.

O(1)
