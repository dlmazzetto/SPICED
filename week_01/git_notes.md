# Version Control with Git: Agenda

### 1. Overview

- Please create an account on GitHub dot com.



### 2. Simple Git / GitHub Workflow 

1. Make some change to the state of the repository:
   - adding some new file that wasn't there before
   - editing an existing file 
   - deleting a file
2. ``git status``
3. ``git add <name-of-file>``
4. ``git status``
5. ``git commit -m "some useful message"``
6. *You can use* ``git log`` *to view the history of commits you've ever done*
7. ``git push origin master``
   - you may be asked to log in. If you have not yet configured "ssh keys", then this is a normal procedure
   - you may also be prompted to give your name and email address.



---

*Break Somewhere in Between*

---



### 3. How will we use Git in this course?

2 repositories we care about:

- ``logistic-lemongrass-encounter-notes``
  - This is for teachers to share code / lesson notes / material from the encounters (i.e. "lessons / lectures") to the students to ``pull`` from.
- ``logistic-lemongrass-student-code``
  - This is where students will create their own branches and push their work.

Please refer to the [course material](https://krspiced.pythonanywhere.com/chapters/your_data_science_toolbox/git/README.html) on how we will use these 2 repos throughout the course.

### 4. Final Thoughts

Things to do:

- Internalize the basic git workflow commands! It's super important that this becomes second-nature to you.
- **Configure your Github email address in your bash terminal!**:
  - ``git config --global user.email`` to view the email that is associated with your Github account.
  - ``git config --global user.email "insert-your-actual-email-here"`` to updated it!
  - If you don't do this, the commits you push in GitHub might not attribute properly to your GitHub profile!
  - I will manually check all of your branches to see if I see this issue.
- Every time a teacher finishes an encounter and they did some notes / live coding, you can get it on your computer too!
  - Either by looking at it at https://github.com/spicedacademy/logistic-lemongrass-encounter-notes
  - or actually pulling the latest changes: ``git pull origin master``

