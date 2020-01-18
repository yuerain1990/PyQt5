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

![批注 2020-01-18 005936.png](../../sample/【第四节】PyQt5菜单和工具栏/示意图/批注%202020-01-18%20005936.png "批注 2020-01-18 005936.png")

### 菜单栏

菜单栏是常见的窗口应用程序的一部分。（Mac OS将菜单条不同。得到类似的结果，
我们可以添加以下行：menubar.setNativeMenuBar）

[example_02.py](../../sample/【第四节】PyQt5菜单和工具栏/example_02.py)

在上面的例子中，我们创建一个菜单和一个菜单。这个菜单将终止应用程序。
Ctrl+Q的行动是可访问的快捷方式。

```python
exitAction = QAction(QIcon('exit.png', '&Exit', self))
exitAction.setShortcut('Ctrl+Q')
exitAction.setStatusTip('Exit application')
```

QAction可以操作菜单栏，工具栏，或自定义键盘快捷键。上面三行，我们创建一个事件
和一个特定的图标和一个“退出”的标签。然后，在定义该操作的快捷键。

第三行创建一个鼠标指针悬停在该菜单项上时的提示。

```python
exitAction.triggered.connect(qApp.quit)
```

当我们点击菜单的时候，调用qApp.quit，终止应用程序。

![批注 2020-01-18 230444.png](../../sample/【第四节】PyQt5菜单和工具栏/示意图/批注%202020-01-18%20230444.png "批注 2020-01-18 230444.png")

### 工具栏

工具栏提供了一个快速访问的入口。

[example_03.py](../../sample/【第四节】PyQt5菜单和工具栏/example_03.py)

在上面的例子中，我们创建一个简单的工具栏。工具栏有一个按钮，点击关闭窗口。

```python
exitAction = QAction(QIcon('exit.png'), '&Exit', self)
exitAction.setShortcut('Ctrl+Q')
exitAction.triggered.connect(qApp.quit)
```

类似于上面的菜单栏的例子，我们创建一个QAction事件。该事件有一个标签、
图标和快捷键。退出窗口的方法。

![批注 2020-01-18 232745.png](../../sample/【第四节】PyQt5菜单和工具栏/示意图/批注%202020-01-18%20232745.png "批注 2020-01-18 232745.png")


### 把他们放在一起

在本节的最后一个例子中，我们将创建一个菜单条，工具栏和状态栏的小窗口。

[example_04.py](../../sample/【第四节】PyQt5菜单和工具栏/example_04.py)

创建了一个窗口

```python
textEdit = QTextEdit()
self.setCentralWidget(textEdit)
```

我们创建了一个QTextEdit，并把他设置为窗口的布局。

![批注 2020-01-18 235141.png](../../sample/【第四节】PyQt5菜单和工具栏/示意图/批注%202020-01-18%20235141.png "批注 2020-01-18 235141.png")