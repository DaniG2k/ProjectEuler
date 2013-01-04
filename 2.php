#!/usr/bin/php -q
<?php

$fib = 0;
$n1 = 1;
$n2 = 0;
$sum = 0;

while($fib <= 4000000){
	$n2 = $fib + $n1;
	$fib = $n1;
	$n1 = $n2;
	
	if( $fib % 2 == 0) {
		echo $fib." is an even term!!!\n";
		$sum += $fib;
	} else {
		echo $fib."\n";
	}
}

echo "\nThe sum of all even terms is: ".$sum."\n";

?>
