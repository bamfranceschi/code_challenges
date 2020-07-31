function almostIncreasingSequence(sequence) {
  let count = 0;
  for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] <= sequence[i - 1]) {
      count++;
      // check if more than one nonincreasing is found in the count (we can only remove one)
      if (count > 1) {
        return false;
      }
      // check if second previous number is equal to or bigger than the current numer
      // and check if the previous number is equal to or bigger than the next number
      // if it is not then it is false
      if (
        sequence[i] <= sequence[i - 2] &&
        sequence[i + 1] <= sequence[i - 1]
      ) {
        return false;
      }
    }
  }
  // otherwise return true
  return true;
}
