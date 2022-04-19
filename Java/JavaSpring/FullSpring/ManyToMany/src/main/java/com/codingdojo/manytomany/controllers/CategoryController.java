package com.codingdojo.manytomany.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.services.CategoryService;
import com.codingdojo.manytomany.services.ProductService;

@Controller
public class CategoryController {

	@Autowired
	CategoryService categoryServ;
	@Autowired
	ProductService productServ;
	
	//Index
	
	@GetMapping("/")
	public String index(Model model) {
		
		List<Product> products = productServ.allProducts();
		List<Category> categories = categoryServ.allCategories();
		
		model.addAttribute("products", products);
		model.addAttribute("categories", categories);
		
		return "index.jsp";
	}
	
	//New Category
	
	@GetMapping("/categories/new")
	public String newCategory(
			@ModelAttribute("category") Category category,
			Model model)
	{
		return "category_new.jsp";
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
	
	// View Category
	
	@GetMapping("/categories/{id}")
	public String viewCategory(
			Model model,
			@PathVariable("id") Long id) 
	{
		Category category = categoryServ.findCategory(id);
		model.addAttribute("category", category);
		model.addAttribute("usedProducts", productServ.getCategory(category));
		model.addAttribute("unusedProducts", productServ.getUnusedCategory(category));
		
		return "category_view.jsp";
	}
	
	@PostMapping("/categories/{id}")
	public String updateCategory(
			@PathVariable("id") Long id,
			@RequestParam(value="productId") Long productId,
			Model model) 
	{
		Category category = categoryServ.findCategory(id);
		Product product = productServ.findProduct(productId);
		
		category.getProducts().add(product);
		categoryServ.updateCategory(category);
		
		model.addAttribute("usedProducts", productServ.getCategory(category));
		model.addAttribute("unusedProducts", productServ.getUnusedCategory(category));
		
		return "redirect:/categories/" + id;
	}
	
		
	
	
}
