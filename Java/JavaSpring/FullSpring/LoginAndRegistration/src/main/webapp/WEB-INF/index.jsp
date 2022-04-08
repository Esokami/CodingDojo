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

<title>Login/Register</title>
</head>
<body class="bg-secondary">
 <div class="container d-flex flex-column align-items-left text-light bg-dark w-50">
 		<h1>Welcome!</h1>
 		<h2>Join our growing community!</h2>
        <div class="bg-dark d-flex flex-column align-items-left text-info">
            <h1>Register</h1>
            <form:form class="d-flex flex-column mb-3 text-light" action="/register" method="POST" modelAttribute="newUser">
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="username">User Name:</form:label>
                    <form:errors path="username" class="text-danger"/>
                    <form:input path="username"/>
                </div>
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="email">Email:</form:label>
                    <form:errors path="email" class="text-danger"/>
                    <form:input path="email"/>
                </div>
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="password">Password:</form:label>
                    <form:errors path="password" class="text-danger"/>
                    <form:input type="password" path="password"/>
                </div>
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="confirm">Confirm Password:</form:label>
                    <form:errors path="confirm" class="text-danger"/>
                    <form:input type="password" path="confirm"/>
                </div>
                <button type="submit" class="btn btn-info">Register</button>
            </form:form>
        </div>
        <div class="bg-dark d-flex flex-column align-items-left text-success">
            <h1>Login</h1>
            <form:form class="d-flex flex-column mb-3 text-light" action="/login" method="POST" modelAttribute="newLogin">
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="email">Email:</form:label>
                    <form:errors path="email" class="text-danger"/>
                    <form:input path="email"/>
                </div>
                <div class="p-2 d-flex justify-content-between">
                    <form:label path="password">Password:</form:label>
                    <form:errors path="password" class="text-danger"/>
                    <form:input type="password" path="password"/>
                </div>
                <button type="submit" class="btn btn-success">Login</button>
            </form:form>
        </div>
    </div>
</body>
</html>