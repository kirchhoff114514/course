# 使用函数构建抽象

## 高阶函数

### 嵌套定义

在python中，传参(bind)和调用(call)的过程是不同的。当调用函数时

```python
return improve(sqrt_update, sqrt_close)
```

解释器会干下面几件事

1. 解释操作符improve，找到其定义，然后创建对应的帧
2. 逐个解释参数，将其绑定到形参上。先把sqrt_update绑定到形参update上，再把sqrt_close绑定到形参close上。注意这步只绑定没有具体运行sqrt_update和sqrt_close内部的每一行，因为这只是传参绑定值的过程，不是真正调用这两个函数；真正调用的地方在improve函数内部
3. 运行improve

### curring

```python
>>> def curry2(f):
        """返回给定的双参数函数的柯里化版本"""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
>>> def uncurry2(g):
        """返回给定的柯里化函数的双参数版本"""
        def f(x, y):
            return g(x)(y)
        return f
>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32
>>> map_to_range(0, 10, pow_curried(2))
1
2
4
8
16
32
64
128
256
512
```

这里柯里化和逆柯里化函数都进行了嵌套定义，这里嵌套的唯一作用就是提供参数作为内部函数的环境（详见上面讲闭包的地方）