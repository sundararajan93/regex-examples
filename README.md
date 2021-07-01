# All meta Characters

```
. ^ $ * + ? { } [ ] \ | ( ) 
```

```
.  Any character (except newline character)
^ Start with "^hello"
$ Ends with "world$"
* zero or more occurrences "aix*"
+ one or more occurences "aix+"
{ } Exactly the specified number of occurences "al{2}"
[ ] A set of characters "[a-m]"
\ Special sequence (or escape special characters) "\d"
| Either or "falls|stays"
( ) capture and group
```

# More Special Characters

\d : Matches any decimal digit; [0-9]
\D : Matches any non-digit character;
\s : Matches any whitespace character; (space " " tab  "\t" newline "\n")
\S : Matches any non-whitespace character;
\w : Matches any alphanumeric (word) character; [a-zA-Z0-9_]
\W: Matches any non-alphanumeric character;
\b : Matches where the specified characters are at the beginning or at the end of a word
\B: Matches where the specified characters are present, but NOT at the beginning or end

# Quantifier

```
* - 0 or more
+ - 1 or more
? - 0 or 1 -> optional character
{9} - exact number
{4,6} - range of number {min, max}
```
