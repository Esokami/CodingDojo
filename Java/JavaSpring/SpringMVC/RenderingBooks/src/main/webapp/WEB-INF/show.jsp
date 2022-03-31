<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>  

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- For any Bootstrap that uses JS or jQuery-->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

<title>Book</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark text-light m-5 p-3 border border-dark">
		<h1 class="text-info"><c:out value="${book.title}"/></h1>
		<h3>Description: <c:out value="${book.description}"/></h3>
		<h3>Language: <c:out value="${book.language}"/></h3>
		<h3>Number of Pages: <c:out value="${book.numberOfPages}"/></h3>
	</div>
</body>
</html>