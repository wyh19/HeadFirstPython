## 发布流程
1. 创建模块文件夹nester，并编写要发布的代码，即nester.py文件
2. 新建setup.py,输入发布配置项信息
3. 构建发布文件,命令行进入nester文件夹，执行下面的命令
```bash
python3 setup.py sdist
```
4. 将发布安装到本地副本
```bash
python3 setup.py install
```
5. 如果安装后，nester.py代码有更新，则执行下面的命令
```bash
python3 setup.py sdist upload
```

## 说明
nester文件夹里除了nester.py和setup.py两个文件是自己写的，其他都是自动生成的，不用关心。
安装完，请打开 【4-使用模块.py】 进行使用