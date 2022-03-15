import java.util.ArrayList;

public class Order {
    // Member variables
    private String name;
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

    public String getStatusMessage(){
        if (ready){
            return "Your order is ready.";
        }
        else{
            return "Thank you for waiting. Your order will be ready soon.";
        }
    }

    public double getOrderTotal(){
        double total = 0.0;

        for (Item i: items){
            total += i.getItemPrice();
        }

        return total;
    }

    public void display(){
        System.out.printf("Customer Name: %s\n", name);
        for (Item i: items){
            System.out.printf("%s - " + "$%s \n", i.getItemName(), i.getItemPrice());
        }
        System.out.printf("Total: %s\n", this.getOrderTotal());
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

    public ArrayList<Item> getItems(){
        return items;
    }

    public void setItems(ArrayList<Item> orderItems){
        items = orderItems;
    }
    
}
