public class TestOrders {
    public static void main(String[] args){
        // Menu Items
        Item item1 = new Item("Latte", 3.80);
        Item item2 = new Item("Mocha", 3.50);
        Item item3 = new Item("Cappuccino", 4.20);
        Item item4 = new Item("Drip", 3.60);

        // Orders
        Order order1 = new Order();
        Order order2 = new Order();

        Order order3 = new Order("Cindhurri");
        Order order4 = new Order("Jimmy");
        Order order5 = new Order("Noah");

        // //Application simulations
        order1.addItem(item1);
        order1.addItem(item2);
        order1.display();
        order1.setIsReady(true);
        System.out.println(order1.getStatusMessage());

        order2.addItem(item3);
        order2.addItem(item3);
        order2.display();

        order3.addItem(item4);
        order3.addItem(item1);
        order3.setIsReady(true);
        order3.display();
        System.out.println(order3.getStatusMessage());

        order4.addItem(item1);
        order4.addItem(item2);
        order4.display();
        System.out.println(order4.getOrderTotal());

        order5.addItem(item3);
        order5.addItem(item2);
        order5.display();

    }

}
