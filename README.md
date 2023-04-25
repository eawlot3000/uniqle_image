# uniqle media 📁
a CLI tool that help you find out duplicated media (images/videos) from a specifc directory


# Features
* support user-specific multi-threads now!
* make sure `main.py` works but slow
* create a duplicated folder to store your wasted so that you can review it and move on


# Performance
I have tested a folder which has 683 images up to 835MB with different formats, including 19 duplicates. with `MAX_THREADS = 64`, it took `14 seconds` to finish perfectly!
### how to maximum the speed if you have better specs?
modify `MAX_THREADS = [YOUR DESIRED THREADS]` in `faster_main.py` file. You should try yourself for best performance because everyone's machine is different.

# requirements
```
pip install -r requirements.txt
```

# usage
```
python faster_main.py [FOLDER/]
```

<br>

----
### TODO
* PRIORITY! PROCESSING TIME IN GENERAL 
* exception data type support? [-args] 
* multi directories at the same time? [multi arguments]
* multi threads to improve speed? ✅
* in root? (great for clean your disk space yuh?)
* GPU support? (tf needs python <= 3.9)

<br>

`tree view`
```
.
├── README.md
├── copy_main.py
├── faster_main.py ==> search faster!
├── main.py
├── performance
├── requirements.txt
```
