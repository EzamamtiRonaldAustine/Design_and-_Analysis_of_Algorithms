// The pseudocode
// Start Program to Find the Biggest Number in an Array

//     Create an array of numbers: {1, 4, 76, 5, 82, 89, 16}
//     Find how many numbers are in the array and store that in a variable called array_size

//     Print: "This is the array we are checking: ["

//     For each number in the array, starting from the first to the last:
//         Print the number
//         If the number is not the last one in the array, also print a comma after it
//     End the array with a closing square bracket "]"

//     Print: "The total number of items in the array is: " followed by array_size

//     If the array has no numbers (array_size is 0):
//         Print: "Error: The array is empty"
//         Stop the program
//     Otherwise, continue

//     Assume the biggest number so far is the first one in the array, call it max_number

//     For each of the other numbers in the array, starting from the second one:
//         If the current number is bigger than max_number:
//             Set max_number to the current number
//             Print: "The new biggest number so far is: " followed by max_number

//     When all numbers have been checked, print: 
//     "The biggest number in the array is: " followed by max_number

// End Program


#include <stdio.h>

int main() {
    int arr[] = {1, 4, 76, 5, 82, 89, 16};
    int arr_size = sizeof(arr) / sizeof(arr[0]); // getting the size of the array

    printf("This is the array whose maximum element we are finding : [");
    
    //Iterating through each element of the array
    for(int i = 0; i < arr_size; i++) {
        printf("%d", arr[i]);
        
        //If this is not the last element, print a comma and space
        if(i < arr_size - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    printf("\n");
    printf("The size of the array is: %d\n", arr_size);
    printf("\n");

    if (arr_size <= 0) {
        printf("Error: This array is empty\n");
        return -1; // Returning an error code if the array is empty
    }

    int max_element = arr[0]; // Initialize max_element with the first element of the array

    // Iterating through the array starting from the second element that is starting from the value 4 in the array 
    for (int i = 1; i < arr_size; i++) {
        if (arr[i] > max_element) {
            max_element = arr[i]; // Update max_element if the current element is greater
            printf("The new maximum element is: %d\n", max_element);
        }
    }
    printf("\n");
    printf("The final maximum element in the array is: %d\n", max_element);

    return 0;
}
