# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|    Input   |    Expected Behavior    |      Actual Behavior     |              Console Output / Error              |
|------------|-------------------------|--------------------------|--------------------------------------------------|
|     30     |        Go Higher        |        Go Lower          |                     None                         |
|     60     |        Go Lower         |        Go Higher         |                     None                         |
|  New Game  |     New Game Starts     |     Nothing Happens      | You already won. Start a new game to play again. |
| Easy Game  | Range: 1-20, Attempt: 6 | Range: 1-100, Attempt: 5 |             The range is not accurate            |
| Easy Game  |        Attempt: 6       |         Attempt: 5       |           Attempt number was off by one          |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The game always uses the range 1-100. It doubles down on an error i caught on as well. 
AI Suggestion: random.rantin(1,100) should be random.randit(low, high)
Seems reasonable to use the variable low and high which store the upper and lower bound of the range depending on the difficulty. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
AI Suggestion: points = 100 - 10 * (attempt_number)
However, even the user guesses on the first attempt, they don't get a 100. I testing this using print statements.

My Suggestion: points = 100 - 10 * (attempt_number - 1)
This makes sense because when number attempt_number = 1, and i guess the secret, i should get 100 points (no deduction). With AI suggestion, the maximum score i get is 90. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
