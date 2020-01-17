# 【第四节】PyQt5菜单和工具栏

在这部分PyQt5教程中，我们将创建菜单和工具栏。

### 主窗口

QMainWindow类提供了一个主要的应用程序窗口。
你用它可以让应用程序添加状态栏，工具栏和菜单栏。

### 状态栏

状态栏用于显示状态信息。

[example_01.py](../../sample/【第四节】PyQt5菜单和工具栏/example_01.py)

你用QMainWindow创建状态栏的小窗口。

```python
self.statusBar().showMessage('Ready')
```

QMainWindow类第一次调用statusBar()方法创建一个状态栏。后续调用返回的状态栏对象。
showMessage()状态栏上显示一条信息。