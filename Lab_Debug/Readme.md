Please refer to below link :

  https://courses.engr.illinois.edu/cs225/sp2018/labs/debug/
  
  
  Understand the System.

Without a solid understanding of the system (the system defined as being both the actual machine you are running on as well as the general structure behind the problem you are trying to solve), you can’t begin to narrow down where a bug may be occurring. Start off by assembling knowledge of:
What the task is
What the code’s structure is
What the control flow looks like
How the program is accomplishing things (library usage, etc)
When in doubt, look it up—this can be anything from using Google to find out what that system call does to simply reading through your lab’s code to see how it’s constructed.
Make it Fail.

The best way to understand why the bug is occurring is to make it happen again—in order to study the bug you need to be able to recreate it. And in order to be sure it’s fixed, you’ll have to verify that your fix works. In order to do that, you’ll need to have a reproducible test case for your bug.
A great analogy here is to turn on the water on a leaky hose—only by doing that are you able to see where the tiny holes might be (and they may be obvious with the water squirting out of them!).
You also need to fully understand the sequence of actions that happen up until the bug occurs. It could be specific to a certain type of input, for example, or only a certain branch of an if/else chain.
Quit Thinking and Look.

After you’ve seen it fail, and seen it fail multiple times, you can generally have an idea of at least what function the program may be failing in. Use this to narrow your search window initially.
Start instrumenting your code. In other words, add things that print out intermediate values to check assumptions that should be true of variables in your code. For instance, check that that pointer you have really is set to NULL.
Guessing initially is fine, but only if you’ve seen the bug before you attempt to fix it. Changing random lines of code won’t get you to a solution very fast, but will result in a lot of frustration (and maybe even more bugs)!
Divide and Conquer.

Just like you’d use binary search on an array to find a number, do this on your code to find the offending line! Figure out whether you’re upstream of downstream of your bug: if your values look fine where you’ve instrumented, you’re upstream of the bug (it’s happening later on in the code). If the values look buggy, you’re probably downstream (the bug is above you).
Fix the bugs as you find them—often times bugs will hide under one another. Fix the obvious ones as you see them on your way to the root cause.
Change One Thing at a Time.

Use the scientific method here! Make sure that you only have one variable you’re changing at each step—otherwise, you won’t necessarily know what change was the one that fixed the bug (or whether or not your one addition/modification introduces more).
What was the last thing that changed before it worked? If something was fine at an earlier version, chances are whatever you changed in the interim is what’s buggy.
Keep an Audit Trail.

Keep track of what you’ve tried! This will prevent you from trying the same thing again, as well as give you an idea of the range of things you’ve tried changing.
Check the Plug.

Make sure you’re assumptions are right! Things like “is my Makefile correct?” or “am I initializing everything?” are good things to make sure of before blindly assuming they’re right.
Get a Fresh View.

Getting a different angle on the bug will often times result in a fix: different people think differently, and they may have a different perspective on your issue.
Also, articulating your problem to someone often causes you to think about everything that’s going on in your control flow. You might even realize what is wrong as you are trying to describe it to someone! (This happens a lot during office hours and lab sections!)
When talking to someone, though, make sure you’re sticking to the facts: report what is happening, but not what you think might be wrong (unless we’re asking you what you think’s going on).
If you didn’t fix it, it ain’t fixed.

When you’ve got something you think works, test it! If you have a reproducible test case (you should if you’ve been following along), test it again. And test the other cases too, just to be sure that your fix of the bug didn’t break the rest of the program.
