# [ClearCase Support: Understanding Config Specs](http://www.philforhumanity.com/ClearCase_Support_17.html)

I recently had a question concerning how to understand configuration specifications or config specs in ClearCase Views, so here goes.

A config spec is the mechanism that a ClearCase View determines what versions of an element that the user accesses. A config spec is only editable, by default, by the account that created the View. A config spec has a single rule on each line, and the lines are interpreted by ClearCase from the top to the bottom as the order of importance. For example, when you create a new ClearCase View, the default config spec is set to this:

```
element * CHECKEDOUT
element * /main/LATEST
```

Each rule basically consists of three parts. First the word "element", second what element to find, and third is the version to access. In this default config spec example, the first rule says to access the checkedout version of the element if the current View has the element checkedout for each element. If the View does not have the element checkedout, then the next rule is interpreted. In this example, the next rule dictates that the View will access the latest version of the element on the /main/ branch. This rule will guarantee to find a version to access, so any further rules, if any existed, will be ignored.

Lets take a look at this more complicated config spec with example #2:

```
element /vob/test/a.txt /main/3
element /vob/test/b.txt /main/4 # This is a comment.
#element * /main/LATEST
# The previous line is a comment, thus completely ignored.
element /vob/test/ /main/LATEST
```

The first rule states to only access the /main/3 version of the element "/vob/test/a.txt". This element may or may not exist, and ClearCase has no verification. Any other elements of a different path will ignore this rule. The second rule states to only access the /main/4 version of a different element called "/vob/test/b.txt". Note that anything after the first # symbol is a comment and is ignored. The third and fourth lines are comments, so they will be ignored even though they may have embedded rules. The fifth line says for all elements in the VOB call "/vob/test", access the latest versions on the /main/ branch, unless a previous rule already selected a version. Note that there are no rules in this config spec to access any versions in any other VOB, so all other VOBs will be inaccessible with this config spec.

You may want to take a mental break now, since the next example is much more complicated. If you dont know what are labels or branches yet, I recommend reading the other training web pages first. Here is example #3:

```
element /vob/training/hockey/ HOCKEY_LABEL
element /vob/training/baseball/ BASEBALL_LABEL
element /vob/training/football/ /football_branch/LATEST
element /vobs/training/ /main/LATEST
```

The first line says to access only the versions that have a label called "HOCKEY_LABEL" in the directory called /vobs/training/hockey. Not all files (or sub-directories) in this directory may have this rule, so these elements will not be accessed from this rule. Similarly, the second line says to access only the versions that have a label called "BASEBALL_LABEL" in the directory called /vobs/training/baseball. The third rule says to access the latest versions in the "/vob/training/football" directory on the /football_branch/ branch if that branch exists for each element. Otherwise the fourth rule says to access all other elements that the previous rules did not define to access by accessing the latest versions in the "/vob/training/" directory on the /main/ branch.

Confused yet? Well, it gets MUCH more complicated. Here is example #4:
```
element /vob/test/a.txt -none
element b.txt -none
element * /main/test/LATEST
element Cfile * /main/LATEST
element -directory * /main/LATEST
```

The first rule says to not access any versions of the element "/vob/test/a.txt". The second rule says to not access any versions that have the element name "b.txt" even if multiple files have the same filename in different directories. I strongly to always use the full paths when modifying config specs, otherwise unintended consequences may happen. The third rule says to access all the latest versions on the /main/test/ branch. Well, this is a bad example, because what if the user wanted to access versions on the /test/ branch, but the /test/ branch was not branching from the /main/ branch? For example /main/abc/test/3 would not be seen in this config spec. The better solution for this line would be "element * /test/LATEST".

The fourth rule says to access the latest versions of all files on the /main/ branch. The fifth rule says to access the latest versions of all directories on the /main/ branch too. The fourth and fifth rules combined are equal to "element * /main/LATEST", but there are sometimes reasons to handle directories and files differently.

Here is most confusing config spec example, and the most likely to be seen in the real world. Here is example #5:
```
element * CHECKEDOUT
element * /developers_branch/LATEST
element -file * RELEASED_LABEL -mkbranch developers_branch
element -file * /main/LATEST -mkbranch developers_branch
element * /main/LATEST
```

The first rule states to access the checkedout version if the current View has the element checkedout. The second rule states to access the latest version on the branch called /developers_branch/ if the branch exists. This is where the software developers typically make their code or documentation changes on their own personal branch. Each developer should have a unique branch for each change they are implementing too. The developer must have already created the branch type manually for this line to work correctly.

If the element is not already being modified on the developers branch, then the third rule will access the version for files that were labeled using the label called "RELEASED_LABEL", if the label exists. Furthermore, this is the version that will be branched from if the developer tries to checkout, if this label exists. The fourth rule is the same rule as the third rule, except this is for all files that do not have the label called "RELEASED_LABEL", so that new files can be added to source control and be accessed and modified accordingly. Finally, the fifth rule is for all the remaining elements, such as directories, to access the /main/LATEST versions and checkouts will not be on the developers branch.

I hope this explanation was clear, otherwise here is how to contact me for free advice.

by Phil B.
From
<http://www.philforhumanity.com/ClearCase_Support_17.html>
