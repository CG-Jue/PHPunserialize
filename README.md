# php反序列化自动分析

> 一步步尝试实现CTF中php反序列化的自动分析

## 先来个基础的php结构分析
```php
<?php
class leiming {
    public $name;
    public function __construct($name) {
        $this->name = $name;
    }
}

if (isset($_GET['data'])) {
    highlight_file(__FILE__);
    unserialize(base64_decode($_GET['data']));
}
```

## TodoList
1. 先把源码转化为AST存储
- [x] 把 PHP源码以json格式存储 PHPToJson
2. 对代码进行分析
    - ~~方案一：直接用ast中的数据~~
    - 方案二：把ast中不需要的数据去掉，只保留类名、方法名、参数名、变量名等
- [x] 获取其中的每一个类    getClass
- [ ] 对每一个类进行处理    processClass
    - [ ] Method处理      handleMethod

