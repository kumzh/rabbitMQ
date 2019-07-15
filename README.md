rabbitMQ
要求：
1、可以异步执行很多命令
2、对多台机器

例如：
>>:执行“df -h --hosts 192.168.1.1 192.168.2.2 ”
   返回task id：XXXX  XXXX     #执行命令时不会有阻塞，直接返回id
根据对应的task id可以找到对应的返回结果
>>:check_task XXXX

可以连续执行多条命令

