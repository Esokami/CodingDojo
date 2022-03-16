// Encapsulation Example

public class CoffeeMaker{
    protected int maxVolumeOz;
    protected String milk;

    public CoffeeMaker(int maxVolumeOz){
        this.maxVolumeOz = maxVolumeOz;
    }

    public int getMaxVolume(){
        return this.maxVolumeOz;
    }

    public int getMaxServings(){
        return this.maxVolumeOz;
    }

    public void brew(String beans){
        System.out.println("Brewing coffee");
    }
}