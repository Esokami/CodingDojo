package com.codingdojo.dojosandninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.dojosandninjas.models.Dojo;
import com.codingdojo.dojosandninjas.models.Ninja;
import com.codingdojo.dojosandninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	
	private final NinjaRepository ninjaRepository;
	
	public NinjaService(NinjaRepository ninjaRepository) {
		this.ninjaRepository = ninjaRepository;
	}
	
	// returns all ninjas
	public List<Ninja> allNinjas(){
		return ninjaRepository.findAll();
	}
	
	// creates a new ninja
	public Ninja createNinja(Ninja d) {
		return ninjaRepository.save(d);
	}
	
	// retrieves ninja
	public Ninja findNinja(Long id) {
		Optional<Ninja> optionalNinja = ninjaRepository.findById(id);
		if (optionalNinja.isPresent()) {
			return optionalNinja.get();
		}
		else {
			return null;
		}
	}
	
	// updates ninja
	public Ninja updateNinja(Ninja d) {
		return ninjaRepository.save(d);
	}
	
	public List<Ninja> ninjaDojo(Dojo dojo){
		return ninjaRepository.findAllByDojo(dojo);
	}
	
	// deletes ninja
	public void delete(Long id) {
		Optional<Ninja> optionalNinja = ninjaRepository.findById(id);
		if (optionalNinja.isPresent()) {
			ninjaRepository.deleteById(id);
		}
	}
}
