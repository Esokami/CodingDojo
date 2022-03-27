<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- For any Bootstrap that uses JS or jQuery-->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

<title>Omikuji Form</title>
</head>
<body class="bg-secondary">
	<div class="mx-auto" style="width: 300px;">
		<div class="p-3 bg-dark text-white border border-dark rounded">
			<h1 class="text-info">Send an Omikuji!</h1>		
			<form action="/createFortune" method="POST" class="d-flex flex-column">
				<label for="number">Pick any number from 5 to 25</label>
				<input class="w-25" type="number" name="number" min="5" max="25">
				<label>Enter the name of any city.</label>
				<input type="text" name="city">
				<label>Enter the name of any real person.</label>
				<input type="text" name="person">
				<label>Enter professional endeavor or hobby:</label>
				<input type="text" name="endeavor">
				<label>Enter any type of living thing.</label>
				<input type="text" name="organism">
				<label for="comment">Say something nice to someone:</label>
				<textarea name="comment" rows="4" cols="50"></textarea>
				<label>Send and show a friend.</label>
				<button class="btn btn-info text-dark" type="submit">Send</button>
			</form>
		</div>
	</div>
</body>
</html>