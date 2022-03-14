public class Item {
    // Member variables
    private String name;
    private double price;

    // Constructor
    // Takes a name and price as arguments
    // and sets them accordingly
    public Item(String name, Double price){
        this.name = name;
        this.price = price;
    }

    // Getters and Setters - for name and price
    public String getItemName(){
        return name;
    }

    public void setItemName(String itemName){
        name = itemName;
    }

    public double getItemPrice(){
        return price;
    }

    public void setItemPrice(Double itemPrice){
        price = itemPrice;
    }
}
