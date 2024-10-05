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