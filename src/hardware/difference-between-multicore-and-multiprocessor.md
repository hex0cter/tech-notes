# [Difference between MultiCore and MultiProcessor](http://superuser.com/questions/214331/what-is-the-difference-between-multicore-and-multiprocessor)

A [CPU](http://en.wikipedia.org/wiki/Cpu), or Central Processing Unit, is what is typically referred to as a processor. A processor contains many discrete parts within it, such as one or more memory caches for instructions and data, instruction decoders, and various types of execution units for performing arithmetic or logical operations.

A multiprocessor system contains more than one such CPU, allowing them to work in parallel. This is called SMP, or Simultaneous Multiprocessing.

A multi*core* CPU has multiple execution cores one one CPU. Now, this can mean different things depending on the exact architecture, but it basically means that a certain subset of the CPU's components is duplicated, so that multiple "cores" can work in parallel on separate operations. This is called CMP, Chip-level Multiprocessing.

For example, a multicore processor may have a separate L1 cache and execution unit for each core, while it has a shared L2 cache for the entire processor. That means that while the processor has one big pool of slower cache, it has separate fast memory and artithmetic/logic units for each of several cores. This would allow each core to perform operations at the same time as the others.

There is an even further division, called [SMT](http://en.wikipedia.org/wiki/Simultaneous_multithreading), Simultaneous Multithreading. This is where an even smaller subset of a processor's or core's componenets is duplicated. For example, an SMT core might have duplicate thread scheduling resources, so that the core looks like two separate "processors" to the operating system, even though it only has one set of execution units. One common implementation of this is Intel's Hyperthreading.

Thus, you could have a multiprocessor, multicore, multithreaded system. Something like two quad-core, hyperthreaded processors would give you 2x4x2 = 16 logical processors from the point of view of the operating system.

Different workloads benefit from different setups. A single threaded workload being done on a mostly single-purpose machine benefits from a very fast, single-core/cpu system. Workloads that benefit from highly-parallelized systems such as SMP/CMP/SMT setups include those that have lots of small parts that can be worked on simultaneously, or systems that are used for lots of things at once, such as a desktop being used to surf the web, play a Flash game, and watch a video all at once. In general, hardware these days is trending more and more toward highly parallel architectures, as most single CPU/core raw speeds are "fast enough" for common workloads across most models.
