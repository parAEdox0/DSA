function linearSearch(array, target) {
    // Iterate over each element in the array
    for (let index = 0; index < array.length; index++) {
      // Check if the current element matches the target
      if (array[index] === target) {
        // If a match is found, return the current index
        return index;
      }
    }
    // If the loop completes without finding the target, return -1
    return -1;
  }
  
  // Example usage:
  const numbers = [10, 20, 30, 40, 50];
  const target = 30;
  const result = linearSearch(numbers, target);
  
  if (result !== -1) {
    console.log(`Element found at index ${result}.`);
  } else {
    console.log('Element not found in the array.');
  }