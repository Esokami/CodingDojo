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

<title>View</title>
</head>
<body class="bg-secondary">
	<div class="m-5 p-3 bg-dark w-75 rounded text-light">
	<div class="d-flex justify-content-between">
		<h1 class="text-info">Language Details</h1>
		<a href="/languages">Dashboard</a>
	</div>
	<div class="d-flex">
		<div class="m-3 text-warning">
			<p>Name:</p>
			<p>Creator:</p>
			<p>Version:</p>
		</div>
		<div class="m-3">
			<p><c:out value="${language.name}"/></p>
			<p><c:out value="${language.creator}"/></p>
			<p><c:out value="${language.version}"/></p>
		</div>
	</div>
	<div>
		<a href="/languages/edit/${language.id}">Edit</a>
		<form action="/languages/${language.id}" method="POST">
			<input type="hidden" name="_method" value="delete">
			<button class="btn btn-danger" type="submit">delete</button>
		</form>
	</div>
	</div>
</body>
</html>