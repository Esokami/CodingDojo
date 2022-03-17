
public class Mammal {
	int energyLevel = 100;
	
	public Mammal() {
		energyLevel = 100;
	}
	
	public int displayEnergy() {
		System.out.println("Energy level: " + energyLevel);
		return energyLevel;
	}
}
