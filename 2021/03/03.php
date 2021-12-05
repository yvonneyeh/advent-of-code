<?php

function open_file($input_file) {
  return array_map(fn ($a) => str_split(trim($a)), file($input_file));
}

function part_one($input_file) {
  $file = open_file($input_file);
  $count_row = count($file);
  $bits = array_reduce($file, fn($a, $b) => array_map(fn(...$args) => array_sum($args), $a, $b), array());
  $gamma = implode('', array_map(fn($a) => (int) ($count_row - $a < $a), $bits));
  $epsilon = strtr($gamma, '01', '10');
  $power_consumption = bindec($gamma) * bindec($epsilon);
  return $power_consumption;
}

function part_two($input_file){
  $file = open_file($input_file);

  function find_rating(array $report, bool $bit) {
   $n = 0;
   while (count($report) > 1) {
     $count_row = count($report);
     $ones = array_sum(array_column($report, $n));
     $keep = (($count_row - $ones <= $ones) xor !$bit);
     $report = array_filter($report, fn($v) => $v[$n] == $keep);
     $n++;
   }
   return implode('', current($report));
  }

 $gamma = find_rating($file, 1);
 $epsilon = find_rating($file, 0);

 $power_consumption = bindec($gamma) * bindec($epsilon);
 return $power_consumption;
}


$part_one_answer = part_one("input.txt");
$part_two_answer = part_two("input.txt");

var_dump($part_one_answer);
echo "Answer #1 = $part_one_answer" . "\n";
// 3309596

var_dump($part_two_answer);
echo "Answer #2 = $part_two_answer" . "\n";
// 3309596
