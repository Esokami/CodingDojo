<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>   

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    

<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>  

<%@ page isErrorPage="true" %>     

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- For any Bootstrap that uses JS or jQuery-->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

<title>Edit</title>
</head>
<body class="bg-secondary">
	<div class="m-5 p-3 bg-dark w-75 rounded text-light">
	<div class="d-flex justify-content-between">
		<h1 class="text-warning">Edit Language</h1>
		<div>
			<form action="/languages/${language.id}" method="POST">
			<input type="hidden" name="_method" value="delete">
			<button class="btn btn-danger" type="submit">delete</button>
			</form>
			<a href="/languages">Dashboard</a>
		</div>
	</div>
	<form:form class="d-flex flex-column align-items-center" action="/languages/edit/${id}" method="POST" modelAttribute="language">
    	<input type="hidden" name="_method" value="put">
			<div class="d-flex flex-column w-50">
				<form:label path="name">Name:</form:label>
				<form:errors path="name" class="text-danger"/>
				<form:input path="name"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="creator">Creator:</form:label>
				<form:errors path="creator" class="text-danger"/>
				<form:input path="creator"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="version">Amount:</form:label>
				<form:errors path="version" class="text-danger"/>
				<form:input type="number" step="any" min="0" path="version"/>
			</div>
			<button class="btn btn-warning mt-2" type="submit">Submit</button>
	</form:form>
	</div>
</body>
</html>