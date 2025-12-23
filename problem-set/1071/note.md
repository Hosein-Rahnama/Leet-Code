# Note

- Suppose $a$ and $b$ are two positive integers with $a > b$. The key recursive relation for understanding the Eculid's algorithm is $\mathrm{gcd}(a, b) = \mathrm{gcd}(b, a \,\,\mathrm{mod}\,\, b)$.

- If two strings $s_1$ and $s_2$ have a Greatest Common Divisor (GCD) like $t$, then $\mathrm{len}(t) = \mathrm{gcd}(\mathrm{len}(s_1), \mathrm{len}(s_2))$.

- An interesting fact is that two strings $s_1$ and $s_2$ have a common divisor if and only if $s_1 s_2 = s_2 s_1$.
