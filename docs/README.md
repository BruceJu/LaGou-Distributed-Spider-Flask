<style>
.div-border-image{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:auto;
    background: whitesmoke;
    border: yellowgreen inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }
.div-border-question{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:50px;
    padding:20px;
    background: whitesmoke;
    border: red inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }
.div-border-answer{
    margin-top: 20px;
    margin-bottom: 10px;
    box-shadow: 10px 10px 5px #888888;
    width:100%;
    hegiht:50px;
    padding:20px;
    background: whitesmoke;
    border: #4876FF inset;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 0px;
    border-left-width: 5px;
    border-radius: 5px;
    }       
</style>
# LaGou-Distributed-Spider-Flask

----
[toc]

<div class="div-border-answer">
分布式采集拉钩网中杭州爬虫相关职位的数据并使用Flask进行数据的可视化与分析
</div>


## 写在前面
<div class="div-border-answer">
来北京3年多了，这3年来，经历了很多了，成长了很多，领悟了许多，也看懂了很多，但是居京都大不易，来北京之前也没有
考虑过在北京定居这个想法，现在也依然没有，即便我有能力在这里定居，我也不会在这里定居，原因就是我不喜欢这个城市
，这里太过于喧嚣，太过于吵闹，就像唐寅那句，‘车尘马足富者趣，酒盏花枝贫者缘。’，北京，于我来说，终究是个临时的
泊岗，而我于北京，终究是个过客，既然迟早要离开，而现在又赶上现在的这样的一个机会，所以，再见，北京。
</div>

## 项目概述

<div class="div-border-question">
好了，说回这个项目，因为之前一直做的是数据采集的相关的工作，以前是通过SDK的方式来采集数据，由于工作的需要，便学习了
网络爬虫，从刚刚开始的定向爬虫，到后来的多机分布式爬虫，定时服务化爬虫，可视化爬虫，在爬虫的使用上，还是有丰富的经验的
现在要离开北京，去杭州了，主要想要从数据采集相关的工作，所以便萌生了一个想法，用爬虫，爬取以下有关数据采集的相关数据，
并进行一下分析，在用 `Flask` 进行一下可视化，为啥要选Flask那，因为它轻啊，`Django` 太过于繁重了，用于中级以上的项目来说是个不
错的选择，但是对于个人来说，Flask是个不二的选择。
</div>

## 项目结构

* 在整体结构上涉及三个部分，
   * 数据采集
   * 数据存储
   * 数据分析与可视化

### 数据采集
 在数据采集上，准备使用 `Scrapy-Redis`和`Redis`来实现多机器分布爬取,目标网站是拉钩网，由于拉钩网的反爬
 还是比较严厉的，所以需要进行一下防ban的操作，具体的实现我会写在下面

### 数据存储
 在数据存储上，前期分析了一下，数据大约几百条，不到1000条，所以就不用需要分布式存储了，直接用`MySQL`或者是`MongDB`存储一下就好了，
 可以先把数据同步在`Redis`中，然后在写个脚本直接从`Redis`同步到MySQL中，就不考虑`Redis`磁盘存储了，或者直接放在磁盘上，就不放在内存中了，
 也方便`Flask`使用。  

### 数据分析与可视化
 在数据可视化上，准备使用`Flask`来实现一个`WebServer`,因为Flask比较轻，所以我非常喜欢`Flask`，基于插件，想要什么功能
 直接用插件来实现即可。用`Flask`来进行数据的可视化，可以分析一下，杭州各个区的数据采集相关的职位数量，薪资和工作年限的分布清空
 或者统计一下，在任职需求中出现频率最高的词汇 Top10等等
 
 ### 补充说明
  最近接触了一个非常不错的文档在线生成工具，[docsify](https://docsify.js.org/#/),这个工具非常的不错，使用GitHubPage可以直接完成部署的工作，非常方便，vue风格的界面非常美观
  对于我这种经常写文档的同学来说，简直是天大的福音。我的这个项目，会提供一份说明文档。就使用这个 [docsify](https://docsify.js.org/#/)来实现，
  最后会呈现在[LaGou-Distributed-Spider-Flask项目说明文档](https://bruceju.github.io/LaGou-Distributed-Spider-Flask/)

