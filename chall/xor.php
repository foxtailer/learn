<?php
function xor_encrypt($in, $key) {
    $outText = '';
    for ($i = 0; $i < strlen($in); $i++) {
        $outText .= $in[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

$base64 = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=";
$data = base64_decode($base64);

$key = '{"showpassword":"no","bgcolor":"#ffffff"}';

$encrypted = xor_encrypt($data, $key);

echo "Encrypted XOR Output (raw):\n";
echo $encrypted . "\n\n";
?>

