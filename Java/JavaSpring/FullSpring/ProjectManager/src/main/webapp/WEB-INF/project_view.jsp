<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!-- c:out ; c:forEach etc. --> 
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!-- Formatting (dates) --> 
<%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<!-- form:form -->
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!-- for rendering errors on PUT routes -->
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

<title>View Project</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark text-light m-5 p-3 border border-dark rounded">
		<div class="d-flex flex-column">
			<h1 class="text-danger text-center">Project Details</h1>
			<a href="/dashboard">Back to Dashboard</a>
		</div>
		<div class="d-flex border-top border-light mt-2">
			<div class="p-2 d-flex flex-column">
				<h5>Project:</h5>
				<h5 class="mt-2">Description:</h5>
				<h5 class="mt-2">Due Date:</h5>	
			</div>
			<div class="p-2 d-flex flex-column">
				<p><c:out value="${project.title}"></c:out></p>
				<p><c:out value="${project.description}"></c:out></p>
				<p><fmt:formatDate value="${project.dueDate}" pattern="MM/dd/yyyy"/></p>
			</div>
		</div>
		<div class="border-top border-light mt-2">
			<a href="#">See Tasks!</a>
		</div>
		<a href="/dashboard/delete/${project.id}">Delete</a>
	</div>
</body>
</html>