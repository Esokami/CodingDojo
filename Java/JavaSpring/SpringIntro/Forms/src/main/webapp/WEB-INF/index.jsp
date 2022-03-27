<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Forms</title>
</head>
<body>
	<h3>Login</h3>
	<form action="/login" method="POST">
		<label>Email:</label>
		<input type="text" name="email">
		<label>Password:</label>
		<input type="text" name="password">
		<input type="submit" value="login">
	</form>
	
	<form action="/search">
		<label>Search:</label>
		<input type="text" name="searchTerm">
		<input type="submit">
	</form>
	
	<h3>Pay</h3>
    <form action="/processPayment" method="post">
        <input type="hidden" name="productID" value="128">
        <label>Credit Card Number</label>
        <input type="text" name="creditCardNumber">
        <label>Expiration Date</label>
        <input type="date" name="expDate">
        <input type="submit">
    </form>
    
</body>
</html>