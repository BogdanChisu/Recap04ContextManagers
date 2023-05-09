"""
----------------------------------------
CONTEXT MANAGER
----------------------------------------

RESOURCE MANAGEMENT

When developing software, there are times when we want to access and manage certaun resources, such as
file operations or database connections. Resources are often limited, so it is good practice to release
them as soon as you stop using them.

File operations
----------------------------------------

File operations are an example or resource management
"""
f = open("file.txt", "w")
f.write("Hello World")
f.close()
"""
The above lines of code give access to the file in write mode, saving a line of text into it and then
closing the file.

However, there may be an error when trying to write to the file. It will result in a throw exception, so
the file will not be closed, and consequently we will deal with memory leaks.

To protect against this, our code should look like this:
"""
f = open("file.txt", "w")
try:
    f.write("Hello worlds")
except IOError:
    print("Error occured")
finally:
    f.close()
"""
In this way we are sure that access to the file will be released, whether the execution is smooth or not.


CONTEXT MANAGER
----------------------------------------

Using the context manager makes the whole process easier: we wrapp the open() function in a with clause
which improves the readability of the code while ensuring that access to an open file is released,
regardless of the circumstances.
"""
with open("file.txt", "w") as f:
    f.write("Hello world")
"""
----------------------------------------
CREATE YOUR OWN MANAGERS
----------------------------------------

We also habe the option of creating our own context managers. We can do this in two ways: by creating a
class or a function. In this way, we can ensure, for example, support for access to the database, without
having to remember to close the connection each time and thus protect ourselves against memory leaks.

Own Content Manager as a Class
----------------------------------------

If we want to create a manager as a class, we must remember to implement the methods __enter__ and
__exit__. The first one must open(file, database, connections, etc.) and share resources. The __exit__
operations are responsible for cleaning and releasing resources (closing a file, connecting to the
database).
"""

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # opening and sharing of resource
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # cleaning, release of resources
        self.file.close()

if __name__ == "__main__":
    with FileManager("test.txt", "w") as f:
        f.write("Test")

"""
Own Content Manager as a Class
----------------------------------------

If we want to create a manager as a function, we need to import the contextmanager decorator from the
contextlib module. Next, we create a function that connects to the resources, then makes these resources
available using the yield command. It returns an object like the return command, but does not block
further program execution. We'll learn more about this when discussing generators and iterators. Finnaly
we release access to the resources. We have to remember to decorate the created function by using
@contextmanager
"""
from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()

if __name__ == "__main__":
    with file_manager("test.txt", "w") as f:
        f.write("Test2")