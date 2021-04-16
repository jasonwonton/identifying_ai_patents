First, install everything with our requirements.txt file <br>
```
pip3 install -r requirements.txt
```

1: Scrape all the patents <br>
After requirements.txt has been installed, we will download all the patent zip files (it will download to your downloads directory). <br> 
```
python3 scraper.py
```

After this is done, we can unzip into a master directory. <br> 
```
cd ../../Downloads
unzip *.zip -d USPTO_Patent_Dir
```

We can then sort the files into certain directories, but it is not a big deal currently. <br> 

2: use our list of AI patents to create a classifier<br>
3: use some NLP model to classify - either BERT or FastText<br>


