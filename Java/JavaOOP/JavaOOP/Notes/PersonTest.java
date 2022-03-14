public class PersonTest {
    public static void main(String[] args){
        Person person1 = new Person(10, "Person1", 130);
        Person person2 = new Person(5, "Person2", 100);
        person1.objectMethods(person2);
    }
}
