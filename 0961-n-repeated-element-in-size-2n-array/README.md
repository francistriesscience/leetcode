# 961. N-Repeated Element in Size 2N Array

[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/problems/n-repeated-element-in-size-2n-array)

Imagine you have a big bag of candies.

- **Half** of the candies are **Red** (your favorite!).
- The **other half** are all different colors: one Blue, one Green, one Yellow, one Purple... each color appears only **once**.

Your job is to find out which color is the "special" one that appears many times.

**How do we do it?**

We start pulling candies out of the bag one by one.

1.  Pull out the first candy. It's **Red**. Okay, put it on the table.
2.  Pull out the second candy. It's **Blue**. Have we seen Blue before? No. Put it on the table.
3.  Pull out the third candy. It's **Red** again!
    **WAIT!** We have seen Red before!

Since all the other colors (Blue, Green, Yellow) are definitely unique (only one of each), the **only** color that can ever appear twice is the **Red** one.

So, as soon as we see a candy we've seen before, we yell: **"It's Red!"** and we are done.
