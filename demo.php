<?php
class leiming {
    public $name;
    public $age;
    public $method;
    public function __construct($name) {
        $this->name = $name;
        $this->age = 18;
        $this->method = new method();
    }
}

if (isset($_GET['data'])) {
    highlight_file(__FILE__);
    unserialize(base64_decode($_GET['data']));
}