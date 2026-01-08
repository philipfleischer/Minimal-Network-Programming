Terminal output:
bruker@MacBook-Pro-2 ~ % curl -4 http://localhost:5000/videos
{"video1": {"title": "Hello World in python", "uploadDate": 20210917}, "video2": {"title": "Why language something", "uploadDate": 20210918}}
bruker@MacBook-Pro-2 ~ % curl -4 http://localhost:5000/videos -d "title=Newest Awesome Video" -d "uploadDate=20220101" -X POST
{"video3": {"title": "Newest Awesome Video", "uploadDate": 20220101}}
bruker@MacBook-Pro-2 ~ % curl -4 http://localhost:5000/videos -d "title=Newest Awesome Videpååpppppåååååååo" -d "uploadDate=20190101" -X POST
{"video4": {"title": "Newest Awesome Videp\u00e5\u00e5ppppp\u00e5\u00e5\u00e5\u00e5\u00e5\u00e5\u00e5o", "uploadDate": 20190101}}
bruker@MacBook-Pro-2 ~ % curl -4 http://localhost:5000/videos
{"video4": {"title": "Newest Awesome Videp\u00e5\u00e5ppppp\u00e5\u00e5\u00e5\u00e5\u00e5\u00e5\u00e5o", "uploadDate": 20190101}, "video1": {"title": "Hello World in python", "uploadDate": 20210917}, "video2": {"title": "Why language something", "uploadDate": 20210918}, "video3": {"title": "Newest Awesome Video", "uploadDate": 20220101}}
bruker@MacBook-Pro-2 ~ %

## Look at videos.json for output

## 127.0.0.1:5000/videos/all

![Video screenshot](image.png)
