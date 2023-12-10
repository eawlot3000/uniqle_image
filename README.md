# uniqle media 📁
A user-specific [multi-threads supporting](https://github.com/eawlot3000/uniqle_media#performance) CLI tool that help you find out duplicated media (images/videos) from a specifc directory
----
### [中文版本](cn-README.md)


# Features
* support user-specific multi-threads now!
* create a duplicated folder to store your wasted so that you can review it and move on
* any errors handling and also performance display


# Performance
<<<<<<< HEAD
1. I have tested a folder which has 683 images up to 835MB with different formats, including 19 duplicates. with `MAX_THREADS = 64`, it took `14 seconds` to finish perfectly!
2. For a updated 1.18GB folder that has 2438 images and vidoes includes 534 duplicates, took 23 seconds!
=======
I have tested a folder which has 683 images up to 835MB with different formats, including 19 duplicates. with `MAX_THREADS = 64`, it only took `14 seconds` to finish perfectly!

### how to maximum the speed if you have better configs?
modify `MAX_THREADS = [YOUR DESIRED THREADS]` in [fast.py](fast.py) file. You should try yourself for best performance because everyone's machine is different.

# requirements
```
pip install -r requirements.txt
```

# usage
```
python fast.py [FOLDER/]
```

<br>

----
### TODO
* `time priority`
* exception data type support? [-args] 
* multi directories at the same time? [multi arguments]
* multi threads to improve speed? ✅
* in root? (great for clean your disk space yuh?)
* GPU support? (tf needs python <= 3.9, NO arm mac)

<br>

`tree view`
```
.
├── README.md
├── copy_main.py
├── fast.py ==> search faster!
├── main.py
├── performance
├── requirements.txt
```
