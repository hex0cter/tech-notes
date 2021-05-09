# Dump thread info in Ruby

```ruby
STDERR.puts "=========== #{Thread.list.select {|thread| thread.status == "run"}.count} RUNNING THREAD ==========="
Thread.list.each do |thread|
  STDERR.puts "Thread-#{thread.object_id.to_s(36)}"
  STDERR.puts thread.backtrace.join("\n    \\_ ") unless thread.backtrace.nil?
end
```
