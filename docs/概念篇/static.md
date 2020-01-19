- static修饰的变量和属性，在全局数据区开辟空间，只有当程序运行结束才会释放

- inline 可将其修饰的方法，内联到函数调用处，不会有函数调用栈空间消耗，不需要预编译，会检查函数入参；但函数里不许有太多的内存消耗，否则内联函数失效

- session锁，当使用session_start()时，用户首次访问，php产生一个ID并设置到用户cookie中；非首次访问，获取用户的cookie，加载session对应的内容。

- 当使用session_start()时，操作系统会锁住session文件，这是一个读写锁，任何session读取都必须等到锁被释放之后。session锁主要是为了防止多个进程同时写时的覆盖写问题，而对于读数据来说是安全的，因此可以在读完session数据之后立刻释放锁，以避免阻塞其他进程。php5和php7的做法分别如下：

```
php5:

<?php
session_start();

session_write_close();
?>


php7:

<?php
session_start(['read_and_close'=>true]);
```

