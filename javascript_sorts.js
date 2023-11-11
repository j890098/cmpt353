const fs = require('fs');

// Function to generate a random array of a given size
function generateRandomArray(size) {
  return Array.from({ length: size }, () => Math.floor(Math.random() * 1000));
}

// Function to measure the performance of a sorting algorithm
function measureSortingPerformance(sortFunction, array) {
  const start = performance.now();
  sortFunction(array.slice()); // Clone the array to avoid modifying the original
  const end = performance.now();
  return end - start; // Time in milliseconds
}

// Function to run sorting algorithms N times and return an array of performance measurements
function runSortingAlgorithms(N, Arr_size) {
  const results = [];

  for (let i = 0; i < N; i++) {
    const array = generateRandomArray(Arr_size);
    // Measure the performance of different sorting algorithms
    const bubbleSortTime = measureSortingPerformance(builtinSort, array);
    const mergeSortTime = measureSortingPerformance(mergeSort, array);
    const quickSortTime = measureSortingPerformance(quickSort, array);
    console.log([bubbleSortTime, mergeSortTime, quickSortTime])
    results.push([bubbleSortTime, mergeSortTime, quickSortTime]);
  }

  return results;
}

// Sorting algorithms (you can replace these with your preferred algorithms)
function builtinSort(arr) {
  // Implementation of bubble sort
  return arr.sort()
}

function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  // Split the array into two halves
  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle);

  // Recursively sort each half
  const leftSorted = mergeSort(left);
  const rightSorted = mergeSort(right);

  // Merge the sorted halves
  return merge(leftSorted, rightSorted);
}

function merge(left, right) {
  let result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  // Compare elements and merge into the result array
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  // Concatenate any remaining elements from both arrays
  return result.concat(left.slice(leftIndex), right.slice(rightIndex));
}
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  // Choose a pivot element
  const pivot = arr[Math.floor(arr.length / 2)];

  // Partition the array into two sub-arrays based on the pivot
  const left = arr.filter(element => element < pivot);
  const middle = arr.filter(element => element === pivot);
  const right = arr.filter(element => element > pivot);

  // Recursively sort the left and right sub-arrays
  return quickSort(left).concat(middle, quickSort(right));
}

// Function to write the results to a CSV file
function writeResultsToCSV(results) {
  const header = 'javascript_builtin, javascript_mergesort, javascript_quicksort\n';
  const csvData = results.map(row => row.join(',')).join('\n');
  const csvContent = header + csvData;

  fs.writeFileSync('javascript_data.csv', csvContent, 'utf8');
}

// Read input from a txt file
const inputFile = fs.readFileSync('parameters.txt', 'utf8');
const [N, Arr_size] = inputFile.trim().split(' ').map(Number);

// Run sorting algorithms and measure performance
const performanceResults = runSortingAlgorithms(N, Arr_size);

// Write the results to a CSV file
writeResultsToCSV(performanceResults);
