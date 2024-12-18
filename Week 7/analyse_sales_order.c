//
// Created by admin on 11/22/2024.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ORDERS 100000
#define MAX_SHOPS 1000
#define MAX_CUSTOMERS 1000
#define MAX_TIME_STR 9

// Define data structure for a sale transaction
typedef struct {
    char customer_id[21];
    char product_id[21];
    int price;
    char shop_id[21];
    int time_sec;
} Transaction;

// Global variables for storing data
Transaction db[MAX_ORDERS];
long total_orders = 0;
long total_revenue = 0;
long shop_revenue[MAX_SHOPS];
long customer_shop_revenue[MAX_CUSTOMERS][MAX_SHOPS];
long cumulative_revenue[MAX_ORDERS];

// Function to convert time to seconds
int time_to_sec(const char* time) {
    int h, m, s;
    sscanf(time, "%d:%d:%d", &h, &m, &s);
    return h * 3600 + m * 60 + s;
}

// Comparison function for sorting transactions by time
int compare(const void *a, const void *b) {
    return ((Transaction *)a)->time_sec - ((Transaction *)b)->time_sec;
}

// Binary search function
int binary_search(int arr[], int size, int target, int lower) {
    int left = 0, right = size - 1, mid;
    while (left <= right) {
        mid = (left + right) / 2;
        if (arr[mid] < target) {
            left = mid + 1;
        } else if (arr[mid] > target) {
            right = mid - 1;
        } else {
            return mid;
        }
    }
    return (lower ? left : right);
}

int main() {
    char buffer[256];
    char command[256];
    int i = 0;

    // Read input and process transactions
    while (fgets(buffer, sizeof(buffer), stdin) && buffer[0] != '#') {
        char customer_id[21], product_id[21], shop_id[21], time[9];
        int price;

        sscanf(buffer, "%s %s %d %s %s", customer_id, product_id, &price, shop_id, time);

        // Process transaction
        strcpy(db[i].customer_id, customer_id);
        strcpy(db[i].product_id, product_id);
        db[i].price = price;
        strcpy(db[i].shop_id, shop_id);
        db[i].time_sec = time_to_sec(time);

        total_orders++;
        total_revenue += price;

        // Shop revenue calculation
        int shop_index = atoi(shop_id + 1) - 1; // assuming shop_id format is "S1", "S2", ...
        shop_revenue[shop_index] += price;

        // Customer-shop revenue calculation
        int customer_index = atoi(customer_id + 1) - 1; // assuming customer_id format is "C1", "C2", ...
        customer_shop_revenue[customer_index][shop_index] += price;

        i++;
    }

    // Sort the transactions based on time
    qsort(db, total_orders, sizeof(Transaction), compare);

    // Precompute cumulative revenue for faster period queries
    cumulative_revenue[0] = db[0].price;
    for (int j = 1; j < total_orders; j++) {
        cumulative_revenue[j] = cumulative_revenue[j - 1] + db[j].price;
    }

    // Process queries
    while (fgets(buffer, sizeof(buffer), stdin) && buffer[0] != '#') {
        sscanf(buffer, "%s", command);

        if (strcmp(command, "?total_number_orders") == 0) {
            printf("%ld\n", total_orders);
        } else if (strcmp(command, "?total_revenue") == 0) {
            printf("%ld\n", total_revenue);
        } else if (strncmp(command, "?revenue_of_shop", 16) == 0) {
            char shop_id[21];
            sscanf(buffer + 17, "%s", shop_id);
            int shop_index = atoi(shop_id + 1) - 1;
            printf("%ld\n", shop_revenue[shop_index]);
        } else if (strncmp(command, "?total_consume_of_customer_shop", 30) == 0) {
            char customer_id[21], shop_id[21];
            sscanf(buffer + 31, "%s %s", customer_id, shop_id);
            int customer_index = atoi(customer_id + 1) - 1;
            int shop_index = atoi(shop_id + 1) - 1;
            printf("%ld\n", customer_shop_revenue[customer_index][shop_index]);
        } else if (strcmp(command, "?total_revenue_in_period") == 0) {
            char start_time[9], end_time[9];
            sscanf(buffer + 23, "%s %s", start_time, end_time);

            int start_sec = time_to_sec(start_time);
            int end_sec = time_to_sec(end_time);

            // Use binary search to find the range of transactions within the time period
            int start_idx = binary_search(db, total_orders, start_sec, 1);
            int end_idx = binary_search(db, total_orders, end_sec, 0);

            if (start_idx <= end_idx) {
                long result = cumulative_revenue[end_idx];
                if (start_idx > 0) {
                    result -= cumulative_revenue[start_idx - 1];
                }
                printf("%ld\n", result);
            } else {
                printf("0\n");
            }
        }
    }

    return 0;
}
