# ifwechat


### ①.IFWechat能做什么

IFWechat是一个能把微信连接到IFTTT的微信公众号,如果你还不知道IFTTT是什么,可以看看这里:[ifttt 是一个什么样的网站？](http://www.zhihu.com/question/19739416).  
IFTTT = if this then that, IFWechat通过微信公众号实现了IFTTT中this的功能,通过微信发送到IFWechat的消息都会触发用户定义的IFTTT Recipes.  


## ②.绑定微信与IFTTT

1.关注IFWechat微信公众号

![qcode](http://7oti6o.com1.z0.glb.clouddn.com/boz-qcode.jpg)

2.生成IFTTT Maker Webhooks key

访问[IFTTT Maker Webhooks](https://ifttt.com/maker_webhooks)  
![IFTTT Maker Webhooks](http://picbang.qiniudn.com/bozmakerchannel.jpg)

点击**Connect**  
访问[Settings](https://ifttt.com/services/maker_webhooks/settings),复制URL后面的key  
![IFTTT Maker key](http://picbang.qiniudn.com/bozmakerchannel2.jpg)

3.绑定key到IFWechat微信公众号

![bind key](http://picbang.qiniudn.com/bozbind.jpg)

发送 BD+key 绑定.

## ③.绑定微信与IFTTT

1.发送文本消息

![text](http://7oti6o.com1.z0.glb.clouddn.com/bozsend1.png)

IFTTT Recipes示例:<https://ifttt.com/p/zhu327/shared>

2.发送照片消息

![image](http://7oti6o.com1.z0.glb.clouddn.com/bozsend2.png)

先发送图片,然后追加一条文本.

3.发送地理位置

![location](http://7oti6o.com1.z0.glb.clouddn.com/bozsend3.png)

4.发送分享链接

![link](http://7oti6o.com1.z0.glb.clouddn.com/bozsend4.png)

## ④.消息格式

上面有一些IFTTT Recipes示例,如果你有更好的创意,那么就需要了解下你发送给IFWechat公众号的消息会在推送给IFTTT的时候的消息格式.

Event Name: text

```javascript
{
    "value1": "Hello world" // value1为文本内容
}
```

Event Name: image

```javascript
{
    "value1": "", // value1为图片地址
    "value2": "Hello world" // value2为文本内容
}
```

Event Name: location

```javascript
{
    "value1": "深圳市罗湖区国贸", // value1为地理位置文本
    "value2": "", // value2为纬度
    "value3": "" // value3为经度
}
```

Event Name: link

```javascript
{
    "value1": "", // value1为分享链接地址
    "value2": "", // value2为分享标题
    "value3": "" // value3为分享描述
}
```
