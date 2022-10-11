#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

typedef enum
{
    SUCCESS = 0,
    ERROR_NULL_POINTER = 1
} error_types;

uint32_t Convert_to_25fpp_representation(uint32_t PCx_reading, double *value)
{
    // Check if value is a nullptr
    if (value == NULL)
    {
        return ERROR_NULL_POINTER;
    }

    // Initialize vars
    uint32_t quotient = PCx_reading;
    int i, remainder, integer = 0, power = 6;
    double mantissa = 0.0;

    // Create empty array
    int input[33];
    for (i = 0; i < 32; i++)
    { // loop ends with i = 32
        input[i] = 0;
    }

    // Store input in array
    while (quotient > 0)
    {
        remainder = quotient % 2;
        quotient /= 2;
        input[--i] = remainder; // start at index 31, decrement
    }

    // Output value - TO DELETE
    /* printf("Input: ");
    for (i = 0; i < 32; i++) {
        printf("%d", input[i]);
    }
    printf("\n"); */

    // Get integer part
    for (i = 0; i < 7; i++)
    {
        if (input[i] == 1)
        {
            integer += pow(2, power);
        }
        power--;
    }
    // printf("Integer: %d\n", integer);

    // Get mantissa
    for (i = 0; i < 25; i++)
    {
        if (input[i + 7] == 1)
        {
            mantissa += (1.0 / pow(2, i + 1));
        }
    }

    // printf("Mantissa: %f\n", mantissa);
    // printf("Number: %f", integer + mantissa);

    *value = integer + mantissa;

    return SUCCESS;
}

int main()
{
    // Testing with input from stdint
    /* double a;
    int b;
    scanf("%d", &b);
    Convert_to_25fpp_representation(b, &a);
    printf("%.25f\n", a);
    return 0; */

    // a) See Convert_to_25fpp_representation function

    // b)
    /* Note that the value returned by the function is displayed
    with up to 15 digits after the decimal, as per the example. */
    double value;
    uint32_t example1 = 192937984; // Hex Value: 0x0B800000, Corresponding value: 5.75
    int return_value1 = Convert_to_25fpp_representation(example1, &value);
    printf("Value of example 1: %.15g.\n", value);

    uint32_t example2 = 2147516417; // Hex Value: 0x80008001, Corresponding value: 64.0009765923023
    int return_value2 = Convert_to_25fpp_representation(example2, &value);
    printf("Value of example 2: %.15g.\n", value);

    int return_value3 = Convert_to_25fpp_representation(example2, NULL);

    // c)
    // Return values of calls to Convert_to_25fpp_representation
    printf("\nReturn value of example 1: %d.\n", return_value1);
    printf("Return value of example 2: %d.\n", return_value2);
    printf("Return value of example 3: %d.\n", return_value3);

    return 0;
}
