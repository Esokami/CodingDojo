public class Casting {
    public static void main(String[] args){
        
        //EXPLICIT CASTING
        
        double d = 35.25;
        double dd = 35.99;

        //casting the double d into a int
        int i = (int) d;

        // casting the double dd into a int
        int ii = (int) dd;

        // System.out.println(i);
        // System.out.println(ii);

        //IMPLICIT CASTING
        int j = 35;
        float f = j;

        // System.out.println("The number is: " + f);

        // PRIMITIVE vs OBJECT TYPES

        // Performance | Object types are an instance of a class. They hold data and methods
        // Their memory capacity is much bugger than their primitive counterpart

        // Object version (longer)

        long start = System.currentTimeMillis();
        Integer sum = 0;
        for (int k = 0; k < Integer.MAX_VALUE; k++){
            sum += k;
        }

        // System.out.println("Sum: " + sum);
        long end = System.currentTimeMillis();
        double total = (double) (end - start) / 1000;
        // System.out.println("Time of execution: " + total + " seconds");

        // Primitive version

        long start2 = System.currentTimeMillis();
        int sum2 = 0;
        for (int m = 0; m < Integer.MAX_VALUE; m++){
            sum2 += m;
        }
        System.out.println("Sum: " + sum2);
        long end2 = System.currentTimeMillis();
        double total2 = (double) (end2 - start2) / 1000;
        System.out.println("Time of execution: " + total2 + " seconds.");

        // Null Values 
        // Primitve data types can only hold data. However, object types are pointers to where the data is stored
        // This means that this pointer can point to nothing (null) while primitive types cannot

        Integer a = 10;
        int b = 10;
        a = null;
        // b = null; //gives error: <null> cannot be converted to int
    }
}
