import java.util.Random;
import java.util.ArrayList;

public class TestPuzzleJava {
    public static void main(String[] args){
        PuzzleJavaUtil generator = new PuzzleJavaUtil();

        System.out.println("\n----- Get Ten Rolls -----");
        ArrayList<Integer> randomRolls = generator.getTenRolls();
        System.out.println(randomRolls);

        System.out.println("\n----- Get Random Letter -----");
        System.out.println(generator.getRandomLetter());

        System.out.println("\n----- Generate Password -----");
        System.out.println(generator.generatePassword());

        System.out.println("\n----- Get New Password Set -----");
        System.out.println(generator.getNewPasswordSet(8));
    }
}