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

<title>New Dojo</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark text-light m-5 p-3 border border-dark w-50">
		<h1 class="text-warning">New Dojo</h1>
		<form:form action="/createDojo" method="POST" modelAttribute="dojo">
			<div class="d-flex flex-column w-50">
				<form:label path="name">Name</form:label>
				<form:errors path="name" class="text-danger"/>
				<form:input path="name"/>
			</div>
			<button class="btn btn-success mt-2" type="submit">Create</button>
		</form:form>
		</div>
</body>
</html>