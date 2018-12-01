Here is a nice explanation of Parallel Processing in Python: https://stackabuse.com/parallel-processing-in-python/

Time comparison\
---------------

C02VQ1S6HTDD:python_multiprocessing nsiddiq$ time python non_parallel_function.py

real	0m0.352s\
user	0m0.252s\
sys	0m0.081s\

C02VQ1S6HTDD:python_multiprocessing nsiddiq$ time python3 parallel_function.py

real	0m0.564s\
user	0m0.559s\
sys	0m0.250s\

The parallel version is slower! Why?\

Short answer: The square root function is not complex enough such that parallelizing it outweighs the time spent by the CPU in keeping track of all of the newly forked processes.\
Long but more detailed answer: https://stackoverflow.com/a/52076791

Process Pools

One can create a pool of processes which will carry out tasks submitted to it with the Pool class.

class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.

processes is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used.

…

map(func, iterable[, chunksize])

A parallel equivalent of the map() built-in function (it supports only one iterable argument though). It blocks until the result is ready.

This method chops the iterable into a number of chunks which it submits to the process pool as separate tasks. The (approximate) size of these chunks can be specified by setting chunksize to a positive integer.

Source: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool

