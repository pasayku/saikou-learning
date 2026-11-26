# Learning Journal

## 07-10-2026

- **Lesson 0.1**: made my GitHub account and practice repo.
- **Lesson 0.2**: installed VS Code, Git, Node.js, pnpm, Python and the GitHub CLI.
- **Lesson 0.3**: cloned my repo and made my first commit. I don't know how to make "one" code into two lines and pressing enter withouting executing like this;

  ```
  cd saikou-learning
  code .
  ```

  tried to type it but every time I press enter it just runs `cd saikou-learning`, which retuns an error. Shift/Control + enter were not working.
  learned 4 new commands `git add`, `git commit`, `git push` and `git status`.
  `git add` tells git which file to include, I don't whether it can add multiple files at once.
  and `git commit -m`, it's a bit confusing, but I think it records/saves the changes you are making. Not sure what `-m` does.
  `git push` and `git status` were the easiest to understand. But I wonder if you can just push without going through the first 2 commands.

## 08-10-2026

- **Lesson 0.4**: made my first pull. Also learned new commands and shortcuts. Overall the lesson was not difficult. I didn't encounter any error I couldn't resolve myself.
- Made a Commans.md file, where I'm recording commands and what they do.

## 09-10-2026

- **Lesson 0.5**: this was the most time consuming by far but I learned a lot.
- struggled with writting problems in my own words. I'll try to get better at that.
- learned how to update a commit and also learned commit some messages. Which had me wondering but was cleared in this lesson.
- despite it taking so long, I enjoyed it a lot. I hope more lessons are this fun.

## 11-10-2026

- **Lesson 0.6**: before starting the lesson, I had to correct the typos and the spellig mistakes I made from the previous lesson.
- created my first python file, and learned what a syntaxError is, along with variables and how to use them in sentences.
- the difficult part was the numbers section. The basic operations like; `~`, `-`, `*` and `/` where straight forward but when I had to make a mark/score calculator, that showed the mark in a sentence as a percentage.
- After several errors and help from the auto complete, I understood the `round` function.  Completed the excerscise and get the correct mark as percentage rounded to 1 decimal place

## 16-10-2026

- **Lesson 0.7** started the lesson by correcting prevoius mistakes, which was tedious but was good prep for the lesson.
- learned what a *"REPL"* is, along with *booleans*, and the meainings of some signs.
- also learned what are `if`, `else`, and `elif` statements. Along with `and` and `or` and used them to make a boss fight, wich I enjoyed a lot. 
- I also added a the WASSCE grade to the score calculator program.

## 17-10-2026

- **Lesson 0.8** today was a big one. Before entering the lesson, I had to go back the last lesson and amend my mistakes, which I'm getting used to. I'm liking it now because it's like a revision, and I need, cause I low-key forget everything after a lesson. But this one was good
- Then I made my first *loop.py* file, where I learned the difference between a `while` loop and an `if` function, along with infinite loops and how to break loops, which wasn't easy.

## 18-10-2026

- still on **Lesson 0.8**. More than half of the time went into solving step 7 in the lesson. However after getting help from *Narciso*, I was able to complete it overnight. Then use the same method to complete step 8 and to make "mine", I made sure the program didn't when you enter a word instead of a number. 
- to make it mine more, I also tried to add taunts, and got very far but when I wanted, it to say when the guess was too high and/or the guess was too low, the program run into infiite loop. I could only get it to say, the guess was too high. I wanted to keep trying but had to get my day started. Next time, I know I can get it done.
- My problem is that, I don't actually understand their meaning, I have to keep trying until I get what I want. It's kinda like high school Trig, I never fully understood those functions but I knew how to use them. But this isn't high school, I don't want to forget anything I'm learning.

## 15-11-2026

- **Lesson 0.8 (Feedback & Fixes)**: took a 3–4 week break from lessons because of my attachment, and finally got back to it last week Wednesday to work through the feedback on Lesson 0.8.
- Started by fixing `score.py`. The main issue was how I handled my `while` loops and converting inputs to `int` too early. Once I understood that a `while` loop needs something inside it to change so the condition can actually become `False`, it clicked. I also fix up the `elif` conditions for the grades so no marks were Forgotten. It took two or three days, wasn't too hard, I just didn't have much time but I actually felt like I was making real progress.
- Then I moved on to `guess.py`. That one had a lot more errors I had indented loops and separate `if`and `while` blocks that kept trapping me in infinite loops. After being away for so long, I honestly didn't even remember half of what I had written, so I practically rebuilt it from scratch following the pseudo-code plan from the feedback. 
- Without that feedback breakdown, I would have been stuck for a long time, so following it step-by-step made it way easier to finally get the taunts, guess counter, and `isdigit()` validation working together.

## 19-11-2026

- **Lesson 0.9**: the lesson took me to back to correct my mistakes from the previous lesson as usual. I'm starting to realise that most of my errors come from me not testing my code enough, and it also had me wondering how Narciso catches all the errors, which are always too ovious when if fixing them. So in `score.py.` I forgot the `isdigit` check for when the mark is greater than the total. Since it wasn't a new error, this fix was easy and quick. Just a little bummed is missed it. 

## 25-11-2026
- **Lesson 0.9 (Update)**: After the "revison", the first part of the lesson, `lists`. How to assign a list to a variable. I also learned the necessary functions like `append`, `len`, `sum` `min` and `max`. Then I used a `for` loop to go through a list and also made 2 programs.
- The first program, `marks.py`, had me create a list called marks containing grades from 49 to 88. The goal was to list the number of marks, the average, the highest mark, and the lowest marks I used the functions for that. But challenge was writing a `for` loop with a condition to find every mark in marks that was greater than 50, keep a count of them, and add those qualifying marks to a credit list. After some time and a some pseudo code I wrote myself, I was able to get it.
- In the second program, `top5.py`, I made a list of my top five games, used `import.random` to pick one, and used `for` loops to rank them from one to five, including a reverse version. I also added an `if` statement star system for specific picks. Like printing five star emojis if the random pick was Cyberpunk 2077 to keep things simple. To be real, the ranking system took a very long time to figure.
- Lastly, it was time for the journal entry, which is starting to take the longest because I am a very slow typer, and it basically requires me to go through the whole lesson, which now is taking me days. So, it serves as a revision and. Although I'm realizing that is necessary. As compared to school, there was no journal and I would just forget everything after a class. But now, after I make a journal entry, it makes it it makes me understand it more. As difficult as I find it to write down my thoughts, I'm getting better at it, for someone who never used to journal. Now I look forward to it, even though I struggle with it. Yeah, that's it for lesson nine. I hope in the next lesson, I don't get too many corrections.