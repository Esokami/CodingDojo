package com.codingdojo.languages.controllers;

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
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.languages.models.Language;
import com.codingdojo.languages.services.LanguageService;

@Controller
public class LanguageController {

	@Autowired
	LanguageService languageService;
	
	@RequestMapping("/")
	public String index() {
		return "redirect:/languages";
	}
	
	@GetMapping("/languages")
	public String dashboard(Model model, @ModelAttribute("language") Language language) {
		List<Language> languages = languageService.allLanguages();
		model.addAttribute("languages", languages);
		
		return "index.jsp";
	}
	
	@PostMapping("/languages")
	public String create(@Valid @ModelAttribute("language") Language language,
			BindingResult result, Model model) 
	{
		if(result.hasErrors()) {
			List<Language> languages = languageService.allLanguages();
			model.addAttribute("languages", languages);
			
			return "index.jsp";
		}
		
		languageService.create(language);
		return "redirect:/languages";
	}
	
	@GetMapping("/languages/edit/{id}")
	public String getLanguage(@PathVariable("id") Long id, Model model) {
		Language language = this.languageService.findLanguage(id);
		model.addAttribute("language", language);
		return "edit.jsp";
	}
	
	@PutMapping("/languages/edit/{id}")
	public String update(
			@PathVariable("id") Long id,
			Model model,
			@Valid @ModelAttribute("language") Language language, 
			BindingResult result) {
		if (result.hasErrors()) {
			return "edit.jsp";
		}
		else {
			languageService.updateLanguage(language);
			return "redirect:/languages";
		}
	}
	
	@GetMapping("/languages/{id}")
	public String view(
			@PathVariable("id") Long id,
			Model model)
	{
		Language language = this.languageService.findLanguage(id);
		model.addAttribute("language", language);
		return "view.jsp";
	}
	
	@DeleteMapping("/languages/{id}")
	public String destroy(@PathVariable("id") Long id) {
		this.languageService.delete(id);
		return "redirect:/languages";
	}
	
}
