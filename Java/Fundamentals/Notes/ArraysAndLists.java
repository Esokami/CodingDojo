import java.util.ArrayList;

public class ArraysAndLists {
    public static void main(String[] args){

        // FIXED ARRAY

        int[] myArray = new int[5];

        myArray[0] = 4;
        myArray[1] = 8;
        myArray[2] = 8;
        myArray[3] = 5;
        myArray[4] = 9;

        // for (int i = 0; i < myArray.length; i++){
        //     System.out.println(myArray[i]);
        // }

        // String[] fruits = {"banana", "pear", "papaya", "kiwi"};
        // String temp = fruits[0];
        // fruits[0] = fruits[fruits.length - 1];
        // fruits[fruits.length -1] = temp;

        // for (int i = 0; i < fruits.length; i++){
        //     System.out.println(fruits[i]);
        // }

        // DYNAMIC ARRAYS

        ArrayList<Integer>myList = new ArrayList<Integer>();
        System.out.println(myList);

        myList.add(10);
        myList.add(11);
        System.out.println(myList);

        // Getters and Setters
        Integer num = myList.get(0);
        System.out.println(num);

        myList.set(0, 9);
        System.out.println(myList);

        ArrayList<Object>things = new ArrayList<Object>( );
        things.add(10);
        things.add("Hello");
        things.add(new ArrayList<Integer>());
        things.add(12.5);
        System.out.println(things);

        // WHILE LOOP

        int i = 0;
        while (i < 7){
            System.out.println("foo");
            i++;
        }

        // FOR LOOPS
        // for (initialization; termination; increment){
        //     body statements
        // }
        for (int j = 0; j < 7; j++){
            System.out.println("bar");
        }

        ArrayList<String> dynamicArray = new ArrayList<String>();
        dynamicArray.add("hello");
        dynamicArray.add("world");
        dynamicArray.add("etc");
        for (int k = 0; k < dynamicArray.size(); k++){
            System.out.println(dynamicArray.get(k));
        }

        // ENHANCED FOR LOOP
        //From this to
        for (int m = 0; m < dynamicArray.size(); m++){
            String name = dynamicArray.get(m);
            System.out.println("hello" + name);
        }
        //This
        for (String name : dynamicArray){
            System.out.println("hello " + name);
        }
        //Reference
        // for(element container : collection){
        //     // body statements
        // }
        
        // WHEN NOT TO USE AN ENHANCED LOOP
        ArrayList<String> snacks = new ArrayList<String> ();
        snacks.add("Apples");
        snacks.add("Pretzels");
        snacks.add("Almonds");
        snacks.add("Yogurt");
        for(String snack : snacks ) {
            if(snack.charAt(0) == 'A') {
                snacks.remove(snack);
            }
        }
        // this will encounter an error like
        // Exception in thread "main" java.util.ConcurrentModificationException
        for(int n=0; n<snacks.size(); n++) {
            if(snacks.get(n).charAt(0) == 'A') {
                snacks.remove(n);
            }
        }
        
    }
}
