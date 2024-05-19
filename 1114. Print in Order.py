'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads.
 Thread A will call first(), thread B will call second(), 
 and thread C will call third(). Design a mechanism and modify the program to ensure that second() 
 is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though 
the numbers in the input seem to imply the ordering. The input format you see is mainly 
to ensure our tests' comprehensiveness.
'''
class Foo(object):
    def __init__(self):
        self.a, self.b, self.c = 0, 0, 0

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a = 1

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while self.a != 1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.b = 1
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while self.b != 1:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.c = 1