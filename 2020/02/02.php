<?php

function open_file($input_file) {
  return array_filter(array_map('trim', file($input_file)));
}

function part_one($input_file) {
  $lines = open_file($input_file);

  function isValid($min, $max, $letter, $password) {
    $number = substr_count($password, $letter);
    if ($number >= $min && $number <= $max) {
      return true;
    }
    return false;
  }

  $count = 0;
  foreach ($lines as $line) {
    preg_match('/^(\d+)-(\d+) (\w+): (\w+)$/', $line, $m);
    if (isValid($m[1], $m[2], $m[3], $m[4])) {
      $count++;
    }
  }
  echo "There are $count valid passwords\n";
  return $count;
}


function part_two($input_file) {
  $lines = open_file($input_file);
}




$part_one_answer = part_one("input.txt");
$part_two_answer = part_two("input.txt");

var_dump($part_one_answer);
echo "Answer #1 = $part_one_answer" . "\n";

var_dump($part_two_answer);
echo "Answer #2 = $part_two_answer" . "\n";

?>
