# JD
Crawling some information and comments on a class of commodities from the Jingdong
明确爬取的是某类商品信息和评价内容
首先我们选择一个品类，“进口牛奶”
京东页面是动态加载的，为了获得全部的商品信息，需要执行js渲染
在这里我将selenium集成到scrapy中，获得整页的全部60个商品信息
之后分析评论内容api，爬取商品对应的评论信息，数据为json样式
