import java.util.ArrayList;
import java.util.Arrays;

public class CafeUtil {
    
    public int getStreakGoal(){
        int numWeeks = 10;
        int sum = 0;

        for (int i = 1; i < (numWeeks + 1); i++){
            sum += i;
        }
        return sum;
    }

    public double getOrderTotal(double[] prices){
        double total = 0;
        
        for (int i = 0; i < prices.length; i++){
            total += prices[i];
        }
        return total;
    }

    public void displayMenu(ArrayList<String> menuItems){

        for (int i = 0; i < menuItems.size(); i++){
            System.out.printf("%s %s \n", i, menuItems.get(i));
        }
    }

    public void addCustomer(ArrayList<String> customers){
        System.out.println("Please enter your name: ");
        String userName = System.console().readLine();
        System.out.printf("Hello, " + userName + "!");
        System.out.printf("There are %s people in front of you. \n", customers.size());
        customers.add(userName);
        System.out.println(customers);
        
    }
}