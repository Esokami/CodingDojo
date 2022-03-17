
public class Bat extends Mammal{
	public Bat() {
		this.energyLevel = 300;
	}
	
	public void fly() {
		System.out.println("Swoosh");
		energyLevel = energyLevel - 50;
		super.displayEnergy();
	}
	
	public void eatHumans() {
		System.out.println("Oof");
		energyLevel = energyLevel + 25;
		super.displayEnergy();
	}
	
	public void attackTown() {
		System.out.println("Ahhhh Fire!");
		energyLevel = energyLevel - 100;
		super.displayEnergy();
	}
}
