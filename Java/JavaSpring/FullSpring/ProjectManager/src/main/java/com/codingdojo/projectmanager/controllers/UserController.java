package com.codingdojo.projectmanager.controllers;

import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.projectmanager.models.LoginUser;
import com.codingdojo.projectmanager.models.Project;
import com.codingdojo.projectmanager.models.User;
import com.codingdojo.projectmanager.services.ProjectService;

@Controller
public class UserController {

	@Autowired
	private com.codingdojo.projectmanager.services.UserService userService;
	@Autowired
	private ProjectService projectService;
	
	@GetMapping("/")
	public String index(Model model) {

		model.addAttribute("newUser", new User());
		model.addAttribute("newLogin", new LoginUser());
		return "index.jsp";
	}
	
	@GetMapping("/dashboard")
	public String dashboard(HttpSession session, Model model) {
		
		if (session.getAttribute("id") == null) {
			return "redirect:/logout";
		}
		
		Long id = (Long) session.getAttribute("id");
		List<Project> userProjects = projectService.usersInProject(userService.findById(id));
		model.addAttribute("inProjects", userProjects);
		
		List<Project> unledProjects = projectService.usersNotInProject(userService.findById(id));
		model.addAttribute("notInProjects", unledProjects);
		
		model.addAttribute("user", userService.findById(id));
		
		return "dashboard.jsp";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.setAttribute("id", null);
		return "redirect:/";
	}
	
	@PostMapping("/register")
	public String register(
			@Valid @ModelAttribute("newUser") User newUser,
			BindingResult result,
			Model model,
			HttpSession session) 
	{

		User user = userService.register(newUser, result);
		
		
		
		if(result.hasErrors()) {
			model.addAttribute("newLogin", new LoginUser());
			return "index.jsp";
		}
		
		session.setAttribute("id", user.getId());
		
		return "redirect:/dashboard";
	}
	
	@PostMapping("/login")
	public String login(
			@Valid @ModelAttribute("newLogin") LoginUser newLogin,
			BindingResult result,
			Model model,
			HttpSession session)
	{
		User user = userService.login(newLogin, result);
		
		if(result.hasErrors() || user==null) {
			model.addAttribute("newUser", new User());
			return "index.jsp";
		}
		
		
		session.setAttribute("id", user.getId());
		
		return "redirect:/dashboard";
	}
}
