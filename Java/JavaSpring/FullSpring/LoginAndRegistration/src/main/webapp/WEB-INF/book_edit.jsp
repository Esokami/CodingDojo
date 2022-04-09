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

<title>Edit Book</title>
</head>
<body>
	<h1>Edit Book</h1>
	<form:form action="/books/edit/${book.id}" method="post" modelAttribute="book">
    	<input type="hidden" name="_method" value="put">
    	<p>
        	<form:label path="title">Title</form:label>
        	<form:errors path="title"/>
        	<form:input path="title"/>
    	</p>
    	<p>
        	<form:label path="description">Description</form:label>
        	<form:errors path="description"/>
        	<form:textarea path="description"/>
    	</p>
    	<p>
        	<form:label path="language">Language</form:label>
        	<form:errors path="language"/>
        	<form:input path="language"/>
    	</p>
    	<p>
        	<form:label path="numberOfPages">Pages</form:label>
        	<form:errors path="numberOfPages"/>     
        	<form:input type="number" path="numberOfPages"/>
    	</p>    
    	<input type="submit" value="Submit"/>
	</form:form>
</body>
</html>