## 发布流程
1. 创建模块文件夹nester
2. 新建setup.py
3. 构建发布文件
```
cd nester
python3 setup.py sdist
```
4. 将发布安装到本地副本
```
cd nester
python3 setup.py install
```
5. 更新
```
cd nester
python3 setup.py sdist upload
```