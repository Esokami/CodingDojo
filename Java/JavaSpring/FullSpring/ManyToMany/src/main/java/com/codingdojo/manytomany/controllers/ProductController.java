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

import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.services.ProductService;

@Controller
public class ProductController {
	
	@Autowired
	ProductService productServ;
	
	@GetMapping("/products/new")
	public String newProduct(@ModelAttribute("product") Product product) 
	{
		return "product_new.jsp";
	}
	
	@GetMapping("/products/{id}")
	public String viewProduct(
			Model model,
			@PathVariable("id") Long productId) 
	{
		Product product = productServ.findProduct(productId);
		model.addAttribute("product", product);
		
		return "product_view.jsp";
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
}
