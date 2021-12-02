<?php

function open_file($input_file) {
  $lines = file($input_file);
  return $lines;
}

function part_one($input_file) {
  $directions = open_file($input_file);
  $horizontal_position = 0;
  $depth = 0;
  foreach ($directions as $line) {
    if (str_contains($line, "forward")) {
      $x = trim($line, "forward");
      $horizontal_position += $x;
      // echo "$x, $horizontal_position";
    } elseif (str_contains($line, "down")) {
      $x = trim($line, "down");
      $depth += $x;
      // echo "$x, $depth";
    } elseif (str_contains($line, "up")) {
      $x = trim($line, "up");
      $depth -= $x;
      // echo "$x, $depth";
    } return $horizontal_position * $depth;
}

// function part_two($input_file) {
//   $directions = open_file($input_file);
//   $horizontal_position = 0;
//   $depth = 0;
//   foreach ($directions as $line) {
//     if (str_contains($line, "forward")) {
//       $x = (int)(trim($line, "forward"));
//       $horizontal_position += $x;
//       // echo "$x, $horizontal_position";
//     } elseif (str_contains($line, "down")) {
//       $x = (int)(trim($line, "down"));
//       $depth += $x;
//       // echo "$x, $depth";
//     } elseif (str_contains($line, "up")) {
//       $x = (int)(trim($line, "up"));
//       $depth -= $x;
//       // echo "$x, $depth";
//     } return ($horizontal_position * $depth);
// }
// //output result

// $part_one_answer = "hi";

$part_one_answer = part_one("input.txt");
// $part_two_answer = part_two("input.txt");

var_dump($part_one_answer);
echo "Answer #1 = $part_one_answer";
//
// var_dump($part_two_answer);
// echo "Answer #2 = $part_two_answer";

?>
