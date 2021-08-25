<?php
$l = "";
$r = "";
$argv = str_split("_GET");
for($i=0;$i<count($argv);$i++)
{
    for($j=0;$j<255;$j++)
    {
        $k = chr($j)^chr(255);
        if($k == $argv[$i]){
            if($j<16){
                $l .= "%ff";
                $r .= "%0" . dechex($j);
                continue;
            }
            $l .= "%ff";
            $r .= "%" . dechex($j);
            continue;
        }
    }
}
echo "\{$l`$r\}";
?>