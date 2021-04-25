
date: None  
author(s): None  

# [7 Ways to Run Shell Commands in Ruby - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/6-ways-to-run-shell-commands-in-ruby-1)

Often times we want to interact with the operating system or run shell commands from within Ruby. Ruby provides a number of ways for us to perform this task.

## Exec

`Kernel#exec` (or simply `exec`) replaces the current process by running the given command For example:
    
    
      $ irb
      >> exec 'echo "hello $HOSTNAME"'
      hello nate.local
      $
    
    

Notice how `exec` replaces the `irb` process is with the `echo` command which then exits. Because the Ruby effectively ends this method has only limited use. The major drawback is that you have no knowledge of the success or failure of the command from your Ruby script.

## System

The `system` command operates similarly but the `system` command runs in a subshell instead of replacing the current process. `system` gives us a little more information than `exec` in that it returns `true` if the command ran successfully and `false` otherwise.
    
    
      $ irb             
      >> system 'echo "hello $HOSTNAME"'
      hello nate.local
      => true
      >> system 'false' 
      => false
      >> puts $?
      256
      => nil
      >> 
    
    

`system` sets the global variable `$?` to the exit status of the process. Notice that we have the exit status of the `false` command (which always exits with a non-zero code). Checking the exit code gives us the opportunity to raise an exception or retry our command.

Note for Newbies: Unix commands typically exit with a status of `0` on success and non-zero otherwise. 

System is great if all we want to know is “Was my command successful or not?” However, often times we want to capture the output of the command and then use that value in our program.

## Backticks (`)

Backticks (also called “backquotes”) runs the command in a subshell and returns the standard output from that command.
    
    
      $ irb
      >> today = `date`
      => "Mon Mar 12 18:15:35 PDT 2007n" 
      >> $?
      => #<Process::Status: pid=25827,exited(0)>
      >> $?.to_i
      => 0
    
    

This is probably the most commonly used and widely known method to run commands in a subshell. As you can see, this is very useful in that it returns the output of the command and then we can use it like any other string.

Notice that `$?` is not simply an integer of the return status but actually a `Process::Status` object. We have not only the exit status but also the process id. `Process::Status#to_i` gives us the exit status as an integer (and `#to_s` gives us the exit status as a string).

One consequence of using backticks is that we only get the _standard output_ (` stdout`) of this command but we do not get the _standard error_ (` stderr`). In this example we run a Perl script which outputs a string to `stderr`.
    
    
      $ irb
      >> warning = `perl -e "warn 'dust in the wind'"`
      dust in the wind at -e line 1.
      => "" 
      >> puts warning
    
      => nil
    
    

Notice that the variable `warning` doesn’t get set! When we `warn` in Perl this is output on `stderr` which is _not_ captured by backticks.

## IO#popen

` IO#popen` is another way to run a command in a subprocess. `popen` gives you a bit more control in that the subprocess standard input and standard output are both connected to the `IO` object.
    
    
      $ irb
      >> IO.popen("date") { |f| puts f.gets }
      Mon Mar 12 18:58:56 PDT 2007
      => nil
    
    

While `IO#popen` is nice, I typically use `Open3#popen3` when I need this level of granularity.

## Open3#popen3

The Ruby standard library includes the class `Open3`. It’s easy to use and returns `stdin`, `stdout` and `stderr`. In this example, lets use the interactive command `dc`. `dc` is reverse-polish calculator that reads from `stdin`. In this example we will push two numbers and an operator onto the stack. Then we use `p` to print out the result of the operator operating on the two numbers. Below we push on `5`, `10` and `+` and get a response of `15\n` to `stdout`.
    
    
      $ irb
      >> stdin, stdout, stderr = Open3.popen3('dc') 
      => [#<IO:0x6e5474>, #<IO:0x6e5438>, #<IO:0x6e53d4>]
      >> stdin.puts(5)
      => nil
      >> stdin.puts(10)
      => nil
      >> stdin.puts("+")
      => nil
      >> stdin.puts("p")
      => nil
      >> stdout.gets
      => "15n" 
    
    

Notice that with this command we not only read the output of the command but we also write to the `stdin` of the command. This allows us a great deal of flexibility in that we can interact with the command if needed.

`popen3` will also give us the stderr if we need it.
    
    
      # (irb continued...)
      >> stdin.puts("asdfasdfasdfasdf")
      => nil
      >> stderr.gets
      => "dc: stack emptyn" 
    
    

However, there is a shortcoming with `popen3` in ruby 1.8.5 in that it doesn’t return the proper exit status in `$?`.
    
    
      $ irb
      >> require "open3" 
      => true
      >> stdin, stdout, stderr = Open3.popen3('false')
      => [#<IO:0x6f39c0>, #<IO:0x6f3984>, #<IO:0x6f3920>]
      >> $?
      => #<Process::Status: pid=26285,exited(0)>
      >> $?.to_i
      => 0
    
    

`0`? `false` is supposed to return a non-zero exit status! It is this shortcoming that brings us to `Open4`.

## Open4#popen4

`Open4#popen4` is a Ruby Gem put together by Ara Howard. It operates similarly to `open3` except that we can get the exit status from the program. `popen4` returns a process id for the subshell and we can get the exit status from that waiting on that process. (You will need to do a `gem instal open4` to use this.)
    
    
      $ irb
      >> require "open4" 
      => true
      >> pid, stdin, stdout, stderr = Open4::popen4 "false" 
      => [26327, #<IO:0x6dff24>, #<IO:0x6dfee8>, #<IO:0x6dfe84>]
      >> $?
      => nil
      >> pid
      => 26327
      >> ignored, status = Process::waitpid2 pid
      => [26327, #<Process::Status: pid=26327,exited(1)>]
      >> status.to_i
      => 256
    
    

A nice feature is that you can call `popen4` as a block and it will automatically wait for the return status.

`$ irb `

`>> require "open4" `

`=> true `

`>> status = Open4::popen4("false") do |pid, stdin, stdout, stderr| `

`?> puts "PID #{pid}" `

`>> end `

`PID 26598 `

`=> #<Process::Status: pid=26598,exited(1)> `

`>> puts status 256 => nil`

`**%x operator**`

`

The way I like to do this is using the %x operator, which makes it easy (and readable!) to use quotes in a command, like so:
    
    
    directorylist = %x[find . -name '*test.rb' | sort]  
    

Which, in this case, will populate file list with all test files under the current directory, which you can process as expected:
    
    
    directorylist.each do |filename|  
      filename.chomp!  
      # work with file  
    end

`

`<http://pasadenarb.com/2007/03/ruby-shell-commands.html>`

`<http://stackoverflow.com/questions/2232/calling-bash-commands-from-ruby>`

