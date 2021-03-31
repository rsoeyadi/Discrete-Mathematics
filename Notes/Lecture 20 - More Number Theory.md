### Lecture 20 at 9:54am on March 31st, 2021

---

### Euclid's Observation

gcd(a, b) = gcd(b, a mod b)

Let a,b,q, r **in Z** 

a = ba + r 

where r is greater than or equal to 0 and b > 0

gcd(30, 24)

30 = 24 x 1 + 6

3 | 30 and 3 | 24

- if 3 divides 30 and 3 divides 24, 3 must also divide 6 (linear relationship)

Divisors of 30 = {1,2,3,6,10,15,30}

Divisors of 24 = {1,2,3,4,6,12,24}

Divisors of 6 = {1,2,3,6}

---

Divisors of 30 **INTERSECT** Divisors of 24 = Divisors of 24 **INTERSECT** Divisors of 6

---

Proof:

gcd(a,b) = gcd(b,r)

a = bq + r 

Let c be a divisor of **a** and **b**

a = cq_1

b = cq_2

![1](./Lect20-img/1.png)

![1](./Lect20-img/2.png)

### Def (Coprime or Relatively Prime):

![1](./Lect20-img/3.png)

### Theorem

There is an infiniity of prime numbers

### Lemma

![1](./Lect20-img/4.png)

![1](./Lect20-img/5.png)

---

## Proof for Kummer 1878

There is an infinity of prime numbers

**By contradiction, suppose there is a largest number (a finite number of primes).**

P_1, P_2, ..., P_r

![1](./Lect20-img/6.png)

Let X = P_1 x P_2 x P_r, a composite... because **P_r is the largest prime**

x + 1 is also composite

Then **x and x + 1 must share at least one prime p_1, p_2, ..., p_r**

Let's call it **p_i**

![1](./Lect20-img/7.png)

![1](./Lect20-img/8.png)

---

![1](./Lect20-img/9.png)

![1](./Lect20-img/10.png)

---

### Proof of FTA involves the following:

![1](./Lect20-img/11.png)

![1](./Lect20-img/12.png)

---

### Factoring (GCD Formula):

GCD(30, 24)

(30, 24, 6, 0)

![1](./Lect20-img/13.png)

![1](./Lect20-img/14.png)

You take the highest shared power of each number

![1](./Lect20-img/15.png)

![1](./Lect20-img/16.png)

---

### Sieve of Eratosthemes

Example:

<u>N = 41</u>

![1](./Lect20-img/17.png)

Check any number between 1 and the **FLOOR(Sqr(n))**

---

Proposition:

To find all prime numbers between 2 and **N**, using the ***Sieve of Eratosthemes***, it is enough to cross all the multiples of all prime numbers until:

![1](./Lect20-img/18.png)

**Steps:**

![1](./Lect20-img/19.png)

---

### Modulo Arithmetic (clock arithmetic):

![1](./Lect20-img/20.png)

![1](./Lect20-img/21.png)

![1](./Lect20-img/22.png)

---

The clock example (11am + 5 hours) can be represented this way:

![1](./Lect20-img/23.png)

![1](./Lect20-img/24.png)