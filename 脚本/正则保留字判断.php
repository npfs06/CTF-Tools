<?php
for ($i = 0; $i < 256; $i++) {
    if (!preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i))) {
        echo chr($i).' ';
    }
}
?>