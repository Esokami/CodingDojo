package com.codingdojo.projectmanager.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.projectmanager.models.Project;
import com.codingdojo.projectmanager.models.User;
import com.codingdojo.projectmanager.services.ProjectService;
import com.codingdojo.projectmanager.services.UserService;

@Controller
public class ProjectController {

	@Autowired
	ProjectService projectService;
	@Autowired
	UserService userService;

	//***VIEW***
	
	@GetMapping("/dashboard/{projectId}")
	public String showProject(
			Model model, 
			@PathVariable("projectId") Long projectId,
			HttpSession session) {
		
		if(session.getAttribute("id")==null) {
			return "redirect:/";
		}
		
		Project project = projectService.find(projectId);
	
		model.addAttribute("project", project);
		
		Long id = (Long)session.getAttribute("id");
		User user = userService.findById(id);
		model.addAttribute("user", user);
		
		return "project_view.jsp";
	}
	
	//***CREATE***
	
	@GetMapping("/dashboard/new")
	public String newProject(
			@ModelAttribute("project") Project project,
			Model model,
			HttpSession session) {
		
		Long id = (Long)session.getAttribute("id");
		User user = userService.findById(id);
		model.addAttribute("user", user);
		
		return "project_new.jsp";
	}
	
	@PostMapping("/createProject")
	public String create(
			@Valid @ModelAttribute("project") Project project,
			BindingResult result,
			HttpSession session) {
		
		Long id = (Long) session.getAttribute("id");
		if(id == null) {
			return "redirect:/logout";
		}
		
		if (result.hasErrors()) {
			return "project_new.jsp";
		}
		
		User user = userService.findById(id);
		Project newProject = new Project(project.getTitle(), project.getDueDate(), project.getDescription(), project.getLead());
		newProject.setLead(user);
		projectService.create(newProject);
		user.getProjects().add(newProject);
		userService.updateUser(user);
		
		return "redirect:/dashboard";
		
	}
	
	//***EDIT***
	
	@GetMapping("/dashboard/edit/{id}")
	public String editProject(
			@PathVariable("id") Long id,
			Model model,
			HttpSession session) {
		
		if(session.getAttribute("id") == null) {
			return "redirect:/";
		}
		
		Project project = this.projectService.find(id);
		model.addAttribute("project", project);
		return "project_edit.jsp";
	}
	
	@PutMapping("/dashboard/edit/{id}")
	public String updateProject(
			@PathVariable("id") Long id,
			@Valid @ModelAttribute("project") Project project, 
			BindingResult result,
			HttpSession session) {
		
		Long userId = (Long) session.getAttribute("id");
		
		User user = userService.findById(userId);
		
		if(userId == null) {
			return "redirect:/logout";
		}
		
		if (result.hasErrors()) {
			return "project_edit.jsp";
		}
		
		Project currentProject = projectService.find(id);
		project.setUsers(currentProject.getUsers());
		project.setLead(user);
		projectService.update(project);
		return "redirect:/dashboard";
	}
	
	//***JOINS/UNJOINS***
	
	@RequestMapping("/dashboard/join/{projectId}")
	public String joinProject(
			@PathVariable("projectId") Long projectId,
			HttpSession session,
			Model model)
	{
		Long id = (Long) session.getAttribute("id");
		if(id == null) {
			return "redirect:/logout";
		}
		
		Project project = projectService.find(projectId);
		User user = userService.findById(id);
		
		user.getProjects().add(project);
		userService.updateUser(user);
		
		
		return "redirect:/dashboard";
	}
	
	@RequestMapping("/dashboard/leave/{projectId}")
	public String leaveProject(
			@PathVariable("projectId") Long projectId,
			HttpSession session,
			Model model)
	{
		Long id = (Long) session.getAttribute("id");
		if(id == null) {
			return "redirect:/logout";
		}
		
		Project project = projectService.find(projectId);
		User user = userService.findById(id);
		
		user.getProjects().remove(project);
		userService.updateUser(user);
		
		
		return "redirect:/dashboard";
	}
	
	//***DELETE***
	
	@RequestMapping("/dashboard/delete/{projectId}")
	public String delete(
			@PathVariable("projectId") Long projectId,
			HttpSession session) 
	{
		if (session.getAttribute("id")==null) {
			return "redirect:/logout";
		}
		
		projectService.delete(projectService.find(projectId));
		return "redirect:/dashboard";
	}
	

}
