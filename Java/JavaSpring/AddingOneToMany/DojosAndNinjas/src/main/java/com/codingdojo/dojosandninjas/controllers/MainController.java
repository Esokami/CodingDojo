package com.codingdojo.dojosandninjas.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.dojosandninjas.models.Dojo;
import com.codingdojo.dojosandninjas.models.Ninja;
import com.codingdojo.dojosandninjas.services.DojoService;
import com.codingdojo.dojosandninjas.services.NinjaService;


@Controller
public class MainController {
	
	@Autowired
	DojoService dojoService;
	
	@Autowired
	NinjaService ninjaService;
	
	@RequestMapping("/")
	public String index() {
		return "redirect:/dojos";
	}
	
	// GETS
	
	@GetMapping("/dojos")
	public String dashboard(Model model, @ModelAttribute("dojo") Dojo dojo) {
		List<Dojo> dojos = dojoService.allDojos();
		model.addAttribute("dojos", dojos);
		
		return "index.jsp";
	}
	
	@GetMapping("/dojos/{id}")
	public String viewDojo(
			@PathVariable("id") Long id,
			Model model)
	{
		Dojo dojo = this.dojoService.findDojo(id);
		model.addAttribute("dojo", dojo);
		return "dojo_view.jsp";
	}
	
	@GetMapping("/dojos/new")
	public String newDojo(@ModelAttribute("dojo") Dojo dojo) {
		return "dojo_new.jsp";
	}
	
	@GetMapping("/ninjas/new")
	public String newNinja(
			@ModelAttribute("ninja") Ninja ninja,
			Model model,
			@ModelAttribute("dojo") Dojo dojo) {
		List<Dojo> dojos = dojoService.allDojos();
		model.addAttribute("dojos", dojos);
		
		return "ninja_new.jsp";
	}
	
	
	// POSTS
	
	@PostMapping("/dojos")
	public String createDojo(@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result, Model model) 
	{
		if(result.hasErrors()) {
			List<Dojo> dojos = dojoService.allDojos();
			model.addAttribute("dojos", dojos);
			
			return "index.jsp";
		}
		
		dojoService.createDojo(dojo);
		return "redirect:/dojos";
	}
	
	@PostMapping("/createDojo")
	public String createDojo(@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result) {
		
		if (result.hasErrors()) {
			return "dojo_new.jsp";
		}
		
		dojoService.createDojo(dojo);
		return "redirect:/dojos";		
	}
	
	@PostMapping("/createNinja")
	public String createNinja(@Valid @ModelAttribute("ninja") Ninja ninja,
			BindingResult result, Model model) {
		
		if (result.hasErrors()) {
			List<Dojo> dojos = dojoService.allDojos();
			model.addAttribute("dojos", dojos);
			return "ninja_new.jsp";
		}
		
		ninjaService.createNinja(ninja);
		return "redirect:/dojos/" + ninja.getDojo().getId();
		
	}

	
	
	// DELETES
	
	@DeleteMapping("/dojos/{id}")
	public String destroyDojo(@PathVariable("id") Long id) {
		this.dojoService.delete(id);
		return "redirect:/dojos";
	}
}
