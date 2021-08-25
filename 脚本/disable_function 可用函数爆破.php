<?php
$arr = get_defined_functions()['internal'];

foreach ($arr as $key => $value) {
    if ( preg_match('/[\x00- 0-9\'"`$&.,|[{_defgops\x7F]+/i', $value) ){
        unset($arr[$key]);
        continue;
    }

    if ( strlen(count_chars(strtolower($value), 0x3)) > 0xd ){
        unset($arr[$key]);
        continue;
    }
}

var_dump($arr);
?>

//结果如下
array(18) {
  [55]=>
  string(5) "bcmul"
  [416]=>
  string(5) "rtrim"
  [422]=>
  
      ......