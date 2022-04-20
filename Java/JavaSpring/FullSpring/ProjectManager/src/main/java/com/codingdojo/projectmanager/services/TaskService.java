package com.codingdojo.projectmanager.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.projectmanager.models.Task;
import com.codingdojo.projectmanager.repositories.TaskRepository;

@Service
public class TaskService {

	private final TaskRepository taskRepository;
	
	public TaskService(TaskRepository taskRepository) {
		this.taskRepository = taskRepository;
	}
	
	// returns all
	public List<Task> getAll(){
		return taskRepository.findAll();
	}
	
	// creates
	public Task create(Task b) {
		return taskRepository.save(b);
	}
	
	
	public List<Task> projectTasks(Long projectId){
		return taskRepository.findByProjectId(projectId);
	}
	
	// updates
	public Task update(Task b) {
		return taskRepository.save(b);
	}
	
	// deletes
	public void delete(Task b)
	{
		taskRepository.delete(b);
	}

}
