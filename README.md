Simply copy the bash script and evernoteCommit.py to /usr/bin/ directory
and use it in place of "git commit -m ...".

Usage:

    $ git add README.md
    $ evercommit 'initial commit'
      ...
      ...
      ...
    $ git add README.md
    $ evercommit 'finished writing examples of evernote auto note creator based on commits'
      ...
    $ git push origin master
