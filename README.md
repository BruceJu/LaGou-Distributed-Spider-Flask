
# LaGou-Distributed-Spider-Flask

## 简介
> * 采集招聘平台中杭州爬虫相关职位的数据并使用Flask进行数据的可视化与分析
> * 详细的实现步骤请查看[LaGou-Distributed-Spider-Flask项目实现纪实文档](https://bruceju.github.io/LaGou-Distributed-Spider-Flask/)

## 成果展示

### web服务
> 身份验证

<div style="fload:left,margin:30px,display:inline">
   <img src="https://s1.ax1x.com/2018/03/06/9gZh3F.png" width="800" />
</div>


> 分析页
<div style="fload:left,margin:30px,display:inline">
   <img src="https://s1.ax1x.com/2018/03/06/9gZTBR.png" width="800" />
</div>


### 数据分析

> 职位地区数量

<div style="fload:left,margin:30px,display:inline">
   <img src="https://s1.ax1x.com/2018/03/06/9gZbAx.png" width="800" />
</div>

> 学历要求占比

<div style="fload:left,margin:30px,display:inline">
   <img src="https://s1.ax1x.com/2018/03/06/9geQU0.png" width="800" />
</div>

> 职位描述词云

<div style="fload:left,margin:30px,display:inline">
   <img src="https://s1.ax1x.com/2018/03/06/9ge3CT.png" width="800" height="400" />
</div>

## 命令脚本設計

```python
usage: Manager.py [-?]
                  {db,runserver,runspider,create_admin,drop_all_db,shell} ...

positional arguments:
  {db,runserver,runspider,create_admin,drop_all_db,shell}
    db init
    db migrate
    db upgrade               
    runserver -p<port> -h<host>
    runspider
    create_admin -a<account> -p<password>
    drop_all_db
    shell    

```






