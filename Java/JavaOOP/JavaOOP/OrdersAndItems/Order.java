import java.util.ArrayList;

public class Order {
    // Member variables
    private String name;
    // private double total;
    private boolean ready;
    private ArrayList<Item>items;

    // Constructor
    // No arguments, sets name to "Guest", initializes items as an empty list
    public Order(){
        name = "Guest";
        items =new ArrayList<Item>();
    }

    // Overloaded Constructor
    // Takes a name as an argument, sets name to this custom name
    // Initializes items as an empty list
    public Order(String name){
        this.name = name;
        items = new ArrayList<Item>();
    }

    // Order methods
    public void addItem(Item currentItem){
        this.items.add(currentItem);
    }

    public String getStatusMessage(String message){
        if (ready){
            message = "Your order is ready.";
        }
        else{
            message = "Thank you for waiting. Your order will be ready soon.";
        }
        return message;
    }

    public double getOrderTotal(double[] prices){
        double total = 0.0;
        return total;
    }

    public void display(ArrayList<String> customerOrder){
        for (int i = 0; i < customerOrder.size(); i++){
            System.out.printf("Customer Name: %s\n", name);
            System.out.printf("%s - $" + items.get(1), items.get(0));
        }
    }

    // Getters and setters
    public String getOrderName(){
        return name;
    }

    public void setOrderName(String orderName){
        name = orderName;
    }

    public boolean isReady(){
        return ready;
    }

    public void setIsReady(Boolean orderStatus){
        ready = orderStatus;
    }

    
}
