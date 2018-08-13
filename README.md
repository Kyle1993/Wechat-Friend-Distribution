# 微信好友统计机器人  
以网页登录的方式统计微信好友的省份分布，性别分布。通过 __文件传输助手__ 返回统计数据  

## 库依赖  
* [安装wxpy](https://github.com/youfou/wxpy/blob/master/docs/index.rst)  
* [安装basemap及geo](https://matplotlib.org/basemap/users/installing.html)(如果不需要可视化省份分布可不安装)  
```bash  
pip3 install -r requirements.txt   
```
## 运行  
```python  
python3 friends_distribution.py  
```
如果不需要可视化省份分布：  
```python  
python3 friends_distribution.py -map False  
```

## 效果
<img src="./Screenshot.png" width="50%" height="50%">  
<img src="./map.png" width="60%" height="60%">  
<img src="./fig.png" width="50%" height="50%">  

## TODO
* 台湾地区的province显示是台湾的城市，比如‘Kaohsiung City’(高雄),而city显示的是‘’，没办法统计