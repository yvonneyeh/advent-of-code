<?php

// parse inputs to an integer array
$input = file('input.txt');
$depths = array_map('intval', $input);

// Exercise 1

// check each depth to see if the previous is smaller
// if so, add 1 to $increased counter
$increased = 0;
foreach ($depths as $key => $value) {
    if ($value < $depths[$key + 1]) {
        $increased++;
    }
}

//output result
var_dump($increased);
echo "There are $increased lines in the file that are higher than the previous line";
// int(1752)

// Exercise 2

# keep track of sum of 3 consecutive depths
# loop through all depths (-2)
# increase counter if sum of 3 depths greater than previous
$lines = count($input);
$increased2 = 0;
$previous_depth = $depths[0] + $depths[1] + $depths[2];

for ($i = 0; $i < $lines - 2; $i++) {
  $next_depth = $depths[$i] + $depths[$i + 1] + $depths[$i + 2];
  if ($i < $lines - 2 && $previous_depth < $next_depth) {
    $increased2++;
  }
  $previous_depth = $next_depth;
}

//output result
var_dump($increased2);
echo "There are $increased2 lines in the file that are higher than the previous line";
// int(1781)

?>
