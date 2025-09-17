\section*{Lecture 14}

\section*{A Minimization Algorithm}

Here is an algorithm for computing the collapsing relation \(\approx\) for a given DFA \(M\) with no inaccessible states. Our algorithm will mark (unordered) pairs of states \(\{p, q\}\). A pair \(\{p, q\}\) will be marked as soon as a reason is discovered why \(p\) and \(q\) are not equivalent.
1. Write down a table of all pairs \(\{p, q\}\), initially unmarked.
2. Mark \(\{p, q\}\) if \(p \in F\) and \(q \notin F\) or vice versa.
3. Repeat the following until no more changes occur: if there exists an unmarked pair \(\{p, q\}\) such that \(\{\delta(p, a), \delta(q, a)\}\) is marked for some \(a \in \Sigma\), then mark \(\{p, q\}\).
4. When done, \(p \approx q\) iff \(\{p, q\}\) is not marked.

Here are some things to note about this algorithm:
- If \(\{p, q\}\) is marked in step 2 , then \(p\) and \(q\) are surely not equivalent: take \(x=\epsilon\) in the definition of \(\approx\).
- We may have to look at the same pair \(\{p, q\}\) many times in step 3, since any change in the table may suddenly allow \(\{p, q\}\) to be marked. We stop only after we make an entire pass through the table with no new marks.
- The algorithm runs for only a finite number of steps, since there are only \(\binom{n}{2}\) possible marks that can be made, \({ }^{1}\) and we have to make at least one new mark in each pass to keep going.
- Step 4 is really a statement of the theorem that the algorithm correctly computes \(\approx\). This requires proof, which we defer until later.

Example 14.1 Let's minimize the automaton of Example 13.2 of Lecture 13.
\[
\rightarrow \begin{array}{ll|ll} 
& & a & b \\
\hline & 0 & 1 & 2 \\
& 1 F & 3 & 4 \\
& 2 F & 4 & 3 \\
& 3 & 5 & 5 \\
& 4 & 5 & 5 \\
& 5 F & 5 & 5
\end{array}
\]

Here is the table built in step 1. Initially all pairs are unmarked.
0
- 1
- - 2
- - - 3
- - - - 4
- \(\quad\) - \(\quad\) - \(\quad\) - 5

After step 2, all pairs consisting of one accept state and one nonaccept state have been marked.
\[
\begin{array}{cccccc}
0 & & & & & \\
\checkmark & 1 & & & & \\
\checkmark & - & 2 & & & \\
- & \checkmark & \checkmark & 3 & & \\
- & \checkmark & \checkmark & - & 4 & \\
\checkmark & - & - & \checkmark & \checkmark & 5
\end{array}
\]

Now look at an unmarked pair, say \(\{0,3\}\). Under input \(a, 0\) and 3 go to 1 and 5 , respectively (write: \(\{0,3\} \rightarrow\{1,5\}\) ). The pair \(\{1,5\}\) is not marked, so we don't mark \(\{0,3\}\), at least not yet. Under input \(b,\{0,3\} \rightarrow\{2,5\}\), which is not marked, so we still don't mark \(\{0,3\}\). We then look at unmarked pairs \(\{0,4\}\) and \(\{1,2\}\) and find out we cannot mark them yet for the same reasons. But for \(\{1,5\}\), under input \(a,\{1,5\} \rightarrow\{3,5\}\), and \(\{3,5\}\) is marked, so we mark \(\{1,5\}\). Similarly, under input \(a,\{2,5\} \rightarrow\{4,5\}\) which is marked, so we mark \(\{2,5\}\). Under both inputs \(a\) and \(b,\{3,4\} \rightarrow\{5,5\}\), which is never marked (it's not even in the table), so we do not mark \(\{3,4\}\). After the first

\footnotetext{
\({ }^{1}\binom{n}{k} \stackrel{\text { def }}{=} \frac{n!}{k!(n-k)!}\), the number of subsets of size \(k\) in a set of size \(n\).
}
pass of step 3, the table looks like

\begin{tabular}{cccccc}
0 & & & & & \\
\(\checkmark\) & 1 & & & & \\
\(\checkmark\) & - & 2 & & & \\
- & \(\checkmark\) & \(\checkmark\) & 3 & & \\
- & \(\checkmark\) & \(\checkmark\) & - & 4 & \\
\(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & 5
\end{tabular}

Now we make another pass through the table. As before, \(\{0,3\} \rightarrow\{1,5\}\) under input \(a\), but this time \(\{1,5\}\) is marked, so we mark \(\{0,3\}\). Similarly, \(\{0,4\} \rightarrow\{2,5\}\) under input \(b\), and \(\{2,5\}\) is marked, so we mark \(\{0,4\}\). This gives

\begin{tabular}{cccccc}
0 & & & & & \\
\(\checkmark\) & 1 & & & & \\
\(\checkmark\) & - & 2 & & & \\
\(\checkmark\) & \(\checkmark\) & \(\checkmark\) & 3 & & \\
\(\checkmark\) & \(\checkmark\) & \(\checkmark\) & - & 4 & \\
\(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & \(\checkmark\) & 5
\end{tabular}

Now we check the remaining unmarked pairs and find out that \(\{1,2\} \rightarrow \{3,4\}\) and \(\{3,4\} \rightarrow\{5,5\}\) under both \(a\) and \(b\), and neither \(\{3,4\}\) nor \(\{5,5\}\) is marked, so there are no new marks. We are left with unmarked pairs \(\{1,2\}\) and \(\{3,4\}\), indicating that \(1 \approx 2\) and \(3 \approx 4\).

Example 14.2 Now let's do Example 13.4 of Lecture 13.
\[
\begin{array}{ll|l} 
& & a \\
\cline { 2 - 3 } & 0 & 1 \\
& 1 F & 2 \\
& 2 & 3 \\
& 3 & 4 \\
& 4 F & 5 \\
& 5 & 0
\end{array}
\]

Here is the table after step 2.
\[
\begin{array}{llllll}
0 & & & & & \\
\checkmark & 1 & & & & \\
- & \checkmark & 2 & & & \\
- & \checkmark & - & 3 & & \\
\checkmark & - & \checkmark & \checkmark & 4 & \\
- & \checkmark & - & - & \checkmark & 5
\end{array}
\]

Then:
- \(\{0,2\} \rightarrow\{1,3\}\), which is marked, so mark \(\{0,2\}\).
- \(\{0,3\} \rightarrow\{1,4\}\), which is not marked, so do not mark \(\{0,3\}\).
- \(\{0,5\} \rightarrow\{0,1\}\), which is marked, so mark \(\{0,5\}\).
- \(\{1,4\} \rightarrow\{2,5\}\), which is not marked, so do not mark \(\{1,4\}\).
- \(\{2,3\} \rightarrow\{3,4\}\), which is marked, so mark \(\{2,3\}\).
- \(\{2,5\} \rightarrow\{0,3\}\), which is not marked, so do not mark \(\{2,5\}\).
- \(\{3,5\} \rightarrow\{0,4\}\), which is marked, so mark \(\{3,5\}\).

After the first pass, the table looks like this:
```
0
\checkmark 1
\checkmark \checkmark 2
- \checkmark \checkmark 3
\checkmark - \checkmark \checkmark 4
\checkmark \checkmark - \checkmark \checkmark 5
```


Now do another pass. We discover that \(\{0,3\} \rightarrow\{1,4\} \rightarrow\{2,5\} \rightarrow\{0,3\}\) and none of these are marked, so we are done. Thus \(0 \approx 3,1 \approx 4\), and \(2 \approx 5\).

\section*{Correctness of the Collapsing Algorithm}

Theorem 14.3 The pair \(\{p, q\}\) is marked by the above algorithm if and only if there exists \(x \in \Sigma^{*}\) such that \(\widehat{\delta}(p, x) \in F\) and \(\widehat{\delta}(q, x) \notin F\) or vice versa; i.e., if and only if \(p \not \approx q\).

Proof. This is easily proved by induction. We leave the proof as an exercise (Miscellaneous Exercise 49).

A nice way to look at the algorithm is as a finite automaton itself. Let
\[
\mathcal{Q}=\{\{p, q\} \mid p, q \in Q, p \neq q\} .
\]

There are \(\binom{n}{2}\) elements of \(\mathcal{Q}\), where \(n\) is the size of \(Q\). Define a nondeterministic "transition function"
\[
\Delta: \mathcal{Q} \rightarrow 2^{\mathcal{Q}}
\]
on \(\mathcal{Q}\) as follows:
\[
\Delta(\{p, q\}, a)=\left\{\left\{p^{\prime}, q^{\prime}\right\} \mid p=\delta\left(p^{\prime}, a\right), q=\delta\left(q^{\prime}, a\right)\right\} .
\]

Define a set of "start states" \(\mathcal{S} \subseteq \mathcal{Q}\) as follows:
\[
\mathcal{S}=\{\{p, q\} \mid p \in F, q \notin F\} .
\]
(We don't need to write "... or vice versa" because \(\{p, q\}\) is an unordered pair.) Step 2 of the algorithm marks the elements of \(\mathcal{S}\), and step 3 marks pairs in \(\Delta(\{p, q\}, a)\) when \(\{p, q\}\) is marked for any \(a \in \Sigma\). In these terms, Theorem 14.3 says that \(p \not \approx q\) iff \(\{p, q\}\) is accessible in this automaton.