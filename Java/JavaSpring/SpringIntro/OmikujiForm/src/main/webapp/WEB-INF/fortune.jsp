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

<title>Fortune</title>
</head>
<body class="bg-secondary">
	<div class="mx-auto bg-dark p-2 border border-dark rounded" style="width: 300px;">
		<h1 class="text-success">Here's Your Omikuji!</h1>
		<div class="p-2 bg-warning text-dark border border-dark rounded">
			<p>In <c:out value="${currentNumber}"/> years, you will
			live in <c:out value="${currentCity}"/> with <c:out value="${currentPerson}"/>
			as your room mate, <c:out value="${currentEndeavor}"/> for a living.
			The next time you see a <c:out value="${currentOrganism}"/>, you will
			have good luck. Also, <c:out value="${currentComment}"/>.
			</p>
		</div>
		<a href="http://localhost:8080/">Go Back</a>
	</div>
</body>
</html>