Lecture 21 at 10:06am on April 5th, 2021

---

## Counting/Combinatorics

**Counting lists**: permutations, anagrams, multiplication theorem

**Counting Sets**: Combinations, binomial theorem, pascal triangle

**Counting the size of sets**: principle of inclusion exclusion (pie)

---

### Theorem (Size of Power Set)

Let **S** be a finite set of cardinality n ≥ 0

|S| = n ---> |P(S)| = 2^n

![1](./Lect21-img/1.png)

---

Ex. 

![19](./Lect21-img/2.png)

---

## Proof by Induction

Prove:

![19](./Lect21-img/3.png)

![19](./Lect21-img/4.png)

![19](./Lect21-img/5.png)

---

### Counting Lists

1. You have 2 pairs of sneakers, 3 pairs of flip flops

**How much footwear do you have?**

3 + 2 = 5 possible pairings.

This is called the **Addition Principle**

---

2. You have 5 shirts,  3 pants, and 2 pairs of shoes.

**How many different outfits can you make?**

5 * 3 * 2 = 30 possible outfits

This is called the **Multiplication Principle**

![19](./Lect21-img/6.png)

---

3. How many **odd** two-digit numbers are between 10 and 99

![19](./Lect21-img/7.png)

---

4. How many 10-digit phone numbers are there?

![19](./Lect21-img/8.png)

---

5. ![19](./Lect21-img/9.png)

   ---

6. You toss a coin 4 times.

HHHH, HHHT, ...

![19](./Lect21-img/10.png)

---

7. You have **10 members in a club**

President, Vice President, Treasurer

![19](./Lect21-img/11.png)

We can't repeat the digits in this example because we have a finite number of members

n, n-1, n-2, **n-k+1**

10, 9, 8, 10 - 3 + 1



---

### Theorem (The Multiplication Theorem):

The number of lists of size **K** whose elements can be chosen from a pool of **n** elements is:

![19](./Lect21-img/12.png)



![19](./Lect21-img/13.png)



**If repetitions are NOT allowed**:

![19](./Lect21-img/14.png)

This is **(n)_k**:

![19](./Lect21-img/15.png)

---

Ex.

```
How many 3-letter words can we make with 26 letters of the alphabet if repetitions are allowed?

What about if repetitions are not allowed?
```

1. **If repetitions are allowed**

![19](./Lect21-img/16.png)

2. **If repetitions are not allowed**

![19](./Lect21-img/17.png)

---

## Permutations

The number of arrangements of **K** distinct elements chosen from **n** distinct elements, where **repetitions are not allowed**

![19](./Lect21-img/18.png)

---

![19](./Lect21-img/19.png)

This is simply the **fallen factorial**

![19](./Lect21-img/20.png)

![19](./Lect21-img/21.png)

---

## Anagrams

Anagrams **are permutations of letters in a word with no repetitions**

Words can be non-sensical.

**Ex.**

How many anagrams can we make with the word **Math**?

```Math, Maht, ...```

![19](./Lect21-img/22.png)

![19](./Lect21-img/23.png)

---

Ex. 

![19](./Lect21-img/24.png)

![19](./Lect21-img/25.png)

---

![19](./Lect21-img/26.png)

---

## Def (Number of Anagrams):

Let an **n-letter** word with **K** unique letters, where letter **i** appears **n**_i times.

![19](./Lect21-img/27.png)

---

What if we don't care about order?

![19](./Lect21-img/28.png)

### Def (Combinations)

The set of **k-element** subsets of an **n-element** set for:

![19](./Lect21-img/29.png)

---

## Def (Binomial Coefficient):

![19](./Lect21-img/30.png)

Ex.

![19](./Lect21-img/31.png)

p(4,2) = 

![19](./Lect21-img/32.png)

![19](./Lect21-img/33.png)

![19](./Lect21-img/34.png)

![19](./Lect21-img/35.png)