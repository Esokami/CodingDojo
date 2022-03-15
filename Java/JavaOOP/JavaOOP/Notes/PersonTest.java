public class PersonTest {
    public static void main(String[] args){
        Person person1 = new Person(10, "Person1");
        Person person2 = new Person(5, "Person2");
        Person person3 = new Person(15, "Person3");
        System.out.println(Person.peopleCount());

        // Person person1 = new Person(10, "Person1", 130);
        // Person person2 = new Person(5, "Person2", 100);
        // person1.objectMethods(person2);
    }
}
