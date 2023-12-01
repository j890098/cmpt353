

import java.util.ArrayList;

// =========================================
// Implementation of dual-pivot quicksort
// Derived portions of code from: https://www.geeksforgeeks.org/dual-pivot-quicksort/
public class QS {
    public void implementedQuicksort(ArrayList<Integer> array, int low, int high) {
        if (low < high) {
            int[] pivots = partition(array, low, high);

            // Recursion
            implementedQuicksort(array, low, pivots[0] - 1);
            implementedQuicksort(array, pivots[0] + 1, pivots[1] - 1);
            implementedQuicksort(array, pivots[1] + 1, high);
        }
    }

    public static int[] partition(ArrayList<Integer> array, int low, int high) {
        if (array.get(low) > array.get(high)) {
            swap(array, low, high);
        }

        int p1 = array.get(low);
        int p2 = array.get(high);
        int i = low + 1;
        int j = high - 1;
        int k = i;

        while (k <= j) {
            if (array.get(k) < p1) {
                swap(array, i, k);
                i++;
            }
            else if (array.get(k) >= p2) {
                while ((array.get(j) > p2) && (k < j)) {
                    j--;
                }
                swap(array, k, j);
                j--;

                if (array.get(k) < p1) {
                    swap(array, i, k);
                    i++;
                }
            }
            k++;
        }
        i--;
        j++;

        swap(array, low, i);
        swap(array, high, j);

        // Return indices of pivots in the form of an array
        return new int[]{i, j};
    }

    public static void swap(ArrayList<Integer> array, int a, int b) {
        int tmp = array.get(a);
        array.set(a, array.get(b));
        array.set(b, tmp);
    }
}
