#!/usr/bin/php -q
<?php
passthru('clear');

$sumofSquare = 0;
for ($i = 1; $i <= 100; $i++){
	$sumofSquare += ($i * $i);
}
echo $sumofSquare . "\n";

$squareofSum = 0;
for ($j = 1; $j <= 100; $j++){
	$squareofSum += $j;
}
$squareofSum *= $squareofSum;
echo $squareofSum . "\n";

$difference = $squareofSum - $sumofSquare;
echo "Difference: " . $difference . "\n";
?>
