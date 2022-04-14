package com.codingdojo.manytomany.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.services.CategoryService;

@Controller
public class CategoryController {

	@Autowired
	private CategoryService categoryServ;
	
	@GetMapping("/")
	public String index(Model model) {
		
		return "index.jsp";
	}
	
	@GetMapping("/categories/new")
	public String newCategory(@ModelAttribute("category") Category category)
	{
		return "category_new.jsp";
	}
	
	@GetMapping("/categories/{id}")
	public String viewCategory(
			Model model,
			@PathVariable("id") Long categoryId) 
	{
		Category category = categoryServ.findCategory(categoryId);
		model.addAttribute("category", category);
		
		return "category_view.jsp";
	}
	
	@PostMapping("/newCategory")
	public String createCategory(
			@Valid @ModelAttribute("category") Category category,
			BindingResult result) 
	{
		if (result.hasErrors()) {
			return "category_new.jsp";
		}
		
		categoryServ.createCategory(category);
		
		return "redirect:/";
	}
}
