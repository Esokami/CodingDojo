class Barista {
    private String name;
    private CoffeeMaker;

    public Barista(String name){
        this.name = name;
        this.cafe = new CoffeeMaker(40);
    }
    
    public void makeCoffee(){
        this.cafe.brew();
    }
}
