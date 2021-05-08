# [Python Readline Completions](https://www.ironalbatross.net/wiki/index.php5?title=Python_Readline_Completions)

  * 1 Python Readline Tab Completion
    * 1.1 Setting up the basics
    * 1.2 The simplest case
    * 1.3 Slightly more complex (Stateless, No Grammar)
    * 1.4 Designing a Completer class
    * 1.5 A quick note and fix
    * 1.6 Complex problem (Regular Grammar)
  * 2 Simple FSAs
    * 2.1 Follow sets for a Regular Grammar
      * 2.1.1 Non-sequence verifying
      * 2.1.2 Sequence Verifying
  * 3 Taking it Beyond the Limit
  * 4 Introducing Dynamic Content


GNU/Readline makes it trivally easy to allow for editing a command inline and adding a history of past commands. However, with a little bit of work we can go one step further and add in a tab line completion to our program. This will allow users to rely less on documentation for mundane tasks. And thanks to pythons powerful language features, we can do this very quickly and efficiently.

Lets begin:

## Setting up the basics

First we will need a program which takes user input (using raw_input) and uses readline. This will be trivial.

ex1.py:

```python
    #!/usr/bin/python

    import readline
    readline.parse_and_bind("tab: complete")
    line = raw_input('prompt> ')
```

By simply importing readline, all future calls to raw_input or input will have the readline line editing and history. And by adding the call to readline.parse_and_bind("tab: complete") we have turned on tab completion. However, we are currently using the default tab completer. This will allow us to access files or objects in the local python scope, which is wicked cool to be sure, but we want to implement our own readline completion system.

## The simplest case

We will need to overwrite the default complete function with one of our design. We will need to write a function of the following form:

  * function(string Text, int State) => String result | None



This function will be called in a strange manner, it will be called with increasing numbers for State until it returns None. Each return value represents a possible return value. Theoretically we want to return an array, but we actually want to return the requested element of the array. The simplest way of doing this is by calculating all possible completions, and then returning the one indexed by State.

Lets do a simple example that only has one possible completion, and that is the word "example". This means that whenever we hit tab, the current word will be replaced with the word "example". This will overwrite any part of the word written so far.

ex2.py:

```python
    #!/usr/bin/python

    import readline

    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        results = ["example",None]
        return results[state]

    readline.set_completer(complete)

    line = raw_input('prompt> ')
```

Example run:


    jkenyon@prometheus:~/src/python/complete$ ./ex2.py prompt> **foo**


... Press tab


    jkenyon@prometheus:~/src/python/complete$ ./ex2.py prompt> **example**


The word "example" was filled in as the proper completion of the word foo. This will only affect the currently typed word:


    jkenyon@prometheus:~/src/python/complete$ ./ex3.py prompt> **foo ba**


... Press Tab


    jkenyon@prometheus:~/src/python/complete$ ./ex3.py
    prompt> foo example


##  Slightly more complex (Stateless, No Grammar)

Now, in those examples pressing tab would turn the word provided entirely into the word "example", which doesn't make any sense. In this example, I will provide a small dictionary of interesting words which we will complete based on the actual text provided.

Our volcabulary will consist of the following words: **dog,cat,rabbit,bird,slug,snail**

I specifically chose slug and snail to start with the same letter for example purposes.

This example of filling out volcabularies is simple because it is stateless, we will see a few more complex tasks coming up soon.

ex3.py:

```python
    #!/usr/bin/python

    import readline
    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        volcab = ['dog','cat','rabbit','bird','slug','snail']
        results = [x for x in volcab if x.startswith(text)] + [None]
        return results[state]

    readline.set_completer(complete)

    line = raw_input('prompt> ')
```

Now we can try running this:

 **run 1:**


    jkenyon@prometheus:~/src/python/complete$ ./ex3.py prompt> _<tab double tapped here>_
    **bird cat dog rabbit slug snail**
    prompt>


**run 2:**


    jkenyon@prometheus:~/src/python/complete$ ./ex3.py prompt> r _<tab pressed here>_

    jkenyon@prometheus:~/src/python/complete$ ./ex3.py
    prompt> rabbit


**run 3:**


    jkenyon@prometheus:~/src/python/complete$ ./ex3.py prompt> s _<tab double tapped here>_
    **slug snail**
    prompt> s


This is already a fantastic improvement over a purely dumb terminal, and the amount of work required was trivial.

## Designing a Completer class

Lets re-do the last example but we want to pack it into a class so we can extend its functionality more easily. We want a class which has its volcabulary or logic setup by the constructor. After that, we can make good use of pythons first class functions, and pass the complete function defined inside of the class, without losing access to our class object.

stub:


    class VolcabCompleter:


def __init__(self,volcab): ... def complete(self,text,state): ...

So now lets fill in that stub. ex3.1.py

```python
    #!/usr/bin/python

    import readline
    readline.parse_and_bind("tab: complete")

    class VolcabCompleter:
        def __init__(self,volcab):
            self.volcab = volcab

        def complete(self,text,state):
            results =  [x for x in self.volcab if x.startswith(text)] + [None]
            return results[state]

    words = ['dog','cat','rabbit','bird','slug','snail']
    completer = VolcabCompleter(words)

    readline.set_completer(completer.complete)

    line = raw_input('prompt> ')
```

Alternatively, one could use closures and nested functions to reduce the total code length, but that will make your code much harder to understand for future users of your code.

## A quick note and fix

One issue with both volcab examples is that when it completes a word, it does not add a space after that word. So when it completes the word "dog", future presses of the tab button will inform the user that the only way to complete the word "dog" is with the word "dog". We can fix this by adding a space to the end of each word after we read the volcabulary in.

```python
    #!/usr/bin/python import readline
    readline.parse_and_bind("tab: complete") class VolcabCompleter: def __init__(self,volcab): self.volcab = volcab def complete(self,text,state): results = [ **x+" "** for x in self.volcab if x.startswith(text)] + [None]
            return results[state]

    words = ['dog','cat','rabbit','bird','slug','snail']
    completer = VolcabCompleter(words)

    readline.set_completer(completer.complete)

    line = raw_input('prompt> ')
```

##  Complex problem (Regular Grammar)

Now we must address the more complex issue of a Regular Grammar. This time we will take into account for the fact that we may have a tree of commands, as if several verbs, several objects specific to each verb. I am restricting this example to grammars represented by acyclic graphcs (so it is not truely a regular grammar, but this is also just an example).

For this example, we will auto-complete an interface for a silly game (I am saving all the applicable examples for real problems). We are in control of a military base that can build structures, train infantry and research technology. This simple example has a small number of cases, but it will illustrate the point.

[Image:CommandTree.png](https://www.ironalbatross.net/wiki/index.php5?title=Special:Upload&wpDestFile=CommandTree.png)

So a few example commands would be:

  * train riflemen
  * build generator
  * research armor

However, it would be **incorrect** to say:

  * research barracks
  * train generator
  * build food

Now we need a data structure to hold this simple language of ours. Ideally (and maybe in a later article) we would setup a regex engine to deal with this sort of grammar, and we would use a full table to act as an finite automata to process the string so far. However, for the sake of simple practicality, we will just use a bunch of nested python dictionaries.

{ 'build': { 'barracks':None, 'generator':None, 'lab':None }, 'train': { 'riflemen':None, 'rpg':None, 'mortar':None }, 'research': { 'armor':None, 'weapons':None, 'food':None } }


So we have used Python Dictionaries to build a simple tree structure. We can traverse this tree using simple recusive decent.


    psuedocode for a traversal function:
    if no leaf provided
        no possible completions
    if end of path
        search this branch for completion
    if path incomplete
        continue walking tree


The complete code is structured as follows. The class ARLCompleter is short for Acyclic Regular Language Completer. It takes the dictionary tree described above as its constructor parameter. Internally it defines the complete function which does some book keeping, then calls the recusrive function traverse.

ex4.py:

```python
    #!/usr/bin/python import readline
    readline.parse_and_bind("tab: complete") class ARLCompleter: def __init__(self,logic): self.logic = logic def traverse(self,tokens,tree): if tree is None: return [] elif len(tokens) == 0: return [] if len(tokens) == 1: return [x+' ' for x in tree if x.startswith(tokens[0])] else: if tokens[0] in tree.keys(): return self.traverse(tokens[1:],tree[tokens[0]]) else: return [] return [] def complete(self,text,state): try: tokens = readline.get_line_buffer().split() if not tokens or readline.get_line_buffer()[-1] == ' ': tokens.append( _)_
                results = self.traverse(tokens,self.logic) + [None]
                return results[state]
            except Exception,e:
                print e

    logic = {
        'build':
                {
                'barracks':None,
                'bar':None,
                'generator':None,
                'lab':None
                },
        'train':
                {
                'riflemen':None,
                'rpg':None,
                'mortar':None
                },
        'research':
                {
                'armor':None,
                'weapons':None,
                'food':None
                }
        }

    completer = ARLCompleter(logic)
    readline.set_completer(completer.complete)

    line = raw_input('prompt> ')
```

This is a very powerful design, since any change to the dictionary tree will immedialy work, no matter the depth of the tree, and no mater the relationships. This is sufficient for most all usual control systems. All future examples are really overkill for most all real world scenarios.

## Simple FSAs

This simple tree structure really provides almost all functionality we will ever need. But just in case, I will try to keep on going with the examples. If nothing else, this will provide examples of how to handle complex grammars for simple tasks in python.

## Follow sets for a Regular Grammar

Now I would like to describe a language which could have cycles and repeated elements. So I will use the structure of a song. All songs start with an intro, and all end with a fade, but in the middle they can be composed of choruses, verses and solos.

[Image:MusicAutomata.png](https://www.ironalbatross.net/wiki/index.php5?title=Special:Upload&wpDestFile=MusicAutomata.png)

So our transition rules could read as follows. rules5.txt


    $->intro
    $->silence
    silence->intro
    intro->verse
    intro->chorus
    verse->chorus
    verse->solo
    verse->fade
    chorus->verse
    chorus->chorus
    chorus->solo
    chorus->fade
    solo->chorus
    solo->verse
    solo->fade


The $->x indicates that that x is a legal first token (a start symbol, kind of).

### Non-sequence verifying

The init function now serves to read in our rules file, and create the rules data structure (dictionary). The new "process" function takes the token stream and analyzes it to determine if we want a start symbol or a normal transition. If it is normal, it looks at the last complete token (which is token[-2]) to get a list of possible completions, and narrows it down based on what has been written so far in the current token (which is token[-1]). As before, the actual complete function just breaks the input buffer into tokens and manages formating.

ex5.py

```python
#!/usr/bin/python

import readline
readline.parse_and_bind("tab: complete")

class SFACompleter:
    def __init__(self,transfile):
        fin = open(transfile,"r")
        self.rules = {}
        self.start = []
        for line in fin:
            assert('->' in line)
            line = line.strip()
            first,second = line.split('->')
            if first == '$':
                self.start.append(second)
                if second not in self.rules:
                    self.rules[second] = []
            else:
                if first not in self.rules:
                    self.rules[first] = []
                if second not in self.rules:
                    self.rules[second] = []
                self.rules[first].append(second)
        fin.close()

    def process(self,tokens):
        if len(tokens) == 0:
            return []
        elif len(tokens) == 1:
            return [x+" " for x in self.start if x.startswith(tokens[-1])]
        else:
             ret = [x+" " for x in self.rules[tokens[-2]] if x.startswith(tokens[-1])]
        return ret

    def complete(self,text,state):
        try:
            tokens = readline.get_line_buffer().split()
            if not tokens or readline.get_line_buffer()[-1] == " ":
                tokens.append()
            results = self.process(tokens)+[None]
            return results[state]
        except Exception,e:
            print
            print e
            print
        return None

completer = SFACompleter("rules5.txt")
readline.set_completer(completer.complete)

line = raw_input('prompt> ')
```

###  Sequence Verifying

## Taking it Beyond the Limit

Ok, this section is likely never to come, since it involves a much harder language to parse, the Context Free Grammar. Ideally, we could design a full context free grammar using Yacc style rules, and then calculate the follow sets for each terminal symbol. This would require a lot of work, research and reading on my part, and I don't know if I will have the time. Hopefully this will happen sometime, but for now the rest of the examples should work.

## Introducing Dynamic Content

So far, all of our grammars have been from a narrow set of volcabulary. However, sometimes completions will specify an object which is dynamically pulled from the environment. For example, we may want to complete the name of a variable, or a file, or a server. At the simple level, we just change the complete function to pull and compare against a list of available files or variables, which we will do an example of just to demonstrate it. However, we may also want to intermix them, use a static vocabulary until you get to a certain grammatical structure is recognized, then call a function to dynamically generate the next set of possible completions.
