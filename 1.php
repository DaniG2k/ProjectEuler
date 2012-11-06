#!/usr/bin/php -q
<?php

$sum = 0;

	for( $i = 0; $i < 1000; $i++){

		if( $i % 3 == 0 || $i % 5 == 0){
			echo $i."\n";
			$sum += $i;
		}
	}
echo $sum."\n";
?>
