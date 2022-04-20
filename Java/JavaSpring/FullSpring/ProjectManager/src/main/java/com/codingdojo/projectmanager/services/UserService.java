package com.codingdojo.projectmanager.services;

import java.util.List;
import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.codingdojo.projectmanager.models.LoginUser;
import com.codingdojo.projectmanager.models.Project;
import com.codingdojo.projectmanager.models.User;
import com.codingdojo.projectmanager.repositories.UserRepository;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepository;
	
	public User register(User newUser, BindingResult result) {

		// Reject if email is taken
		Optional<User> potentialUser = userRepository.findByEmail(newUser.getEmail());
		if (potentialUser.isPresent()) {
			result.rejectValue("email", "Matches", "This email is already taken.");
		}		

		// Reject if password doesn't match
		if(!newUser.getPassword().equals(newUser.getConfirm())) {
		    result.rejectValue("confirm", "Matches", "The Confirm Password must match Password.");
		}
		
		// Return null if result has errors
		if(result.hasErrors()) {
			return null;
		}
		
		// Hash and set password, save user to database
		String hashed = BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
		newUser.setPassword(hashed);
		return userRepository.save(newUser);
		
	}

	public User login(LoginUser newLoginObject, BindingResult result) {

		// Find user in the DB by email
		Optional<User> potentialUser = userRepository.findByEmail(newLoginObject.getEmail());
		if (!potentialUser.isPresent()) {
			result.rejectValue("email", "Matches", "User not found.");
			return null;
		}
		
		User user = potentialUser.get();
		
		// Reject if BCrypt password match fails
		if(!BCrypt.checkpw(newLoginObject.getPassword(), user.getPassword())) {
		    result.rejectValue("password", "Matches", "Invalid Password.");
		}
		
		// Return null if result has errors
		if(result.hasErrors()) {
			return null;
		}
		
		//Otherwise, return the user object
		return user;
	}
	
	public User findById(Long id) {
		Optional<User> potentialUser = userRepository.findById(id);
		if(potentialUser.isPresent()) {
			return potentialUser.get();
		}
		return null;
	}
	
	public List<User> allUsers(){
		return userRepository.findAll();
	}
	
	public User updateUser(User user) {
		return userRepository.save(user);
	}
	
	public List<User> getProjectsIn(Project project){
		return userRepository.findByProjects(project);
	}
	
	public List<User> getProjectsNotIn(Project project){
		return userRepository.findByProjectsNotContains(project);
	}
}
