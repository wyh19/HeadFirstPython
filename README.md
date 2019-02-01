## 关于本项目
本项目是《HeadFirst Python》学习笔记、代码练习。我对着书学习时，希望不仅仅是自己入门python,还希望能帮到其他人。因此练习时，增加了足够的代码注释以及思维引导，其他python学习者可以直接阅读本项目的练习代码进行pthon学习。

## 目录结构
* base 文件夹放置了练习代码
* book-source 文件夹放置了书本提供的资源文件，无需关心

## 学习方式
如果你手头有《HeadFirst Pyhton》这本书的话，对着书来学习当然是更好的选择了。
如果没有，那么按base文件夹下文件顺序阅读和练习每一个py文件,也是个不错的选择。

## 避开一些误区
* 这本书更像是python的观光书，没有详细介绍python的语法，而是带着读者快速了解python的最常规的用法。因此，学习完这里的代码，你并不能成为一个python高手，甚至都不算一个合格的入门者，但是也不用担心你在浪费时间，这是最快让你用上python的学习途径。
* 学完这里，依然要好好学习python的语法，而不是直接上手一些复杂项目，有时候过于贪快，容易导致知识体系打不开。

# 使用VS Code一定要看
如果你使用pycharm,无需往下看。
使用VS Code,由于本项目的py文件写在base目录下，按F5执行调试时，会找不到相对路径的文件，需要在launch.json里添加 "cwd":""
由于我把launch.json一并上传到github上了，所以直接clone下代码的项目是不会遇到这个问题的，但是知道这里有个坑更好。

```json
{
    "name": "Python: Current File (Integrated Terminal)",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal",
    "cwd":""
}
```

[问题详情](https://stackoverflow.com/questions/54471395/why-is-python-assuming-my-path-is-the-project-root-which-is-two-directory-level)
[cwd配置项](https://code.visualstudio.com/docs/python/debugging#_cwd)
