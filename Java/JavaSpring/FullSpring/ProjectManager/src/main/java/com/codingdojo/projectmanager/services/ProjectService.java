package com.codingdojo.projectmanager.services;

import java.util.List;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.projectmanager.models.Project;
import com.codingdojo.projectmanager.models.User;
import com.codingdojo.projectmanager.repositories.ProjectRepository;

@Service
public class ProjectService {

	private final ProjectRepository projectRepository;
	
	public ProjectService(ProjectRepository projectRepository) {
		this.projectRepository = projectRepository;
	}
	
	// returns all
	public List<Project> getAll(){
		return projectRepository.findAll();
	}
	
	// creates
	public Project create(Project b) {
		return projectRepository.save(b);
	}
	
	// retrieves 
	public Project find(Long id) {
		Optional<Project> optionalProject = projectRepository.findById(id);
		if (optionalProject.isPresent()) {
			return optionalProject.get();
		}
		else {
			return null;
		}
	}
	
	// updates
	public Project update(Project b) {
		return projectRepository.save(b);
	}
	
	// deletes
	public void delete(Project book) {
		projectRepository.delete(book);
	}
	

	public List<Project> usersInProject(User user){
		return projectRepository.findAllByUsers(user);
	}
	
	public List<Project> usersNotInProject(User user){
		return projectRepository.findByUsersNotContains(user);
	}

}
