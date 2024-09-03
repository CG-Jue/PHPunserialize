<?php
highlight_file(__FILE__);
error_reporting(0);

class re{
    public $chu0;
    public function __toString(){
        if(!isset($this->chu0)){
            return "I can not believes!";
        }
        $this->chu0->$nononono;
    }
}

class web {
    public $kw;
    public $dt;

    public function __wakeup() {
        echo "lalalla".$this->kw;
    }

    public function __destruct() {
        echo "ALL Done!";
    }
}

class pwn {
    public $dusk;
    public $over;

    public function __get($name) {
        if($this->dusk != "gods"){
            echo "什么，你竟敢不认可?";
        }
        $this->over->getflag();
    }
}

class Misc {
    public $nothing;
    public $flag;

    public function getflag() {
        eval("system('cat /flag');");
    }
}

class Crypto {
    public function __wakeup() {
        echo "happy happy happy!";
    }

    public function getflag() {
        echo "you are over!";
    }
}
$ser = $_GET['ser'];
unserialize($ser);
?>