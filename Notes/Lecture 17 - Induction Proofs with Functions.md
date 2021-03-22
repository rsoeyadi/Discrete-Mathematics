### Lecture 17 at 10:07am on March 22nd, 2021

---

### Proof by Mathematical Induction

*Proof Template*

<img src="./Lect17-img/1.png" alt="1" style="zoom:90%;" />

<img src="./Lect17-img/2.png" alt="1" style="zoom:90%;" />

---

### Def (Well-ordering Principle)

Every set of non-negative integers has a least element 

Take any subset--you will have a starting point

```
Well-ordering Principle is a property of non-negative integers
It states that there is a starting point: the least element
```



<img src="./Lect17-img/3.png" alt="1" style="zoom:90%;" />

---

### Example

**1575 - Francesco Maurolico**

```
The sum of the first n odd positive integers is a perfect square.
1 = 1^2
1 + 3 = 2^2
1 + 3 + 5 = 3^2
1 + 3 + 5 + 7 = 4^2
1 + 3 + 5 + ... + 2(n-1) = n^2
```

Visually, this looks like this (where you continue surrounding with the next odd integer)

<img src="./Lect17-img/4.png" alt="1" style="zoom:90%;" />

---

Try proving it through induction; the template will look like this

<img src="./Lect17-img/5.png" alt="1" style="zoom:90%;" />

---

### Another example

<img src="./Lect17-img/6.png" alt="1" style="zoom:90%;" />

<img src="./Lect17-img/7.png" alt="1" style="zoom:90%;" />

---

### Proof by Smallest Counter Example (equivalent to induction)

*hybrid of induction and proof by contradiction*

**Induction** is base case, assume p(k), prove p(k+1) 

**Smallest Counter Example** is base case, assumed p(x) is false

<img src="./Lect17-img/8.png" alt="1" style="zoom:90%;" />

Prove the base case p(0)

By contradiction, assume there exists a smallest counter example **x** (the exception) such that

p(x) is **false**

p(x-1), (p(x-2)) ... are all true because **x** is the smallest counter example

Show that p(x) is false, p(x-1) is true

**This leads to a contradiction**

---

### Example

<img src="./Lect17-img/9.png" alt="1" style="zoom:90%;" />

