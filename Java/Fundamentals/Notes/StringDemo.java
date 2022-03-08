public class StringDemo {
    public static void main(String[] args){
        String ninja = "Coding Dojo is Awesome!";
        int length = ninja.length();
        System.out.println( "String Length is: " + length);

        // CONCATENATE 
        String string1 = "My name is ";
        String string2 = "Michael";
        String string3 = string1.concat(string2);
        System.out.println(string3);

        // FORMAT 
        String ninja1 = String.format("Hi %s, you owe me $%.2f !", "Jack", 25.0);
        System.out.println(ninja1);

        // INDEX OF | searches left to right inside the given string for a "target" string. Returns the index number where the 
        // target string is firt found or -1 if the target is not found
        String ninja2 = "Welcome to Coding Dojo!";
        int a = ninja.indexOf("Coding"); // a is 11
        int b = ninja.indexOf("co"); // b is 3
        int c = ninja.indexOf("pizza"); // c is -1, "pizza" is not found

        // TRIM  | removes any trailing or leading white spaces from the string
        String sentence = "         spaces everywhere!     ";
        System.out.println(sentence.trim());

        // UPPERCASE AND LOWERCASE 
        String d = "HELLO";
        String e = "world";
        System.out.println(d.toLowerCase());
        System.out.println(e.toUpperCase());

        // EQUALITY  | Do they refer to the exact same object or do they have the same exact sequence of characters
        String f = "same string";
        String g = "same string";
        System.out.println(f == g);

        f = new String("same letters");
        g = new String("same letters");
        System.out.println(f == g);
        System.out.println(f.equals(g));

        // WHEN TO USE "==" OR ".equals"
        String h = new String("Dojo");
        System.out.println(h == "Dojo"); // will show false
        System.out.println(h.equals("Dojo")); // will show true
    }
}