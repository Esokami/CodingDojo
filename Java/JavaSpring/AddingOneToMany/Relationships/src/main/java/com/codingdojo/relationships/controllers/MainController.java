package com.codingdojo.relationships.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.relationships.models.Person;
import com.codingdojo.relationships.services.PersonService;

@Controller
public class MainController {
	
	@Autowired
	PersonService personService;
	
	@RequestMapping("/")
	public String index() {
		return "redirect:/persons";
	}
	
	@GetMapping("/persons")
	public String dashboard(Model model,
			@ModelAttribute("person") Person person) {
		List<Person> persons = personService.allPersons();
		model.addAttribute("persons", persons);
		
		return "index.jsp";
	}
	
	@GetMapping("/persons/{person_id}")
	public String showPerson(@PathVariable Long person_id, Model model) {
		
		Person someAwesomePerson = personService.findPerson(person_id);
		model.addAttribute("person", someAwesomePerson);
		
		return "showPerson.jsp";
	}
}
