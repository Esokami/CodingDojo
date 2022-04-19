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
import org.springframework.web.bind.annotation.RequestParam;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.services.CategoryService;
import com.codingdojo.manytomany.services.ProductService;

@Controller
public class ProductController {
	
	@Autowired
	ProductService productServ;
	@Autowired
	CategoryService categoryServ;
	
	// New Product
	
	@GetMapping("/products/new")
	public String newProduct(@ModelAttribute("product") Product product) 
	{
		return "product_new.jsp";
	}
	
	@PostMapping("/newProduct")
	public String createProduct(
			@Valid @ModelAttribute("product") Product product,
			BindingResult result) 
	{
		if (result.hasErrors()) {
			return "product_new.jsp";
		}
		
		productServ.createProduct(product);
		return "redirect:/";
	}
	
	// View Product
	
	@GetMapping("/products/{id}")
	public String viewProduct(
			Model model,
			@PathVariable("id") Long id) 
	{
		Product product = productServ.findProduct(id);
		model.addAttribute("product", product);
		model.addAttribute("usedCategories", categoryServ.getProducts(product));
		model.addAttribute("unusedCategories", categoryServ.getUnusedProducts(product));
		
		return "product_view.jsp";
	}
	
	@PostMapping("/products/{id}")
	public String updateProduct(
			@PathVariable("id") Long id,
			@RequestParam(value="categoryId") Long categoryId,
			Model model) 
	{
		Product product = productServ.findProduct(id);
		Category category = categoryServ.findCategory(categoryId);
		
		product.getCategories().add(category);
		productServ.updateProduct(product);
		
		model.addAttribute("usedCategories", categoryServ.getProducts(product));
		model.addAttribute("unusedCategories", categoryServ.getUnusedProducts(product));
		
		return "redirect:/products/" + id;
	}
	
	
}
