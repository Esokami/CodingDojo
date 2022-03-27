package com.codingdojo.forms.controllers;

import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MainController {
	
	@RequestMapping("/")
	public String index() {
		return "index.jsp";
	}
	
	@RequestMapping(value="/login", method=RequestMethod.POST)
	public String login(
			@RequestParam(value="email") String email,
			@RequestParam(value="password") String password) {
		
		// Code to process the form. i.e., check email and password
		
		return "redirect:/"; 
	}
	
	
	//Can use PostMapping or GetMapping instead of RequestMapping
	@RequestMapping(value="/processPayment", method=RequestMethod.POST)
	public String processPayment(
			@RequestParam(value="creditCardNumber") Integer creditCardNumber,
			@RequestParam(value="expDate") Date expDate,
			@RequestParam(value="amount") Double amount) {
		
		// Code here to complete the transaction and charge CC
		// ** Put any necessary information in the session for later
		
		return "redirect:/confirm"; // redirects to a /confirm render route
	}
	
	@RequestMapping("/confirm")
	public String confirmationPage(Model model) {
		// get any info needed out of session and add to the
		// view model to render on the page
		
		return "confirmation.jsp";
	}
}
