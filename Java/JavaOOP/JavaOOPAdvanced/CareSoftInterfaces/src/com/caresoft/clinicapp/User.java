package com.caresoft.clinicapp;

public class User {
	protected Integer id;
	protected int pin;
	
	// To Do: Getters and Setters
	// Implement a constructor that takes an ID
	
	public Integer getID() {
		return id;
	}
	
	public int getPin() {
		return pin;
	}
	
	public void setID(Integer id) {
		this.id = id;
	}
	
	public void setPin(int pin) {
		this.pin = pin;
	}
	
	public User(Integer id) {
		this.id = id;
	}
}
