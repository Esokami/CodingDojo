import java.util.Random;
import java.util.ArrayList;

public class PuzzleJavaUtil {
    Random randMachine = new Random();

    public ArrayList<Integer> getTenRolls() {
        ArrayList<Integer> rolls = new ArrayList<Integer>();

        for (int i = 1; i <= 10; i++){
            rolls.add(randMachine.nextInt(20));
        }
        return rolls;
    }

    public String getRandomLetter(){
        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        String[] letter = new String[26];

        for (int i = 0; i < letter.length; i++){
            letter[i] = String.valueOf((alphabet.charAt(i)));
        }
        return letter[randMachine.nextInt(26)];
    }

    public String generatePassword(){
        String password = "";

        for (int i = 0; i < 8; i++){
            password = password + getRandomLetter();
        }
        return password;
    }

    public ArrayList<String> getNewPasswordSet(int length){
        ArrayList<String> passwordSet = new ArrayList<String>();
        for (int i = 0; i < length; i++){
            passwordSet.add(generatePassword());
        }
        return passwordSet;
    }
}
