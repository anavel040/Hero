<?php
$ip = $_SERVER['REMOTE_ADDR'];
$username = $_GET['username'];

$logEntry = $username . " : " . $ip . PHP_EOL;

file_put_contents("log.txt", $logEntry, FILE_APPEND);

echo "Dirección IP guardada en el registro.";
?>
