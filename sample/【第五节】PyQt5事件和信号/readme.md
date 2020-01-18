# 【第五节】PyQt5事件和信号

在这一部分的PyQt5教程中，我们将探讨PyQt5中的时间Event。

### 事件 Event

所有的GUI程序都是事件驱动的。事件主要由用户触发，但也可能有其他触发方式：
例如网络连接、window manager或定时器。当我们调用QApplication的exec_()
方法时会使程序进入主循环。主循环会获取并分发事件。

在事件模型中，有三个参与者：

- 事件源
- 事件对象
- 事件接收者

事件源时状态发生变化的对象。它会生成事件。事件（对象）封装了事件源中状态的变动。
事件接收者时要通知的对象。事件源对象将事件处理的工作交给事件接收者。

PyQt5有一个独特的signal&slot（信号槽）机制来处理事件。信号槽用于对象间的通信。
signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用
与之相连的slot。

### 信号槽 Signal & slots

这是一个使用信号槽的PyQt5例子。

[example_01.py](../../sample/【第五节】PyQt5事件和信号/example_01.py)

这个例子中展示了一个QtGui.QLCDNumber和QtGUI.QSlider。lcd的值会随着滑块的拖动而改变。

```python
sld.valueChanged.connect(lcd.display)
```

在这里我们将滑动条的valueChanged信号连接到lcd的display插槽。

sender是发出信号的对象。receiver是接收信号的对象。slot（插槽）是对信号做出反应的方法。

![批注 2020-01-19 004147.png](../../sample/【第五节】PyQt5事件和信号/示意图/批注%202020-01-19%20004147.png "批注 2020-01-19 004147.png")
