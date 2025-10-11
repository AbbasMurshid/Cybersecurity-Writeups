# Fermat’s factorization method

**Fermat’s factorization method**, which is used when two prime factors of $n$ (say $p$ and $q$) are **close to each other**.

---

### Step 1: Write $n$ in difference of squares form

We know:

$n=p⋅q$

Fermat’s idea is: any odd integer $n$ can be written as a **difference of two squares**:

$n=a^2−b^2$

---

### Step 2: Expand the difference of squares

$n=a^2−b^2=(a+b)(a−b)$

Compare this with $n=p⋅q$.

$p=a+b,q=a−b$

(or vice versa, doesn’t matter).

---

### Step 3: Why this works for *close primes*

Suppose $p$ and $q$ are close.

That means:

$p≈q$

So $a = \frac{p+q}{2}$ is **almost $\sqrt{n}$**.

And $b = \frac{p-q}{2}$ is small.

So instead of searching all possible factors of $n$, we just search values of $a$ starting from $⌈n⌉\sqrt{n}$ , and check if $a^2 - n$ is a perfect square.

---

### Step 4: The algorithm (simple version)

1. Compute a=$\sqrt{n}$ 
2. Compute $b^2 = a^2 - n$
3. If b2b^2b2 is a perfect square, stop. Factors are:
    
    $p=a+b,q=a−b$
    
4. If not, increase $a$ by 1 and repeat.

---

### Step 5: Why this breaks bad RSA

RSA chooses two large primes $p,q$.

If those primes are chosen **too close together**, then Fermat’s method finds them quickly:

- Because you don’t need to try many $a$’s beyond $\sqrt{n}$.
- In worst case, if $p$ and $q$ differ by only a few thousand (tiny compared to $n$), Fermat finds them *fast*.

That’s why a **bad RSA implementation** (choosing primes too close) is weak against Fermat’s factorization.