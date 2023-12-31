

import java.io.*;
import java.util.*;
import java.time.*;



// ===================================
// Main class-- Compile then run with:
// javac Main.java   -->   java Main.java
public class Main {
    public static void main(String[] args) {
        // Find and read 'parameters.txt'
        try {
            // Read file and get N and ARRAY_SIZE
            File file = new File("parameters.txt");
            Scanner scanner = new Scanner(file);
            String String_N = scanner.next();
            String String_ARRAY_SIZE = scanner.next();
            scanner.close();

            // Convert from String to int
            int N = Integer.parseInt(String_N);
            int ARRAY_SIZE = Integer.parseInt(String_ARRAY_SIZE);
            System.out.println("N = " + N);
            System.out.println("ARRAY_SIZE = " + ARRAY_SIZE);

            // N trials of applying built-in sort
            ArrayList<String> time = new ArrayList<String>();
            time.add("java_dualqsort,implementedQuicksort");
            for (int i = 0; i < N; i++) {
                // Generate random array
                ArrayList<Integer> array1 = new ArrayList<Integer>();
                ArrayList<Integer> array2 = new ArrayList<Integer>();
                Random random = new Random();
                for (int j = 0; j < ARRAY_SIZE; j++) {
                    int r = random.nextInt(1000000);
                    array1.add(r);
                    array2.add(r);
                }
                // Call built-in sorting algorithm and time it in MILLISECONDS (ms)
                // NOTE: Java's only sorting algorithm for this type is a dual-pivot quicksort
                Instant start = Instant.now();
                Collections.sort(array1);
                Instant end = Instant.now();
                long elapsed1 = Duration.between(start, end).toMillis();

                // Call the hand-coded implementation of dual-pivot quicksort
                start = Instant.now();
                QS qs = new QS();
                qs.implementedQuicksort(array2, 0, array2.size() - 1);
                end = Instant.now();
                long elapsed2 = Duration.between(start, end).toMillis();
                time.add(elapsed1 + "," + elapsed2);

                // Output results in 'java_sorts.csv'
                try {
                    FileWriter output = new FileWriter("java_sorts.csv");
                    int rowNumber = 1;
                    for (String entry : time) {
                        // System.out.println(entry);
                        output.append(entry);
                        output.append("\n");
                        rowNumber++;
                    }
                    output.close();
                }
                // Handle exception
                catch (IOException e) {
                    System.out.println("Error in FileWriter.");
                }
            }
        }
        // Handle exception
        catch (FileNotFoundException e) {
            System.out.println("Error finding file.");
        }
    }
}
