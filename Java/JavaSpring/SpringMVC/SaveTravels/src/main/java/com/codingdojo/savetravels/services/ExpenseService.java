package com.codingdojo.savetravels.services;

import java.util.ArrayList;

import org.springframework.stereotype.Service;

import com.codingdojo.savetravels.models.Expense;
import com.codingdojo.savetravels.repositories.ExpenseRepository;

@Service
public class ExpenseService {
	private final ExpenseRepository expenseRepository;
	
	public ExpenseService(ExpenseRepository expenseRepository) {
		this.expenseRepository = expenseRepository;
	}
	
	// returns all expenses
	public ArrayList<Expense> allExpenses(){
		return expenseRepository.findAll();
	}
	
	// creates a new expense
	public Expense createExpense(Expense e) {
		return expenseRepository.save(e);
	}
}
