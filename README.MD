# 发送钓鱼邮件（简单几行Python即可实现<利用Telnet>）
无需建立服务器，稍作更改即可直接发送钓鱼电子邮件。

## 使用方式
更改SendPhishingEmail.py中执行函数的参数即可。

其中，

      第一个参数代表目标接收服务器地址；

      第二个参数代表发件人邮箱（伪造的发件人）；
      
      第三个参数代表收件人邮箱；
      
      第四个参数代表邮件主题；
      
      第五个参数代表邮件内容。

如：

    SendmailWithTelnet("mx.google.com", "UnknwonSecurity@UnknownSecurity.UnknownSecurity", "admin@unkn0wn.cn", "Miss You!","Now, I Miss You So Much!!!")


记得安装依赖。`pip install -r requirements.txt`

## 其他
[English Readme.md](https://github.com/UnknownU0/SendPhishingEmail/blob/main/Readme-en.md)
