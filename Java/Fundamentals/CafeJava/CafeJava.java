public class CafeJava {
    public static void main(String[] args){
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly.";
        String readyMessage = ", your order is ready.";
        String displayTotalMessage = "Your total is $";

        double mochaPrice = 3.5;
        double dripPrice = 3.6;
        double lattePrice = 3.9;
        double cappucinoPrice = 4.5;

        double DripPrice = 3.2;
        double LattePrice = 3.8;
        double CappucinoPrice = 4.2;

        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";

        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = false;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = false;

        System.out.println(generalGreeting + customer1 + pendingMessage);

        if (isReadyOrder4){
            System.out.println(generalGreeting + customer4 + readyMessage + displayTotalMessage + cappucinoPrice);
        }
        else{
            System.out.println(generalGreeting + customer4 + pendingMessage);
        }

        if (isReadyOrder2){
            System.out.println(generalGreeting + customer2 + readyMessage + displayTotalMessage + (lattePrice + lattePrice));
        }
        else{
            System.out.println(generalGreeting + customer2 + pendingMessage);
        }

        System.out.println(generalGreeting + customer3 + readyMessage + displayTotalMessage + (lattePrice - dripPrice));
    }
}