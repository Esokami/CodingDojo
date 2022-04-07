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

<title>New Ninja</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark text-light m-5 p-3 border border-dark w-75">
		<h1 class="text-warning">New Ninja</h1>
		<form:form action="/createNinja" method="POST" modelAttribute="ninja">
			<div class="d-flex flex-column w-50">
				<form:label path="dojo">Dojo</form:label>
				<form:select path="dojo">
        			<c:forEach var="oneDojo" items="${dojos}">
            			<!--- Each option VALUE is the name of the Dojo --->
            			<form:option value="${oneDojo.id}" path="dojo">
            			<!--- This is what shows to the user as the option --->
                			<c:out value="${oneDojo.name}"/>
            			</form:option>
        			</c:forEach>
    			</form:select>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="firstName">First Name:</form:label>
				<form:errors path="firstName" class="text-danger"/>
				<form:input path="firstName"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="lastName">Last Name:</form:label>
				<form:errors path="lastName" class="text-danger"/>
				<form:input path="lastName"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="age">Age:</form:label>
				<form:errors path="age" class="text-danger"/>
				<form:input type="number" path="age"/>
			</div>
			<button class="btn btn-success mt-2" type="submit">Create</button>
		</form:form>
		</div>
</body>
</html>