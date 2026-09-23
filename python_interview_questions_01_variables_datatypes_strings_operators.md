# Python Interview Questions — Variables, Data Types, Strings & Operators

> Comprehensive interview-preparation question bank based on the Python topics covered so far.

---

# 1. Python Variables

## A. Basic Questions

1. What is a variable in Python?
2. How do you create a variable in Python?
3. Does Python require variable declaration before assignment?
4. How do you assign a value to a variable?
5. Can one variable be assigned to another variable?
6. Can multiple variables be assigned in one line?
7. Can multiple variables have the same value?
8. What happens when you assign a new value to an existing variable?
9. Are Python variables statically typed or dynamically typed?
10. What does dynamic typing mean in Python?
11. Can the type of a Python variable change during execution?
12. What is the difference between a variable and a value?
13. What is the difference between `x = 10` and `x = "10"`?
14. What happens when you write `x = 10`?
15. How can you check the type of a variable?
16. What does the `type()` function return?
17. Are variable names case-sensitive in Python?
18. What is the difference between `age` and `Age`?
19. Can a variable name contain spaces?
20. Can a variable name start with a number?
21. Can a variable name contain an underscore?
22. Can a variable name contain numbers?
23. Can a variable name start with an underscore?
24. What are valid variable names in Python?
25. What are invalid variable names in Python?
26. What are Python keywords?
27. Can a Python keyword be used as a variable name?
28. How should Python variables generally be named?
29. What is the difference between `studentName` and `student_name`?
30. What is PEP 8's general naming convention for variables?

## B. Multiple Assignment

31. What is multiple assignment in Python?
32. Explain `x, y, z = 1, 2, 3`.
33. What happens if the number of variables does not match the number of values?
34. What does `x = y = z = 10` mean?
35. How can you swap two variables in Python?
36. What is special about Python's tuple unpacking?
37. What is the output of:
   ```python
   a, b = 10, 20
   print(a, b)
   ```
38. What happens here?
   ```python
   a, b = 10
   ```
39. What happens here?
   ```python
   a, b, c = 10, 20, 30
   ```

## C. Dynamic Typing Questions

40. What does dynamically typed mean?
41. Is Python a dynamically typed language?
42. What is the output?
   ```python
   x = 10
   x = "Python"
   print(x)
   ```
43. What is the output?
   ```python
   x = 10
   print(type(x))
   x = 10.5
   print(type(x))
   ```
44. Does dynamic typing mean Python has no types?
45. If Python is dynamically typed, are values still associated with types?
46. What is the difference between dynamic typing and static typing?
47. Why can a variable hold values of different types at different times?

## D. Practical / Interview Coding Questions

48. Create variables for a student's name, age, marks, and enrollment status.
49. Write a program that stores two numbers and prints their sum.
50. Write a program that swaps two variables.
51. Create three variables in a single line.
52. Assign the same value to three variables.
53. Write a program that prints both the value and type of several variables.
54. Write a program demonstrating that Python variables are dynamically typed.
55. Write a program that converts a string number into an integer.
56. What naming convention would you use for a variable storing a user's first name?
57. How would you name a variable containing a student's date of birth?

---

# 2. Python Data Types

## A. Fundamental Questions

58. What is a data type?
59. Why are data types important?
60. What are Python's built-in data types?
61. How can you check the data type of an object?
62. What does `type()` do?
63. What is `NoneType`?
64. What is the difference between `None` and `False`?
65. What is the difference between `None` and `0`?
66. What is the difference between `None` and an empty string?
67. What does Python use to determine a value's type?
68. Can a variable's data type change during execution?

## B. Numeric Data Types

69. What is an integer in Python?
70. What is a float in Python?
71. What is a complex number in Python?
72. How do you create an integer?
73. How do you create a float?
74. How do you create a complex number?
75. What is the difference between `10` and `10.0`?
76. What is the type of `10`?
77. What is the type of `10.0`?
78. What is the type of `10 + 5j`?
79. What does `j` represent in a complex number?
80. Can Python integers be very large?
81. What happens when you divide two integers using `/`?
82. What is the difference between `/` and `//`?

## C. String Data Type

83. What is the `str` data type?
84. How do you create a string?
85. What is the difference between single and double quotes?
86. Can strings contain numbers?
87. What is the difference between `"100"` and `100`?
88. What is a multiline string?
89. How can you create a multiline string?
90. What is the type of `"Python"`?
91. Is a string a sequence type?
92. Can strings be indexed?
93. Can strings be modified directly?

## D. List

94. What is a list?
95. How do you create a list?
96. Can a list contain different data types?
97. Is a list ordered?
98. Is a list mutable?
99. Can a list contain duplicate values?
100. What is the type of `[1, 2, 3]`?
101. What is the difference between a list and a string?
102. What is the difference between a list and a tuple?

## E. Tuple

103. What is a tuple?
104. How do you create a tuple?
105. Is a tuple mutable or immutable?
106. Can a tuple contain duplicate values?
107. Can a tuple contain different data types?
108. What is the type of `(1, 2, 3)`?
109. What is the difference between `(1, 2, 3)` and `[1, 2, 3]`?
110. Why might you use a tuple instead of a list?

## F. Range

111. What is the `range` data type?
112. What does `range(5)` represent?
113. What is the type of `range(5)`?
114. Does `range(5)` include 5?
115. What values are represented by `range(5)`?
116. Why is `range()` useful in loops?

## G. Dictionary

117. What is a dictionary?
118. How do you create a dictionary?
119. What is a key-value pair?
120. Can dictionary keys be duplicated?
121. Can dictionary values be duplicated?
122. Can dictionary values have different data types?
123. What is the type of `{"name": "Aayushman"}`?
124. What is the difference between a dictionary and a list?
125. What is the difference between a dictionary and a set?

## H. Set

126. What is a set?
127. How do you create a set?
128. Does a set allow duplicate values?
129. Is a set ordered?
130. What is the difference between a set and a list?
131. What is the difference between a set and a tuple?
132. What is a `frozenset`?
133. What is the difference between `set` and `frozenset`?

## I. Boolean

134. What is a Boolean?
135. What are the two Boolean values in Python?
136. What is the type of `True`?
137. What is the type of `False`?
138. Where are Boolean values commonly used?
139. What is the difference between `True` and `"True"`?
140. What is the difference between `False` and `0`?

## J. Binary Types

141. What are binary data types in Python?
142. What is `bytes`?
143. What is `bytearray`?
144. What is `memoryview`?
145. What is the difference between `bytes` and `bytearray`?
146. Where might binary types be useful?

## K. Type Constructors and Conversion

147. What is type casting?
148. What does `int()` do?
149. What does `float()` do?
150. What does `str()` do?
151. What does `list()` do?
152. What does `tuple()` do?
153. What does `dict()` do?
154. What does `set()` do?
155. What does `bool()` do?
156. What does `complex()` do?
157. What happens when you run `int("10")`?
158. What happens when you run `float("10")`?
159. What happens when you run `str(10)`?
160. What happens when you run `int("10.5")`?
161. What happens when you run `int("Python")`?
162. What is the difference between conversion and changing a variable's type automatically?

## L. Output / Tricky Questions

163. What is the output?
   ```python
   x = 10
   print(type(x))
   ```

164. What is the output?
   ```python
   x = 10.0
   print(type(x))
   ```

165. What is the output?
   ```python
   x = "10"
   print(type(x))
   ```

166. What is the output?
   ```python
   x = True
   print(type(x))
   ```

167. What is the output?
   ```python
   x = None
   print(type(x))
   ```

168. What is the output?
   ```python
   x = [1, 2, 3]
   print(type(x))
   ```

169. What is the output?
   ```python
   x = (1, 2, 3)
   print(type(x))
   ```

170. What is the output?
   ```python
   x = {1, 2, 3}
   print(type(x))
   ```

171. What is the output?
   ```python
   x = {"a": 1}
   print(type(x))
   ```

---

# 3. Python Strings

## A. String Fundamentals

172. What is a string in Python?
173. How do you create a string?
174. What is the difference between single and double quotes?
175. Can you use both single and double quotes in Python?
176. How do you create a multiline string?
177. What are triple quotes?
178. Are strings sequences?
179. Are strings indexed?
180. Does Python use zero-based indexing for strings?
181. What is the first index of a string?
182. What is the last index of a string?
183. What is negative indexing?
184. What does `text[-1]` return?
185. What does `text[0]` return?
186. What happens if you access an index that does not exist?
187. What is the length of a string?
188. How do you find string length?
189. What does `len()` return?

## B. String Indexing

190. What is the output?
   ```python
   text = "Python"
   print(text[0])
   ```

191. What is the output?
   ```python
   text = "Python"
   print(text[-1])
   ```

192. What is the output?
   ```python
   text = "Python"
   print(text[2])
   ```

193. How do you access the last character of a string?
194. How do you access the second-last character?
195. How do you iterate through every character in a string?

## C. String Slicing

196. What is string slicing?
197. What is the syntax for slicing?
198. What does `text[1:4]` mean?
199. Is the ending index included in slicing?
200. What does `text[:4]` mean?
201. What does `text[2:]` mean?
202. What does `text[:]` mean?
203. What is negative slicing?
204. What does `text[-4:-1]` mean?
205. What happens if the start index is omitted?
206. What happens if the end index is omitted?

## D. String Searching

207. How do you check whether a substring exists?
208. What does the `in` operator do with strings?
209. What does `not in` do?
210. What is the difference between `in` and `find()`?
211. What does `find()` return when the substring is not found?
212. What does `count()` do?
213. How do you count how many times a word occurs in a string?
214. What does `startswith()` do?
215. What does `endswith()` do?

## E. String Modification

216. Are Python strings mutable?
217. What does immutable mean?
218. Can you change one character of a string directly?
219. Why does `text[0] = "X"` fail?
220. How does `replace()` work?
221. What does `upper()` do?
222. What does `lower()` do?
223. What does `capitalize()` do?
224. What does `title()` do?
225. What does `swapcase()` do?
226. What does `strip()` do?
227. What is the difference between `strip()`, `lstrip()`, and `rstrip()`?
228. What does `split()` do?
229. What does `join()` do?
230. What is the difference between `split()` and `join()`?
231. Do string methods modify the original string?
232. Why must you assign the result of a string method if you want to keep the changed string?

## F. Escape Characters

233. What is an escape character?
234. What does `\n` represent?
235. What does `\t` represent?
236. What does `\\` represent?
237. What does `\"` represent?
238. How do you include a quote inside a string?
239. How do you print a Windows-style file path?
240. What is a raw string?

## G. String Concatenation

241. What is string concatenation?
242. How do you concatenate two strings?
243. What does the `+` operator do with strings?
244. What happens if you try to concatenate a string and an integer?
245. How can you concatenate a number with a string safely?
246. What is the difference between concatenation and interpolation?

## H. f-Strings / String Formatting

247. What is an f-string?
248. Why are f-strings useful?
249. How do you insert a variable into an f-string?
250. Can you put expressions inside an f-string?
251. What is the output?
   ```python
   age = 22
   print(f"I am {age} years old.")
   ```
252. What is the output?
   ```python
   age = 22
   print(f"Next year I will be {age + 1}.")
   ```
253. How do you format a floating-point number to two decimal places?
254. What does `:.2f` mean?
255. What is the difference between f-strings and string concatenation?
256. Why are f-strings generally convenient for readable formatted strings?

## I. String Methods

257. What is a string method?
258. How do you call a string method?
259. What does `capitalize()` do?
260. What does `casefold()` do?
261. What does `center()` do?
262. What does `count()` do?
263. What does `encode()` do?
264. What does `endswith()` do?
265. What does `find()` do?
266. What does `index()` do?
267. What does `isalnum()` do?
268. What does `isalpha()` do?
269. What does `isdigit()` do?
270. What does `isdecimal()` do?
271. What does `islower()` do?
272. What does `isspace()` do?
273. What does `istitle()` do?
274. What does `isupper()` do?
275. What does `join()` do?
276. What does `ljust()` do?
277. What does `lower()` do?
278. What does `lstrip()` do?
279. What does `partition()` do?
280. What does `replace()` do?
281. What does `rfind()` do?
282. What does `rindex()` do?
283. What does `rjust()` do?
284. What does `rsplit()` do?
285. What does `rstrip()` do?
286. What does `split()` do?
287. What does `splitlines()` do?
288. What does `startswith()` do?
289. What does `strip()` do?
290. What does `swapcase()` do?
291. What does `title()` do?
292. What does `translate()` do?
293. What does `upper()` do?
294. What does `zfill()` do?

## J. String Output Questions

295. What is the output?
   ```python
   text = "Python"
   print(text.upper())
   ```

296. What is the output?
   ```python
   text = "  Python  "
   print(text.strip())
   ```

297. What is the output?
   ```python
   text = "Python Programming"
   print(text.replace("Python", "Java"))
   ```

298. What is the output?
   ```python
   text = "Python"
   print(len(text))
   ```

299. What is the output?
   ```python
   text = "Python"
   print(text[1:4])
   ```

300. What is the output?
   ```python
   text = "Python"
   print(text[::-1])
   ```

301. What is the output?
   ```python
   text = "apple,banana,cherry"
   print(text.split(","))
   ```

302. What is the output?
   ```python
   words = ["Python", "is", "easy"]
   print(" ".join(words))
   ```

303. What is the output?
   ```python
   text = "Python Python"
   print(text.count("Python"))
   ```

304. What is the output?
   ```python
   text = "Python"
   print("Py" in text)
   ```

305. What is the output?
   ```python
   text = "Python"
   print("Java" not in text)
   ```

---

# 4. Python Operators

## A. General Operator Questions

306. What is an operator in Python?
307. What is an operand?
308. What are unary operators?
309. What are binary operators?
310. What are Python's major categories of operators?
311. What is the difference between an operator and an operand?
312. Give examples of arithmetic, comparison, logical, identity, and membership operators.

## B. Arithmetic Operators

313. What are arithmetic operators in Python?
314. What does `+` do?
315. What does `-` do?
316. What does `*` do?
317. What does `/` do?
318. What does `%` do?
319. What does `**` do?
320. What does `//` do?
321. What is the difference between `/` and `//`?
322. What is the modulus operator?
323. Where is `%` useful in programming?
324. What is exponentiation?
325. What does `2 ** 3` return?
326. What does `10 // 3` return?
327. What does `10 % 3` return?
328. What does `10 / 3` return?
329. What happens with negative numbers and floor division?
330. What is the output?
   ```python
   print(10 + 5)
   ```
331. What is the output?
   ```python
   print(10 - 5)
   ```
332. What is the output?
   ```python
   print(10 * 5)
   ```
333. What is the output?
   ```python
   print(10 / 5)
   ```
334. What is the output?
   ```python
   print(10 // 3)
   ```
335. What is the output?
   ```python
   print(10 % 3)
   ```
336. What is the output?
   ```python
   print(2 ** 4)
   ```

## C. Assignment Operators

337. What is the assignment operator?
338. What does `=` mean in Python?
339. What does `+=` do?
340. What does `-=` do?
341. What does `*=` do?
342. What does `/=` do?
343. What does `//=` do?
344. What does `%=` do?
345. What does `**=` do?
346. What are augmented assignment operators?
347. What is the difference between `=` and `==`?
348. What is the output?
   ```python
   x = 10
   x += 5
   print(x)
   ```
349. What is the output?
   ```python
   x = 10
   x *= 3
   print(x)
   ```
350. What is the output?
   ```python
   x = 10
   x %= 3
   print(x)
   ```

## D. Comparison Operators

351. What are comparison operators?
352. What do comparison operators return?
353. What does `==` mean?
354. What does `!=` mean?
355. What does `>` mean?
356. What does `<` mean?
357. What does `>=` mean?
358. What does `<=` mean?
359. What is the difference between `=` and `==`?
360. Can comparison operators be used with strings?
361. What is the output?
   ```python
   print(10 == 10)
   ```
362. What is the output?
   ```python
   print(10 != 5)
   ```
363. What is the output?
   ```python
   print(10 > 5)
   ```
364. What is the output?
   ```python
   print(10 < 5)
   ```

## E. Logical Operators

365. What are logical operators?
366. What does `and` do?
367. What does `or` do?
368. What does `not` do?
369. What is the difference between `and` and `or`?
370. How does `not` change a Boolean expression?
371. Can logical operators be used with comparison expressions?
372. What is short-circuit evaluation?
373. How does `and` short-circuit?
374. How does `or` short-circuit?
375. What is the output?
   ```python
   print(True and True)
   ```
376. What is the output?
   ```python
   print(True and False)
   ```
377. What is the output?
   ```python
   print(True or False)
   ```
378. What is the output?
   ```python
   print(not True)
   ```
379. What is the output?
   ```python
   age = 22
   print(age >= 18 and age <= 60)
   ```

## F. Identity Operators

380. What are identity operators?
381. What does `is` mean?
382. What does `is not` mean?
383. What is the difference between `is` and `==`?
384. Does `is` compare values or object identity?
385. When should you use `is`?
386. Why is `is None` commonly used?
387. What is the output?
   ```python
   x = ["Python"]
   y = x

   print(x is y)
   ```
388. What is the output?
   ```python
   x = ["Python"]
   y = ["Python"]

   print(x is y)
   ```
389. What is the difference between:
   ```python
   x == y
   ```
   and:
   ```python
   x is y
   ```

## G. Membership Operators

390. What are membership operators?
391. What does `in` do?
392. What does `not in` do?
393. Can membership operators be used with strings?
394. Can membership operators be used with lists?
395. Can membership operators be used with tuples?
396. Can membership operators be used with sets?
397. Can membership operators be used with dictionaries?
398. What does `in` check for a dictionary?
399. What is the output?
   ```python
   print("Python" in "Python Programming")
   ```
400. What is the output?
   ```python
   print(2 in [1, 2, 3])
   ```
401. What is the output?
   ```python
   print("name" in {"name": "Aayushman"})
   ```

## H. Bitwise Operators

402. What are bitwise operators?
403. What does `&` do?
404. What does `|` do?
405. What does `^` do?
406. What does `~` do?
407. What does `<<` do?
408. What does `>>` do?
409. Where are bitwise operators useful?
410. What is the difference between logical `and` and bitwise `&`?
411. What is the difference between logical `or` and bitwise `|`?
412. What does `10 & 3` return?
413. What does `10 | 3` return?
414. What does `10 ^ 3` return?
415. What does `10 << 1` do?
416. What does `10 >> 1` do?

## I. Operator Precedence — Important

417. What is operator precedence?
418. Why is operator precedence important?
419. What happens first in `10 + 5 * 2`?
420. What is the output of:
   ```python
   print(10 + 5 * 2)
   ```
421. What is the output of:
   ```python
   print((10 + 5) * 2)
   ```
422. Which has higher precedence: `*` or `+`?
423. Which has higher precedence: `**` or `*`?
424. Which has higher precedence: comparison operators or arithmetic operators?
425. Which has higher precedence: `and` or `or`?
426. Which has higher precedence: `not` or `and`?
427. How can parentheses change operator precedence?
428. Give a basic precedence order for Python operators.
429. What is the output?
   ```python
   print(10 + 2 * 3 ** 2)
   ```
430. What is the output?
   ```python
   print((10 + 2) * 3 ** 2)
   ```
431. Why should parentheses sometimes be used even when Python already knows the precedence?
432. What is the difference between precedence and associativity?

---

# 5. Mixed Interview Questions

These questions combine variables, data types, strings, and operators.

433. What is the output?
   ```python
   x = 10
   y = "20"
   print(x + int(y))
   ```

434. What is the output?
   ```python
   name = "Python"
   print(name * 3)
   ```

435. What is the output?
   ```python
   x = "10"
   y = "20"
   print(x + y)
   ```

436. What is the output?
   ```python
   x = 10
   y = 20
   print(str(x) + str(y))
   ```

437. What is the output?
   ```python
   age = 22
   print(f"I am {age} years old.")
   ```

438. What is the output?
   ```python
   text = "Python"
   print(text[0] + text[-1])
   ```

439. What is the output?
   ```python
   text = "Python"
   print(text[:3])
   ```

440. What is the output?
   ```python
   text = "Python"
   print(text[::-1])
   ```

441. What is the output?
   ```python
   x = 10
   y = 3
   print(x // y, x % y)
   ```

442. What is the output?
   ```python
   x = 10
   x += 5
   print(x)
   ```

443. What is the output?
   ```python
   age = 22
   is_student = True

   print(age > 18 and is_student)
   ```

444. What is the output?
   ```python
   x = None
   print(x is None)
   ```

445. What is the output?
   ```python
   name = "Aayushman"
   print("A" in name)
   ```

446. What is the output?
   ```python
   result = 10 + 5 * 2
   print(result)
   ```

447. What is the output?
   ```python
   result = (10 + 5) * 2
   print(result)
   ```

448. Explain the difference:
   ```python
   x = 10
   ```
   versus:
   ```python
   x == 10
   ```

449. Explain the difference between:
   ```python
   "10"
   ```
   and:
   ```python
   10
   ```

450. Explain the difference between:
   ```python
   x == y
   ```
   and:
   ```python
   x is y
   ```

451. Explain the difference between:
   ```python
   / 
   ```
   and:
   ```python
   //
   ```

452. Explain the difference between:
   ```python
   +
   ```
   for numbers and strings.

453. What happens when you multiply a string by an integer?

454. What happens when you add two strings?

455. What happens when you add a string and an integer?

456. How would you convert user input `"25"` into an integer?

457. How would you check whether a variable contains a string?

458. How would you check whether a string contains a particular word?

459. How would you remove extra spaces from user input?

460. How would you convert a string to uppercase?

461. How would you format a number inside a sentence?

462. How would you check whether a variable is `None`?

463. How would you check whether two variables refer to the same object?

464. How would you calculate the remainder of a division?

465. How would you calculate the square of a number using an operator?

466. How would you check whether a number is greater than or equal to 18?

---

# 6. Beginner Coding Questions

467. Write a program to store your name and print it.
468. Write a program to store your name, age, and city and print them.
469. Write a program to print the type of five different variables.
470. Write a program to add two numbers.
471. Write a program to subtract two numbers.
472. Write a program to multiply two numbers.
473. Write a program to divide two numbers.
474. Write a program to find the remainder of two numbers.
475. Write a program to calculate the square of a number.
476. Write a program to calculate the cube of a number.
477. Write a program to convert Celsius to Fahrenheit.
478. Write a program to calculate the area of a rectangle.
479. Write a program to calculate the area of a circle.
480. Write a program to swap two variables.
481. Write a program to convert a string number into an integer.
482. Write a program to convert an integer into a string.
483. Write a program to check whether a number is greater than 18.
484. Write a program to check whether a number is even using `%`.
485. Write a program to check whether a number is odd using `%`.
486. Write a program to check whether a word exists inside a string.
487. Write a program to count the number of characters in a string.
488. Write a program to convert a string to uppercase.
489. Write a program to convert a string to lowercase.
490. Write a program to remove spaces from the beginning and end of a string.
491. Write a program to replace one word with another.
492. Write a program to reverse a string using slicing.
493. Write a program to print the first character of a string.
494. Write a program to print the last character of a string.
495. Write a program to extract the first three characters of a string.
496. Write a program using an f-string to create a sentence from variables.
497. Write a program to check whether a string starts with a particular word.
498. Write a program to check whether a string ends with a particular extension.
499. Write a program to split a comma-separated string into a list.
500. Write a program to join a list of words into a sentence.

---

# 7. Conceptual Follow-Up Questions

501. Why is Python dynamically typed?
502. Why are strings immutable?
503. Why does `type()` matter in debugging?
504. Why is type conversion important when processing user input?
505. Why is `"10"` different from `10`?
506. Why is `is` different from `==`?
507. Why should `is` generally be used with `None` for identity checks?
508. Why does `10 + 5 * 2` not evaluate from left to right?
509. Why are parentheses useful in complex expressions?
510. Why are f-strings useful in real-world Python?
511. Why are string methods important in data processing?
512. Why are lists, tuples, dictionaries, and sets all separate data types?
513. What does mutability mean?
514. Which common Python types are mutable?
515. Which common Python types are immutable?
516. Why does immutability matter for strings?
517. What is the difference between a sequence and a mapping?
518. What is the difference between ordered and unordered collections?
519. What is the difference between equality and identity?
520. How do operators interact with different data types?

---

# 8. Rapid-Fire Revision

521. What symbol assigns a value to a variable? → `=`
522. What checks equality? → `==`
523. What checks identity? → `is`
524. What checks membership? → `in`
525. What checks the type of a value? → `type()`
526. What finds string length? → `len()`
527. What converts to integer? → `int()`
528. What converts to float? → `float()`
529. What converts to string? → `str()`
530. What converts to Boolean? → `bool()`
531. What converts to a list? → `list()`
532. What converts to a tuple? → `tuple()`
533. What converts to a set? → `set()`
534. What removes surrounding whitespace? → `strip()`
535. What converts text to uppercase? → `upper()`
536. What converts text to lowercase? → `lower()`
537. What replaces text? → `replace()`
538. What splits a string? → `split()`
539. What joins strings? → `join()`
540. What creates formatted strings easily? → f-strings
541. What gives the remainder? → `%`
542. What performs floor division? → `//`
543. What performs exponentiation? → `**`
544. What means logical AND? → `and`
545. What means logical OR? → `or`
546. What means logical NOT? → `not`
547. What checks that two references are not the same object? → `is not`
548. What checks that a value is not present? → `not in`
549. What determines expression evaluation order? → operator precedence
550. What can override normal precedence? → parentheses

---

# 9. High-Priority Questions to Master First

If an interviewer asks beginner-level Python questions, make sure you can answer these without hesitation:

1. What is a variable in Python?
2. What does dynamically typed mean?
3. What are Python's main built-in data types?
4. What is the difference between `int`, `float`, `str`, and `bool`?
5. What is the difference between `22` and `"22"`?
6. What does `type()` do?
7. What is type casting?
8. What is the difference between a list, tuple, set, and dictionary?
9. What is a string?
10. What is string indexing?
11. What is string slicing?
12. What is negative indexing?
13. Are strings mutable or immutable?
14. What does `len()` do?
15. What does `strip()` do?
16. What does `replace()` do?
17. What does `split()` do?
18. What does `join()` do?
19. What are f-strings?
20. What is string concatenation?
21. What are arithmetic operators?
22. What is the difference between `/` and `//`?
23. What does `%` do?
24. What does `**` do?
25. What is the difference between `=` and `==`?
26. What are comparison operators?
27. What are logical operators?
28. What is the difference between `and`, `or`, and `not`?
29. What is the difference between `==` and `is`?
30. What are membership operators?
31. What is operator precedence?
32. What is the output of `10 + 5 * 2`?
33. Why is `(10 + 5) * 2` different?
34. What happens when you add a string and an integer?
35. How do you convert `"25"` to `25`?
36. How do you check whether `"Python"` exists in a string?
37. How do you reverse a string?
38. How do you check whether a variable is `None`?
39. How do you swap two variables in Python?
40. Write a small program combining variables, strings, data types, and operators.

---

# Interview Preparation Strategy

For every question, practice answering in this order:

1. **Definition** — What is it?
2. **Syntax** — How is it written?
3. **Example** — Show a small example.
4. **Output** — Explain what happens.
5. **Real-world use** — Explain where you would use it.

Example:

**Question:** What is an f-string?

**Strong beginner answer structure:**

- An f-string is a formatted string literal in Python.
- It allows variables and expressions to be embedded directly inside a string.
- It is written by putting `f` before the string.
- Example:
  ```python
  name = "Aayushman"
  print(f"Hello {name}")
  ```
- It is useful when creating readable dynamic text.

---

# Topics Covered So Far

```text
01. Python Print
02. Python Variables
03. Python Data Types
04. Python Strings
05. Python Operators
```

This question bank specifically covers:

```text
Python Variables
        ↓
Python Data Types
        ↓
Python Strings
        ↓
Python Operators
        ↓
Operator Precedence
        ↓
Mixed Practical Questions
```
