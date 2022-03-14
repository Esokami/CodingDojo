public class Person {
    private int age; 
    private int cmHeight;
    private String name;

    public Person(int ageParam, String nameParam, int cmHeight){
        this.age = ageParam;
        this.name = nameParam;
        this.cmHeight = cmHeight;
    }
    // Must use "this" if one of the parameter variables shares the same name as one of the member variables
    // public Person(int age, String name){
    //     this.age = age;
    //     this.name = name;

        // this will not set the attribute value. 'age' is a local variable in the constructor method and its value is the very 
        // first argument

        //age = age
    // }

    public void objectMethods(Person anotherObject){
        System.out.println("Class name: " + this.getClass().getSimpleName());
        System.out.println("toString: " + this.toString());
        System.out.print(("Equals: " + this.equals(anotherObject)));
    }
}
