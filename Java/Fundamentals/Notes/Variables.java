public class Variables {
    public static void main(String[] args){
        int ourInt; // we can delcare a variable without setting its value
        ourInt = 400; // we can assign a value to the variable later in our code
        double pi = 3.14159265; // we can also declare and assign on the same line
        boolean bool = true; 
        char singleCharacter = 'A';

        String multipleCharacters = "ABC";

        // IF STATEMENTS

        boolean isRaining = true;
        boolean isCold = true;

        if (isRaining){
            // what to do if the condition is true
            System.out.println("Bring an umbrella.");
        }
        //continue with program
        else if (isCold) {
            System.out.println("Wear a coat.");
        }
        else{
            System.out.println("Have fun!");
        }

        // Notes

        // A condition must alway evaluate to a boolean value, true or false

        // If condition is true, it will execute the block of code between the curly braces {}
        // then skip any other "else if" or "else" statements in that chain and keep going

        // If the condition is false, it will skip that block of code {} but continue to the code
        // immdiately following that block which may be another "else if" or "else" statement

        
    }
}