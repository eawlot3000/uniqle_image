# uniqle media 📁
一个支持用户自定义[多线程的CLI 工具](https://github.com/eawlot3000/uniqle_media#performance)，可帮助您从特定目录中查找重复的媒体（图像/视频）
----
### [English version](README.md)


# 功能
* 现在支持用户特定的多线程！
* 创建一个重复的文件夹，以存储您浪费的媒体，以便您可以查看并继续前进
* 任何错误处理以及性能显示


# 性能
我已经测试了一个包含 683 张图片，总共 835MB 的文件夹，其中包括 19 个重复项。在 `MAX_THREADS = 64` 的情况下，它仅花费了 `14 秒` 完成！
### 如何最大化速度？
在 [faster_main.py](faster_main.py) 文件中修改 `MAX_THREADS = [YOUR DESIRED THREADS]`。您应该自己尝试，以获得最佳性能，因为每个人的机器都不同。

# 要求
pip install -r requirements.txt


# 用法
```
python faster_main.py [FOLDER/]
```


<br>

----
### 待办事项
* 优先级！总体处理时间
* 异常数据类型支持？[-args]
* 同时处理多个目录？[多个参数]
* 多线程以提高速度？✅
* 在根目录下？（非常适合清理您的磁盘空间）
* GPU 支持？（tf 需要 python <= 3.9）

<br>

`树形视图`
```
.
├── README.md
├── copy_main.py
├── faster_main.py ==> search faster!
├── main.py
├── performance
├── requirements.txt
```
