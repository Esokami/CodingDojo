package com.codingdojo.hoppersreceipt.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HoppersReceiptController {
	@RequestMapping("/")
	public String index(Model model) {
		String name = "Grace Hopper";
		String itemName = "Copper wire";
		double price = 5.25;
		String description = "Metal strips, also an illustration of nanoseconds.";
		String vendor = "Little Things Corner Store";
		
		
		model.addAttribute("name", name);
		model.addAttribute("itemName", itemName);
		model.addAttribute("price", price);
		model.addAttribute("description", description);
		model.addAttribute("vendor", vendor);
		
		/*model.addAttribute("name", "Yennefer");
		model.addAttribute("itemName", "Lilacs");
		model.addAttribute("price", 6.75);
		model.addAttribute("description", "Flowers to make perfume.");
		model.addAttribute("vendor", "Witch of the Forest");*/
		
		return "index.jsp";
	}
}
