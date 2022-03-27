package com.codingdojo.omikuji.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class OmikujiController {
	
	@RequestMapping("/")
	public String index() {
		return "index.jsp";
	}
	
	@PostMapping("/createFortune")
	public String createFortune(
			HttpSession session,
			@RequestParam("number") int number,
			@RequestParam("city") String city,
			@RequestParam("person") String person,
			@RequestParam("endeavor") String endeavor,
			@RequestParam("organism") String organism,
			@RequestParam("comment") String comment) {
		
		session.setAttribute("number", number);
		session.setAttribute("city", city);
		session.setAttribute("person", person);
		session.setAttribute("endeavor", endeavor);
		session.setAttribute("organism", organism);
		session.setAttribute("comment", comment);
		
		
		return "redirect:/fortune";
	}
	
	@RequestMapping("/fortune")
	public String displayFortune(HttpSession session, Model model) {
		int currentNumber = (int) session.getAttribute("number");
		String currentCity = (String) session.getAttribute("city");
		String currentPerson = (String) session.getAttribute("person");
		String currentEndeavor = (String) session.getAttribute("endeavor");
		String currentOrganism = (String) session.getAttribute("organism");
		String currentComment = (String) session.getAttribute("comment");
		
		model.addAttribute("currentNumber", currentNumber);
		model.addAttribute("currentCity", currentCity);
		model.addAttribute("currentPerson", currentPerson);
		model.addAttribute("currentEndeavor", currentEndeavor);
		model.addAttribute("currentOrganism", currentOrganism);
		model.addAttribute("currentComment", currentComment);
		
		return "fortune.jsp";
	}
}
