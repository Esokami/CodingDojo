
public class Gorilla extends Mammal{
	
	public Gorilla() {
		this.energyLevel = 100;
	}
	
	public void throwSomething() {
		System.out.println("The Gorilla has thrown something.");
		energyLevel = energyLevel - 5;
		super.displayEnergy();
		
	}
	
	public void eatBananas() {
		System.out.println("The Gorilla is eating bananas.");
		energyLevel = energyLevel + 10;
		super.displayEnergy();
	}
	
	public void climb() {
		System.out.println("The Gorilla is climbing.");
		energyLevel = energyLevel - 10;
		super.displayEnergy();
	}
}
