<?php
function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=";
$data = '{"showpassword":"no","bgcolor":"#ffffff"}';
$data2 = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
$key = 'eDWo';

echo xor_encrypt($data, base64_decode($cookie)) . "\n";
echo xor_encrypt(base64_decode($cookie), $data) . "\n";
echo base64_encode(xor_encrypt($data2, 'eDWo')) . "\n";
?>

