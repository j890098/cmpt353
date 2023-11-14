package java_sorts;
import java.io.*;
import java.util.*;
import java.time.*;



// ===================================
// Main class-- Compile then run with:
// javac Main.java   -->   java Main.java
class Main {
    public static void main(String[] args) {
        // Find and read 'parameters.txt'
        try {
            // Read file and get N and ARRAY_SIZE
            File file = new File("../parameters.txt");
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
            time.add("java_dualqsort");
            for (int i = 0; i < N; i++) {
                // Generate random array
                ArrayList<Integer> array = new ArrayList<Integer>();
                Random random = new Random();
                for (int j = 0; j < ARRAY_SIZE; j++) {
                    array.add(random.nextInt(1000000));
                }

                // Call built-in sorting algorithm and time it in MILLISECONDS (ms)
                // NOTE: Java's only sorting algorithm for this type is a dual-pivot quicksort
                Instant start = Instant.now();
                Collections.sort(array);
                Instant end = Instant.now();
                long elapsed = Duration.between(start, end).toMillis();
                time.add(elapsed + "");

                // Output results in 'java_sorts.csv'
                try {
                    FileWriter output = new FileWriter("java_sorts.csv");
                    int rowNumber = 1;
                    for (String entry : time) {
                        // System.out.println(entry);
                        output.append(entry);
                        // Append comma if not last row
                        if (rowNumber != N+1) {
                            output.append(",");
                        }
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
