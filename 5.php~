#!/usr/bin/php -q
<?php
passthru('clear');
$time_start = microtime(true);
echo "Starting time count: $time_start\n";
$range = array(1,2,3,4,5,
				6,7,8,9,10,
				11,12,13,14,15,
				16,17,18,19,20);
$counter = 1;
while ( true ){
	if ($counter % 1000000 == 0 ) echo $counter . "\n";

	foreach ($range as $num){ 			// For each number in the array from 1-10

		if ( $counter % $num == 0 ){	// If it's evenly divisible

			if ( $num == count($range) ) {
				echo "\$num is " . $num . "\n";
				echo "\$counter is " . $counter . "\n";
				echo "Success!\n";
				$time_end = microtime(true);
				echo "End time: $time_end\n";
				$total_time = $time_end - $time_start;
				echo "\nProgram execution time: $total_time\n";
				return false;
			}		
		} else {
			break;
		}
	}
	$counter++;
}
?>
