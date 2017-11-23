title: Hesdfsrld
date: 2022-06-21
tags: [general, awesome, stuff]

### 3. 流量限制与请求限制


#### 【模块】limit_conn

[Ref: limit_conn](http://nginx.org/en/docs/http/ngx_http_limit_conn_module.html)

- 设置连接限制共享池

:::
Syntax:	limit_conn_zone key zone=name:size;
Default:	—
Context:	http
:::

#### sample

:::
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
:::

- 懂的

:::sh
netstat -an | grep 18848| awk '/^tcp/{++S[$NF]} END {for(a in S) print a, S[a]}'
:::