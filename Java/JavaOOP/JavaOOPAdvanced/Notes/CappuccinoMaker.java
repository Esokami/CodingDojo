class CappuccinoMaker extends CoffeeMaker{
    // Inheritance Example
    public CappuccinoMaker(int maxVolumeOz){
        super(maxVolumeOz);
        this.milk = "whole";
    }

    public void makeCappuccino(String beans){
        super.brew(beans);
        System.out.println("Smooth.");
    }

    // Polymorphism Example

    // private String milk;
    // public CappuccinoMaker(){
    //     this.maxVolumeOz = 16;
    //     this.milk = "whole";
    // }

    // public void brew(String beans){
    //     super.brew(beans);
    //     System.out.println("Frothy!!!");
    // }

    // public void clean(){
    //     System.out.println("Cleaning the froth!");
    // }
}
