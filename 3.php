#!/usr/bin/php -q
<?php
passthru('clear');

//multiply all prime numbers
//hit 600851475143
//return last multiplied value
$nonPrime = array();

for($nom = 1; $nom <= 40; $nom++){
	//echo $nom . ")\n";

	for($denom = 1; $denom <= $nom; $denom++){

		if ( $nom % $denom == 0 && $denom != 1 && $denom != $nom){
			//echo "\t" . $nom . " is not prime. Adding to array...\n";
			$nonPrime[] = $nom;
		}
	}
}
$nonPrime = array_unique( $nonPrime );
print_r ( $nonPrime );
?>
