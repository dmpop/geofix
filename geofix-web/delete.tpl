<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>Delete Record</title>
<div id="content">
<h1>Delete record {{no}}?</h1>
<form action="/delete/{{no}}" method="GET">
<input type="submit" id="btn" class="red" name="delete" value="Delete">
</form>
<p><a href="/geofix">Back</a></p>
</div>
