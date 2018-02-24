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

### 登录认证

> 现在数据库有了，并且也可以用命令生成Admin角色了，那么就下了可以开始构建登录认证功能了

* 登录认证功能设计思路
  * SemanticUi构建前端页面
  * 使用蓝图构建项目结构
  * flask_wtf设计登录表单
  * 提供登录验证的装饰器
  * 提供消息闪现支持



   
    
   
      
 

