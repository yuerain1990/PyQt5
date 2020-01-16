# 【第三节】PyQt5布局管理

PyQt5布局有两种方式，绝对定位和布局类

### 绝对定位

程序制定每个控件的位置和大小(以像素为单位)。

绝对定位有以下限制：

- 如果我们调整窗口，控件的大小和位置不会改变
- 在各种平台上应用程序看起来会不一样
- 如果改变字体，我们的应用程序的布局就会改变
- 如果我们决定改变我们的布局，我们必须完全重做我们的布局

下面的例子显示了一个绝对定位

[example_01.py](../../sample/【第三节】PyQt5布局管理/example_01.py)

我们使用move()方法来控制控件的位置

![批注 2020-01-15 232856.png](../../sample/【第三节】PyQt5布局管理/示意图/批注%202020-01-15%20232856.png "批注 2020-01-15 232856.png")


### 框布局 Boxlayout

我们使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。

[example_02.py](../../sample/【第三节】PyQt5布局管理/example_02.py)

在这个例子中，我们使用QHBoxLayout和QVBoxLayout并添加伸展因子，在窗口的右下角显示两个按钮。

```python
hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)
```

我们创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示。

```python
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)
```

创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部。

```python
self.setLayout(vbox)
```

最后，我们设置窗口的布局界面

![批注 2020-01-15 234456.png](../../sample/【第三节】PyQt5布局管理/示意图/批注%202020-01-15%20234456.png "批注 2020-01-15 234456.png")

### 表格布局

表格布局将空间划分为行和列。我们使用QGridLayout类创建一个网格布局。

[example_03.py](../../sample/【第三节】PyQt5布局管理/example_03.py)

在我们的示例中,我们创建一个网格的按钮。

```python
grid = QGridLayout()
self.setLayout(grid)
```

QGridLayout的实例被创建并设置应用程序窗口的布局。

```python
names = ['Cls', 'Bck', '', 'Close',
         '7', '8', '9', '/',
         '4', '5', '6', '*',
         '1', '2', '3', '-',
         '0', '.', '=', '+']
```

这些按钮的标签。

```python
positions = [(i,j) for i in range(5) for j in range(4)]
```

我们创建一个网格中的位置的列表。

```python
for position, name in zip(positions, names):
    if name == '':
        continue
    button = QPushButton(name))
    grid.addWidget(button, *position
```

创建按钮并使用addWidget()方法添加到布局中。

![批注 2020-01-16 003730.png](../../sample/【第三节】PyQt5布局管理/示意图/批注%202020-01-16%20003730.png "批注 2020-01-16 003730.png")

### 评论的例子

控件可以在网络中跨越多个行或列。在下一个示例中，我们说明了这一点。

[example_04.py](../../sample/【第三节】PyQt5布局管理/example_04.py)

我们创建一个窗口，其中有三个标签，两个行编辑和一个文本编辑窗口小控件。然后使用QGirdLayout完成布局。

```python
gird = QGridLayout()
grid.setSpacing(10)
```

创建一个网格布局和设置组件之间的间距。

```python
grid.addWidget(reviewEdit, 3, 1, 5, 1)
```

在添加一个小的控件到网络的时候，我们可以提供小部件的行和列跨。在例子中，reviewEdit控件跨度5行。

![批注 2020-01-16 005838.png](../../sample/【第三节】PyQt5布局管理/示意图/批注%202020-01-16%20005838.png "批注 2020-01-16 005838.png")