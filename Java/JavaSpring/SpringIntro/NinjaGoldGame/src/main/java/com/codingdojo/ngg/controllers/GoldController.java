package com.codingdojo.ngg.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GoldController {
	
	@RequestMapping("/")
	public String index() {
		return "index.jsp";
	}
	
	@PostMapping("/gold")
	public String farmGold(HttpSession session, @RequestParam int gold) {
		session.setAttribute("gold", gold);
		return "redirect:/activities";
	}
	
}
