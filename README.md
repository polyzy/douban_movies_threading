#douban_movies_threading
该脚本主要是为了学习python中的threading和Queue模块。
分别使用多线程和不使用多线程抓取了2011,2012,2013,2014四年中豆瓣电影的前100部。
使用多线程的脚本中设置的线程数为４。
![](https://github.com/smartczy/douban_movies_threading/raw/master/weather.png)

#结果
使用多线程的脚本抓取所有数据总共耗时：23.54秒
不使用多线程的脚本抓取所有数据总共耗时：92.48秒
从结果可以看出，不使用多线程所消耗时间大约是使用多线程所耗时间的４倍，即为线程数。

#测试环境
* Python 2.7.6
* Ubuntu 14.04 32bit

