title: Hello World
date: 2012-03-04
tags: [general, awesome, stuff]

# nginx完整心得笔记（内测不删档，送宝刀屠龙）

> 集天地之精华\
> 呕心吐血未完成\
> FIXME

[TOC]


## 一、功能点说明

### 1. 配置

#### 1.1 location

`location [=|~|~*|^~] /uri/ { … }`

|         模式         |                                     含义                                    |
|----------------------|-----------------------------------------------------------------------------|
| location = /uri      | = 表示精确匹配，只有完全匹配上才能生效                                      |
| location ^~ /uri     | ^~ 开头对URL路径进行前缀匹配，并且在正则之前。                              |
| location ~ pattern   | 开头表示***区分大小写***的【***正则***】匹配                                |
| location ~\* pattern | 开头表示***不区分大小写***的【***正则***】匹配                              |
| location /uri        | 不带任何修饰符，也表示前缀匹配，但是在正则匹配之后                          |
| location /           | 通用匹配，任何未匹配到其它location的请求都会匹配到，相当于switch中的default |

前缀匹配时，Nginx不对url做编码，因此请求为`/static/20%/aa`，可以被规则`^~ /static/ /aa`匹配到（注意是空格）

多个`location`配置的情况下匹配顺序为:

- 首先精确匹配 `=`
- 其次前缀匹配 `^~`
- 其次是按文件中顺序的正则匹配
- 然后匹配不带任何修饰的前缀匹配。
- 最后是交给 `/` 通用匹配
- 当有匹配成功时候，停止匹配，按当前匹配规则处理请求

**注意**：前缀匹配，如果有包含关系时，按最大匹配原则进行匹配。\
比如在前缀匹配：`location /dir01`与`location /dir01/dir02`，\
如有请求`http://localhost/dir01/dir02/file`将最终匹配到`location /dir01/dir02`

#### 1.2 你哪个单位的

- 空间单位

  k/K : KiloByte\
  m/M : MegaBye

- 时间单位

  ms : 毫秒\
  s  : 秒\
  m  : 分\
  h  : 时\
  d  : 天\
  M  : 月\
  y  ：年

### 2. nginx变量

[link:nginx变量](http://nginx.org/en/docs/varindex.html)

> 变态搞这么多，我也不造

```txt
$ancient_browser
$arg_
$args
$binary_remote_addr (ngx_http_core_module)
$binary_remote_addr (ngx_stream_core_module)
$body_bytes_sent
$bytes_received
$bytes_sent (ngx_http_core_module)
$bytes_sent (ngx_http_log_module)
$bytes_sent (ngx_stream_core_module)
$connection (ngx_http_core_module)
$connection (ngx_http_log_module)
$connection (ngx_stream_core_module)
$connection_requests (ngx_http_core_module)
$connection_requests (ngx_http_log_module)
$connections_active
$connections_reading
$connections_waiting
$connections_writing
# HTTP请求信息里的"Content-Length";
$content_length
$content_type
$cookie_
$date_gmt
$date_local
$document_root
$document_uri
$fastcgi_path_info
$fastcgi_script_name
$gzip_ratio
$host
$hostname (ngx_http_core_module)
$hostname (ngx_stream_core_module)
$http2
$http_
$https
$invalid_referer
$is_args
$jwt_claim_
$jwt_header_
$limit_rate
$memcached_key
$modern_browser
$msec (ngx_http_core_module)
$msec (ngx_http_log_module)
$msec (ngx_stream_core_module)
$msie
$nginx_version (ngx_http_core_module)
$nginx_version (ngx_stream_core_module)
$pid (ngx_http_core_module)
$pid (ngx_stream_core_module)
$pipe (ngx_http_core_module)
$pipe (ngx_http_log_module)
$protocol
$proxy_add_x_forwarded_for
$proxy_host
$proxy_port
$proxy_protocol_addr (ngx_http_core_module)
$proxy_protocol_addr (ngx_stream_core_module)
$proxy_protocol_port (ngx_http_core_module)
$proxy_protocol_port (ngx_stream_core_module)
$query_string
$realip_remote_addr (ngx_http_realip_module)
$realip_remote_addr (ngx_stream_realip_module)
$realip_remote_port (ngx_http_realip_module)
$realip_remote_port (ngx_stream_realip_module)
$realpath_root
$remote_addr (ngx_http_core_module)
$remote_addr (ngx_stream_core_module)
$remote_port (ngx_http_core_module)
$remote_port (ngx_stream_core_module)
$remote_user
$request
$request_body
$request_body_file
$request_completion
$request_filename
$request_id
$request_length (ngx_http_core_module)
$request_length (ngx_http_log_module)
$request_method
$request_time (ngx_http_core_module)
$request_time (ngx_http_log_module)
$request_uri
# request scheme, “http” or “https”
$scheme
$secure_link
$secure_link_expires
$sent_http_
$sent_trailer_
$server_addr (ngx_http_core_module)
$server_addr (ngx_stream_core_module)
$server_name
$server_port (ngx_http_core_module)
$server_port (ngx_stream_core_module)
$server_protocol
$session_log_binary_id
$session_log_id
$session_time
$slice_range
$spdy
$spdy_request_priority
$ssl_cipher (ngx_http_ssl_module)
$ssl_cipher (ngx_stream_ssl_module)
$ssl_ciphers (ngx_http_ssl_module)
$ssl_ciphers (ngx_stream_ssl_module)
$ssl_client_cert (ngx_http_ssl_module)
$ssl_client_cert (ngx_stream_ssl_module)
$ssl_client_escaped_cert
$ssl_client_fingerprint (ngx_http_ssl_module)
$ssl_client_fingerprint (ngx_stream_ssl_module)
$ssl_client_i_dn (ngx_http_ssl_module)
$ssl_client_i_dn (ngx_stream_ssl_module)
$ssl_client_i_dn_legacy
$ssl_client_raw_cert (ngx_http_ssl_module)
$ssl_client_raw_cert (ngx_stream_ssl_module)
$ssl_client_s_dn (ngx_http_ssl_module)
$ssl_client_s_dn (ngx_stream_ssl_module)
$ssl_client_s_dn_legacy
$ssl_client_serial (ngx_http_ssl_module)
$ssl_client_serial (ngx_stream_ssl_module)
$ssl_client_v_end (ngx_http_ssl_module)
$ssl_client_v_end (ngx_stream_ssl_module)
$ssl_client_v_remain (ngx_http_ssl_module)
$ssl_client_v_remain (ngx_stream_ssl_module)
$ssl_client_v_start (ngx_http_ssl_module)
$ssl_client_v_start (ngx_stream_ssl_module)
$ssl_client_verify (ngx_http_ssl_module)
$ssl_client_verify (ngx_stream_ssl_module)
$ssl_curves (ngx_http_ssl_module)
$ssl_curves (ngx_stream_ssl_module)
$ssl_preread_server_name
$ssl_protocol (ngx_http_ssl_module)
$ssl_protocol (ngx_stream_ssl_module)
$ssl_server_name (ngx_http_ssl_module)
$ssl_server_name (ngx_stream_ssl_module)
$ssl_session_id (ngx_http_ssl_module)
$ssl_session_id (ngx_stream_ssl_module)
$ssl_session_reused (ngx_http_ssl_module)
$ssl_session_reused (ngx_stream_ssl_module)
$status (ngx_http_core_module)
$status (ngx_http_log_module)
$status (ngx_stream_core_module)
$tcpinfo_rtt
$tcpinfo_rttvar
$tcpinfo_snd_cwnd
$tcpinfo_rcv_space
$time_iso8601 (ngx_http_core_module)
$time_iso8601 (ngx_http_log_module)
$time_iso8601 (ngx_stream_core_module)
$time_local (ngx_http_core_module)
$time_local (ngx_http_log_module)
$time_local (ngx_stream_core_module)
$uid_got
$uid_reset
$uid_set
$upstream_addr (ngx_http_upstream_module)
$upstream_addr (ngx_stream_upstream_module)
$upstream_bytes_received (ngx_http_upstream_module)
$upstream_bytes_received (ngx_stream_upstream_module)
$upstream_bytes_sent
$upstream_cache_status
$upstream_connect_time (ngx_http_upstream_module)
$upstream_connect_time (ngx_stream_upstream_module)
$upstream_cookie_
$upstream_first_byte_time
$upstream_header_time
$upstream_http_
$upstream_response_length
$upstream_response_time
$upstream_session_time
$upstream_status
$uri
```

### 3. 流量限制与请求限制


#### 【模块】limit_conn

[Ref: limit_conn](http://nginx.org/en/docs/http/ngx_http_limit_conn_module.html)

- 设置连接限制共享池

```
Syntax:	limit_conn_zone key zone=name:size;
Default:	—
Context:	http
```

- 共享池中某个key为连接的最大的连接数

```
Syntax:  limit_conn zone number;
Default: —
Context: http, server, location
```

Sets the shared memory zone and the maximum allowed number of connections for a given key value. When this limit is exceeded, the server will return the error in reply to a request. For example, the directives

#### 【模块】limit_rate

[Ref: limit_rate*](http://nginx.org/en/docs/http/ngx_http_core_module.html#limit_rate)

```
Syntax:	limit_rate rate;
Default:
limit_rate 0;
Context:	http, server, location, if in location
```
Limits the rate of response transmission to a client. The rate is specified in bytes per second. The zero value disables rate limiting. The limit is set per a request, and so if a client simultaneously opens two connections, the overall rate will be twice as much as the specified limit.

```
Syntax:	limit_rate_after size;
Default:
limit_rate_after 0;
Context:	http, server, location, if in location
This directive appeared in version 0.8.0.
```

Sets the initial amount after which the further transmission of a response to a client will be rate limited.


#### 【模块】limit_req

[Ref: limit_req](http://nginx.org/en/docs/http/ngx_http_limit_req_module.html)

```
Syntax:	limit_req zone=name [burst=number] [nodelay];
Default:	—
Context:	http, server, location
```

Sets the shared memory zone and the maximum burst size of requests. If the requests rate exceeds the rate configured for a zone, their processing is delayed such that requests are processed at a defined rate. Excessive requests are delayed until their number exceeds the maximum burst size in which case the request is terminated with an error. By default, the maximum burst size is equal to zero.

```
Syntax:	limit_req_zone key zone=name:size rate=rate;
Default:	—
Context:	http
```

Sets parameters for a shared memory zone that will keep states for various keys. In particular, the state stores the current number of excessive requests. The key can contain text, variables, and their combination. Requests with an empty key value are not accounted.


#### sample

```
# 以对端ip作为key
limit_conn_zone  $binary_remote_addr  zone=ConnIP:10m;
# 以服务端ip作为key
limit_conn_zone  $server_name         zone=ConnServer:10m;

# 以对端ip作为key，限速5条/秒
limit_req_zone   $binary_remote_addr  zone=ReqIP:10m     rate=5r/s;
# 以服务端ip作为key，限速20条/秒
limit_req_zone   $server_name         zone=ReqServer:10m rate=20r/s;


server {
    listen 22223;

    location /test_limit {

        # 某个IP来源的请求同时只能1个
        limit_conn ConnIP 1;
        # 服务端只接受最大100个连接
        limit_conn ConnServer 100;

        # 限流速
        limit_rate 100k;
        limit_rate_after 10M;

        # 限请求频率
        limit_req zone=ReqIP burst=30 nodelay;
        limit_req zone=ReqServer burst=40;
    }
}
```

- 懂的

```sh
netstat -an | grep 18848| awk '/^tcp/{++S[$NF]} END {for(a in S) print a, S[a]}'
```

### 4. 限制ip

#### 【模块】deny/allow

[Ref: deny/allow](http://nginx.org/en/docs/http/ngx_http_access_module.html)


```
Syntax:	allow address | CIDR | unix: | all;
Default:	—
Context:	http, server, location, limit_except
```

```
Syntax:	deny address | CIDR | unix: | all;
Default:	—
Context:	http, server, location, limit_except
```

#### sample

```
deny 10.3.4.15;
allow 10.3.4.0/24;
allow 10.3.7.246;
deny all;
```

### 5. 日志记录

```
# access日志输出字段格式
log_format  pxylog '{{$remote_addr}} - {{$remote_user}} - {{$time_local}} - '
                   '{{$request}} - {{$status}} - {{$body_bytes_sent}} - '
                   '{{$http_referer}} - {{$http_user_agent}} - '
                   '{{$http_x_forwarded_for}} - {{$request_body}} - '
                   '{{$resp_body}}';


access_log logs/name_access.log pxylog;

#########################################################################

# Context:server, server

lua_need_request_body on;
set $resp_body "";
body_filter_by_lua '
    local resp_body = string.sub(ngx.arg[1], 1, 1000)
    ngx.ctx.resp_body_buf = (ngx.ctx.resp_body_buf or "") .. resp_body
    if ngx.arg[2] then
        ngx.var.resp_body = ngx.ctx.resp_body_buf
    end
';
```

`log_format` 是日志格式。可以使用nginx内置变量记录。

上例的`resp_body`不是内置变量，可以用lua脚本捕捉，这样就可以记录一条请求的请求与应答。



### 6. 反代代理

```
upstream ngccserver {
    server 127.0.0.1:30021;
    server 127.0.0.1:30022;
}

server {
    listen 30001;
    server_name localhost;

    # 写法1
    location /ismp/ngcc/qryorderrecord {
        proxy_pass http://ngccserver$uri;

        proxy_buffering off;
        proxy_pass_request_headers on;
        proxy_pass_request_body on;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # 写法2
    location /ismp/ngcc/qryspinfo {
        access_log logs/ngcc/qryspinfo_access.log pxylog;
        error_log  logs/ngcc/qryspinfo_error.log;

        proxy_pass http://192.168.1.1:12345/$uri;

        proxy_buffering off;
        proxy_pass_request_headers on;
        proxy_pass_request_body on;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

#### sample

- 使用ngx代理的抓包报文（http头）

```http
POST /IsmpCrmEngine HTTP/1.0
Host: 10.3.4.208
X-Real-IP: 10.3.4.14
REMOTE-HOST: 10.3.4.14
X-Forwarded-For: 10.3.4.14
Connection: close
Content-Length: 1170
Content-Type: text/xml; charset=utf-8
SOAPAction: ""
```

- 未使用代理的抓包报文（http头）

```http
POST /IsmpCrmEngine HTTP/1.0
Host: 10.3.4.201:7031
Content-Type: text/xml; charset=utf-8
Content-Length: 1170
SOAPAction: ""
```

### 7. 【模块】rewrite

==FIXME==

==智商不够字数来凑(o_O)==

[Ref: rewrite](http://nginx.org/en/docs/http/ngx_http_rewrite_module.html)

```
Syntax:	rewrite regex replacement [flag];
Default:	—
Context:	server, location, if
```

|    flag   |                                                                   说明                                                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| last      | stops processing the current set of ngx_http_rewrite_module directives and starts a search for a new location matching the changed URI; |
| break     | stops processing the current set of ngx_http_rewrite_module directives as with the break directive;                                     |
| redirect  | returns a temporary redirect with the 302 code; used if a replacement string does not start with “http://”, “https://”, or “$scheme”;   |
| permanent | returns a permanent redirect with the 301 code.                                                                                         |


### 8. 【模块】proxy_redirect

[Ref: proxy_redirect](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_redirect)

```
Syntax:	proxy_redirect default;
proxy_redirect off;
proxy_redirect redirect replacement;
Default:
proxy_redirect default;
Context:	http, server, location
```

Sets the text that should be changed in the “Location” and “Refresh” header fields of a proxied server response.

当上游服务器应答是重定向时，可以修改报文头（HTTP协议）中的`Location`和`Refresh`值


#### sample

- 实践

替换原有重定向地址，重写为hello

```
port_in_redirect on;
proxy_redirect ~^(http://[^:]+):\d+(/.+)$ $scheme://hello;
```

最终抓包得到的头

```
HTTP/1.1 302 Found
Server: openresty
Date: Fri, 10 Nov 2017 07:18:55 GMT
Content-Type: text/html;charset=utf-8
Content-Length: 0
Connection: keep-alive
Set-Cookie: JSESSIONID=F058FA13F96DFE294693A4D90BB005F9; Path=/AMS_HN; HttpOnly
Location: http://hello
```

```sh
##########
# before #
##########
[sbeamer ~]$ curl -I http://cdserver:64000/AMS_HN
HTTP/1.1 302 Found
Server: openresty
Date: Fri, 10 Nov 2017 07:14:21 GMT
Connection: keep-alive
Location: http://cdserver:8088/AMS_HN/

#########
# after #
#########
[sbeamer ~]$ curl -I http://cdserver:64000/AMS_HN
HTTP/1.1 302 Found
Server: openresty
Date: Fri, 10 Nov 2017 07:22:33 GMT
Connection: keep-alive
Location: http://hello
```

### 9. 【模块】port_in_redirect

[Ref: port_in_redirect](http://nginx.org/en/docs/http/ngx_http_core_module.html#port_in_redirect)

```
Syntax:	port_in_redirect on | off;
Default:
port_in_redirect on;
Context:	http, server, location
```

Enables or disables specifying the port in absolute redirects issued by nginx.

The use of the primary server name in redirects is controlled by the server_name_in_redirect directive.

重定向时是否允许指定端口。

* on（默认），按监听的端口转发

* off，始终按照默认的80端口转发。


#### sample

- 实践

```
port_in_redirect off;
```

访问 `http://cdserver:64000/AMS_HN/`

重定向之后跳转到了 `http://cdserver/AMS_HN/`，端口变成80。

```
HTTP/1.1 302 Found
Server: openresty
Date: Fri, 10 Nov 2017 07:54:34 GMT
Content-Type: text/html;charset=utf-8
Content-Length: 0
Location: http://cdserver/AMS_HN
Connection: keep-alive
Set-Cookie: JSESSIONID=79D0B6FF7584FBD324D12989859A7FE7; Path=/AMS_HN; HttpOnly
```

### 10. 【模块】server_name_in_redirect

[Ref: server_name_in_redirect](http://nginx.org/en/docs/http/ngx_http_core_module.html#server_name_in_redirect)

```
Syntax:	server_name_in_redirect on | off;
Default:
server_name_in_redirect off;
Context:	http, server, location
```

Enables or disables the use of the primary server name, specified by the server_name directive, in absolute redirects issued by nginx. When the use of the primary server name is disabled, the name from the “Host” request header field is used. If this field is not present, the IP address of the server is used.

The use of a port in redirects is controlled by the port_in_redirect directive.

设置重定向的Location是完整的URL还是URI

==[FIXME]== 未实践成功

* on（默认），url重定向为`server_name`中的第一个+`目录名`+`/`;

* off，url重定向为`原域名`+`目录名`+`/`;


## 二、强悍的lua

[lua-nginx-module](https://github.com/openresty/lua-nginx-module#readme)库由[openresty](http://openresty.org/)作者**章亦春**[[牛得惊动党中央](https://www.zhihu.com/question/28951394)]开发，也是`openresty`的组成部分。

> 信春哥得永生！

该模块让nginx使用者从需要写ngx库中解放出来，只需要动动手指头敲几行lua脚本就能实现各种业务功能，培养了一群拿来主义却又高效的懒汉。

> 涉世未深，不太了解lua与luajit之间的战争

[一个5.3版本的中文lua手册](http://www.runoob.com/manual/lua53doc/manual.html)

过于丰富，无从下口

## 三、备忘录

### 1. 重写rewrite

[link:参考](http://www.ttlsa.com/nginx/nginx-rewriting-rules-guide/)

- 修改url结尾的`/`

```nginx
# 向URL结尾添加"/"
# http://host/apple => http://host/apple/
rewrite ^(.*[^/])$ $1/ permanent;


# 删除URL结尾的"/"，尽量避免此操作
# http://host/banana/ => http://host/banana
rewrite ^/(.*)/$ /$1 permanent;
```

### 2. 日志

- 彻底关闭access.log

```nginx
access_log off;
```

### 3. 隐藏nginx版本

```nginx
# http {}
server_tokens off;
```

### 4. 需要登陆认证


#### 【模块】auth_basic

[Ref: auth_basic](http://nginx.org/en/docs/http/ngx_http_auth_basic_module.html)

```
Syntax:	auth_basic string | off;
Default:
auth_basic off;
Context:	http, server, location, limit_except
```

Enables validation of user name and password using the “HTTP Basic Authentication” protocol. The specified parameter is used as a realm. Parameter value can contain variables (1.3.10, 1.2.7). The special value off allows cancelling the effect of the auth_basic directive inherited from the previous configuration level.

---

```
Syntax:	auth_basic_user_file file;
Default:	—
Context:	http, server, location, limit_except
```

Specifies a file that keeps user names and passwords, in the following format:

- comment

```
name1:password1
name2:password2:comment
name3:password3
```

---

认证文件需要使用apache的htpasswd加密生成

当然万能的openssl也能胜任

```shell
printf "UserName:$(openssl passwd -crypt YourPassword)\n" > htpasswd_file
```

### 5. 目录浏览

#### 【模块】autoindex

[Ref: autoindex](http://nginx.org/en/docs/http/ngx_http_autoindex_module.html)

```nginx
# 默认off不允许浏览目录
autoindex on;

# 显示文件确切大小，off时以gb,mb,kb为单位显示
autoindex_exact_size on|off;

# 显示服务器时间或utc时间，默认off
autoindex_localtime on;

# 以什么格式显示。默认html
#autoindex_format html | xml | json | jsonp;

alias /home/user/dir;
```

#### 【三方插件】fancy_index

[Ref: 美化插件-fancy_index](https://www.nginx.com/resources/wiki/modules/fancy_index/)

注：facy_index_footer file

无路径表示当前目录，如 a.html，意思就是每一级访问目录下的a.html。

带路径表示root目录，如/h/a.html


虚拟目录`alias`, `root`

```nginx
# 使用alias
local /apple {
    autoindex on;
    alias /home/data/apple;
}
# 使用root
local /apple {
    autoindex on;
    root /home/data;
}
```

区别在于，用alias相当于ln软连接，访问的路径对应uri
而root的uri是需要拼接到路径后的。


### 6. 处理302，301跳转url跳转的解决办法

```nginx
server {
    listen 8088;
    server_name 182.148.107.198;
    server_name 10.3.4.208;
    # server_name_in_redirect on;

    # 这里需要设置，避免302，301跳转导致url变化
    # 【FIXME】还需要深入研究
    proxy_redirect http:// $scheme://;
    port_in_redirect on;

    access_log logs/tomcat_access.log;
    error_log  logs/tomcat_error.log error;

    location / {
        root   html;
        index  index.html index.htm;
    }

    location /sh_rest {
        proxy_pass http://10.3.4.208:8180;

        proxy_buffering             off;
        proxy_pass_request_headers  on;
        proxy_pass_request_body     on;
        proxy_set_header            Host $host:$server_port;
        proxy_set_header            Host $host;
        proxy_set_header            X-Real-IP $remote_addr;
        proxy_set_header            REMOTE-HOST $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # rewrite修改
    # 访问http://server/ismp/download
    # 代理到http://10.3.4.208:8000
    # 将"ismp/download"通过rewrite修改为"/"达到访问代理的目的
    location /ismp/download/ {
        auth_basic "天王盖地虎";
        auth_basic_user_file htpasswd;
        autoindex on;

        rewrite ^/ismp/download/(.*)$ /$1 break;
        proxy_pass http://10.3.4.208:8000;

        proxy_buffering             off;
        proxy_pass_request_headers  on;
        proxy_pass_request_body     on;
        proxy_set_header            Host $host:$server_port;
        proxy_set_header            Host $host;
        proxy_set_header            X-Real-IP $remote_addr;
        proxy_set_header            REMOTE-HOST $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### 7. 设置字符集

```
server {
    charset utf-8;
    # charset gb2312;
}
```

